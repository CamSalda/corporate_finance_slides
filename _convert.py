"""Convert the original beamer decks into Quarto revealjs sources.

Temporary migration scaffolding: delete once every lecture has been migrated and reviewed.

Usage: python _convert.py <lecture-folder-name> <source-tex-stem> <output-qmd-name>
Example: python _convert.py Lecture4 CorporateFinance_Lecture4 lecture4
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

SOURCE_ROOT = Path(__file__).parent.parent / "slides"
TARGET_ROOT = Path(__file__).parent / "quarto slides"

# A slide whose markdown exceeds this many characters gets Quarto's {.smaller} class.
SMALLER_THRESHOLD = 400

STRIP_COMMANDS = ["vspace", "hspace", "vskip", "medskip", "smallskip", "bigskip", "bigstrut"]


def read_source(tex_path: Path) -> str:
    """Read a deck, inlining any \\input of a shared InputTex body."""
    text = tex_path.read_text(encoding="latin-1")

    def inline(match: re.Match) -> str:
        included = (tex_path.parent / match.group(1)).resolve()
        return included.read_text(encoding="latin-1")

    return re.sub(r"\\input\{([^}]+)\}", inline, text)


def strip_comments(text: str) -> str:
    """Drop LaTeX comments, keeping escaped percent signs."""
    return re.sub(r"(?<!\\)%.*$", "", text, flags=re.MULTILINE)


def extract_frames(body: str) -> list[tuple[str, str]]:
    """Return (title, body) for every frame, skipping the plain title page."""
    pattern = re.compile(
        r"\\begin\{frame\}(\[[^\]]*\])?(?:\{(.*?)\})?\s*(.*?)\\end\{frame\}",
        re.DOTALL,
    )
    frames = []
    for options, title, content in pattern.findall(body):
        if "\\titlepage" in content:
            continue
        frames.append((title.strip(), content.strip()))
    return frames


def latex_to_markdown(fragment: str) -> str:
    """Run a frame body through pandoc."""
    result = subprocess.run(
        ["quarto", "pandoc", "-f", "latex", "-t", "markdown-raw_tex-simple_tables"],
        input=fragment,
        capture_output=True,
        text=True,
        encoding="utf-8",
        shell=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"pandoc failed: {result.stderr}")
    return result.stdout


def expand_column_commands(fragment: str) -> str:
    """Rewrite beamer's \\column{...} shorthand into explicit column environments.

    Pandoc only understands the environment form, and collapses the shorthand into a
    single undifferentiated div.
    """

    def rewrite(match: re.Match) -> str:
        inner = match.group(1)
        parts = re.split(r"\\column\{([^}]*)\}", inner)
        if len(parts) == 1:
            return match.group(0)
        columns = []
        for width, content in zip(parts[1::2], parts[2::2]):
            columns.append(f"\\begin{{column}}{{{width}}}\n{content.strip()}\n\\end{{column}}")
        return "\\begin{columns}\n" + "\n".join(columns) + "\n\\end{columns}"

    return re.sub(r"\\begin\{columns\}(.*?)\\end\{columns\}", rewrite, fragment, flags=re.DOTALL)


def clean_fragment(fragment: str) -> str:
    """Remove spacing commands and beamer-only markup pandoc cannot map."""
    for command in STRIP_COMMANDS:
        fragment = re.sub(rf"\\{command}\*?(\{{[^}}]*\}})?", "", fragment)
    fragment = re.sub(r"\\resizebox\{[^}]*\}\{[^}]*\}", "", fragment)
    fragment = fragment.replace("\\par", "")
    fragment = fragment.replace("\\pause", "\n\n. . .\n\n")
    return expand_column_commands(fragment)


def convert_divs(markdown: str) -> str:
    """Map pandoc's plain divs onto the classes the ESCP theme styles.

    Pandoc does not carry a column's width into the div, it leaves the raw fraction as the
    first word of the column body, so the width is recovered from there and the stray text
    removed.
    """
    markdown = re.sub(
        r"(:::+) column\s*\n\s*([\d.]+)[ \t]*",
        lambda m: f'{m.group(1)} {{.column width="{round(float(m.group(2)) * 100)}%"}}\n',
        markdown,
    )
    markdown = re.sub(r"^(\s*)(:::+) columns\s*$", r"\1\2 {.columns}", markdown, flags=re.MULTILINE)
    markdown = re.sub(r"^(\s*)(:::+) column\s*$", r"\1\2 {.column}", markdown, flags=re.MULTILINE)
    markdown = re.sub(r"^(\s*)(:::+) block\s*$", r"\1\2 {.box .box-a}", markdown, flags=re.MULTILINE)
    markdown = re.sub(r"^(\s*)(:::+) center\s*$", r"\1\2 {.center}", markdown, flags=re.MULTILINE)
    return markdown


def fix_math(markdown: str) -> str:
    """Make display math MathJax-safe.

    MathJax rejects `align*` nested inside `$$`, and does not know xcolor's palette names.
    """
    markdown = markdown.replace("\\begin{align*}", "\\begin{aligned}")
    markdown = markdown.replace("\\end{align*}", "\\end{aligned}")
    markdown = markdown.replace("\\begin{align}", "\\begin{aligned}")
    markdown = markdown.replace("\\end{align}", "\\end{aligned}")
    return markdown.replace("BrickRed", "firebrick")


def fix_images(markdown: str) -> str:
    """Centre every figure and drop pandoc's LaTeX-sizing attributes."""
    return re.sub(
        r"!\[[^\]]*\]\(([^)]+)\)(\{[^}]*\})?",
        lambda m: f'![]({m.group(1)}){{fig-align="center"}}',
        markdown,
    )


def referenced_images(text: str) -> set[str]:
    """Images a deck needs, minus the logo the shared theme already supplies."""
    return {
        name.split("/")[-1]
        for name in re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", text)
    } - {"escplogo.png"}


def deck_title(tex: str) -> str:
    """Recover the running title from the beamer footline."""
    match = re.search(r"\\usebeamerfont\{title in head/foot\}\s*(.+?)\s*\n", tex)
    title = match.group(1) if match else ""
    return title.replace("\\&", "&").replace("  ", " ").strip()


def front_matter(title: str) -> str:
    return f'---\ntitle: "Corporate Finance"\nsubtitle: "{title}"\nfooter: "{title}"\n---\n\n'


def convert(lecture: str, stem: str, output_name: str) -> None:
    source_dir = SOURCE_ROOT / lecture
    target_dir = TARGET_ROOT / lecture
    target_dir.mkdir(parents=True, exist_ok=True)

    raw = strip_comments(read_source(source_dir / f"{stem}.tex"))
    body = raw.split("\\begin{document}", 1)[1].split("\\end{document}")[0]

    slides = []
    for title, content in extract_frames(body):
        markdown = fix_images(fix_math(convert_divs(latex_to_markdown(clean_fragment(content)))))
        markdown = markdown.strip()
        heading = f"## {title}" if title else "##"
        if len(markdown) > SMALLER_THRESHOLD:
            heading += " {.smaller}"
        slides.append(f"{heading}\n\n{markdown}\n")

    document = front_matter(deck_title(raw)) + "\n".join(slides)
    (target_dir / f"{output_name}.qmd").write_text(document, encoding="utf-8")

    for image in referenced_images(raw):
        for candidate in (source_dir / image, source_dir / f"{image}.png"):
            if candidate.exists():
                shutil.copy2(candidate, target_dir / candidate.name)
                break

    print(f"{lecture}/{output_name}.qmd: {len(slides)} slides")


if __name__ == "__main__":
    convert(*sys.argv[1:4])
