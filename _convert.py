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

# Beamer frames hold more than a reveal slide comfortably fits, so long slides are shrunk in
# two steps: Quarto's own {.smaller}, then the theme's stronger {.dense} on top of it.
SMALLER_THRESHOLD = 400
DENSE_THRESHOLD = 800

STRIP_COMMANDS = ["vspace", "hspace", "vskip", "medskip", "smallskip", "bigskip", "bigstrut"]

# Pandoc discards LaTeX font sizing, which would blow up footnote-sized source credits into
# body text. Sentinel paragraphs survive the round trip and become styled divs afterwards.
FONT_SIZES = ["tiny", "scriptsize", "footnotesize", "small", "large", "Large"]
SIZE_OPEN = "QZSIZE{}QZ"
SIZE_CLOSE = "QZENDSIZEQZ"


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
    """Return (title, body) for every frame that belongs in the slides.

    A frame may carry an overlay specification before its options. `<beamer:0>` marks a frame
    the original deck shows only in the handout, so it is dropped; `<handout:0>` marks the
    reverse and is kept. The title page is dropped too, Quarto builds its own from the YAML.
    """
    pattern = re.compile(
        r"\\begin\{frame\}(<[^>]*>)?(\[[^\]]*\])?(?:\{(.*?)\})?\s*(.*?)\\end\{frame\}",
        re.DOTALL,
    )
    frames = []
    for overlay, options, title, content in pattern.findall(body):
        if "beamer:0" in overlay or "\\titlepage" in content:
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


def closing_brace(text: str, start: int) -> int | None:
    """Index of the brace closing the group that opens at `start`."""
    depth = 0
    for index in range(start, len(text)):
        if text[index] == "{":
            depth += 1
        elif text[index] == "}":
            depth -= 1
            if depth == 0:
                return index
    return None


def mark_font_sizes(fragment: str) -> str:
    """Replace LaTeX font sizing with sentinels pandoc carries through as paragraphs.

    The `{\\small ...}` switch form has to be brace-matched rather than regex-matched: a lazy
    match would stop at the first closing brace, which is usually inside the maths it wraps.
    """
    def wrap(size: str, inner: str) -> str:
        return f"\n\n{SIZE_OPEN.format(size)}\n\n{inner}\n\n{SIZE_CLOSE}\n\n"

    for size in FONT_SIZES:
        fragment = re.sub(
            rf"\\begin\{{{size}\}}(.*?)\\end\{{{size}\}}",
            lambda m, s=size: wrap(s, m.group(1)),
            fragment,
            flags=re.DOTALL,
        )

    switch = re.compile(r"\{\\(" + "|".join(sorted(FONT_SIZES, key=len, reverse=True)) + r")(?![a-zA-Z])")
    for match in reversed(list(switch.finditer(fragment))):
        end = closing_brace(fragment, match.start())
        if end is None:
            continue
        inner = fragment[match.end() : end]
        fragment = fragment[: match.start()] + wrap(match.group(1), inner) + fragment[end + 1 :]
    return fragment


def apply_font_sizes(markdown: str) -> str:
    """Turn the surviving sentinels into divs the theme styles."""
    for size in FONT_SIZES:
        markdown = markdown.replace(SIZE_OPEN.format(size), f"::: {{.{size.lower()}}}")
    return markdown.replace(SIZE_CLOSE, ":::")


def strip_resizebox(fragment: str) -> str:
    """Unwrap \\resizebox{w}{h}{$...$}, keeping only the maths it scales.

    Dropping just the two size arguments would leave the content group's braces and inline
    `$` behind, which breaks the display environment the box usually sits in.
    """
    while (start := fragment.find("\\resizebox")) != -1:
        cursor = start + len("\\resizebox")
        groups = []
        for _ in range(3):
            cursor = fragment.find("{", cursor)
            end = closing_brace(fragment, cursor) if cursor != -1 else None
            if end is None:
                return fragment
            groups.append(fragment[cursor + 1 : end])
            cursor = end + 1
        content = groups[2].strip().strip("$")
        fragment = fragment[:start] + content + fragment[cursor:]
    return fragment


def clean_fragment(fragment: str) -> str:
    """Remove spacing commands and beamer-only markup pandoc cannot map."""
    for command in STRIP_COMMANDS:
        fragment = re.sub(rf"\\{command}\*?(\{{[^}}]*\}})?", "", fragment)
    fragment = strip_resizebox(fragment)
    fragment = fragment.replace("\\par", "")
    fragment = fragment.replace("\\pause", "\n\n. . .\n\n")
    return mark_font_sizes(expand_column_commands(fragment))


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
    # Pandoc wraps raw equation environments in $$, which nests two display modes.
    markdown = re.sub(r"\\(begin|end)\{equation\*?\}", "", markdown)
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
        markdown = latex_to_markdown(clean_fragment(content))
        markdown = fix_images(fix_math(convert_divs(apply_font_sizes(markdown))))
        markdown = markdown.strip()
        heading = f"## {title}" if title else "##"
        if len(markdown) > DENSE_THRESHOLD:
            heading += " {.smaller .dense}"
        elif len(markdown) > SMALLER_THRESHOLD:
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
