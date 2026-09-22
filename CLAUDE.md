# CLAUDE.md

Quarto slide decks for the Corporate Finance course, ESCP Business School (Camilo Saldarriaga,
2025/2026). Migrated from beamer. Each deck renders twice: reveal.js HTML for teaching, beamer
PDF for handouts.

## Commands

```bash
pixi run render     # render every deck, both formats
pixi run preview    # live preview while editing
pixi run clean      # drop quarto build artifacts
```

The beamer PDF needs a system LaTeX (MiKTeX / TeX Live); it is not in the pixi environment.
`pre-commit` (trailing whitespace, EOF, YAML, line endings, 50 MB file cap, ruff) is a dependency
— run it before committing.

## Layout

```
quarto slides/
  _quarto.yml            shared format config for every deck
  escp.scss              reveal.js theme, ESCP blue #240085
  _beamer-preamble.tex   matching colors for the PDF
  Lecture1/ … Lecture12/ one folder per lecture: .qmd + only the images it uses
```

Decks: L1 pricing of risk (+ `intro.qmd`, the course-admin deck), L2 portfolio choice and
diversification (+ `lecture2-extras.qmd`), L3 efficient frontier, L4 CAPM,
L5 market efficiency, L6 cost of capital, L7-8 capital structure (perfect market), L9 debt and
taxes, L10 payout policy, L11 long-term financing, L12 options and risk management (+
`final-exam.qmd`). Rendered `.html` and `.pdf` are committed next to their source.

Restyling the whole course means editing `escp.scss` alone — do not put per-deck CSS in a `.qmd`.

## Slide conventions

- One `##` per slide. Continuation slides repeat the title with `(con't)`, `(con't 2)`.
- **Slide numbers** mean the counter shown in the deck's bottom-right corner: the title slide is
  1, and untitled `##` slides (a bare `##` with just an image) count too. Grep for `^##`, not
  `^## `, or the untitled ones are missed and every number after them is off by one.
- Section slides are lettered to match the deck's `## Plan` / `## Outline`: `## A. …`.
- Slide sizing classes, in order of severity: `{.smaller}`, then `{.smaller .dense}` for frames
  that were already crowded in beamer. `.dense` sets an absolute size, it does not compound.
- **Fit the slide.** Reveal slides are 1050×700 and do not scroll — content that overruns just
  spills over the footer. Budget roughly: 10 lines of body text at default size, 16 with
  `{.smaller}`, 24 with `{.smaller .dense}`. A display formula (`$$…$$`) costs ~2 lines, a
  `.box` ~4, a title that wraps to a second line ~2. Count before adding, and count the wrapped
  lines, not the source lines — a bullet that reads as three lines on screen costs three.
- When a slide overruns, cut words first, then step up the sizing class, and only then split it
  into a `(con't)` slide. Shrinking alone makes it unreadable at the back of the room.
- Keep titles to one line: 45 characters or so at default size. Long titles are what push the
  body down.
- Other theme classes: `.center`, `.result`, `.box .box-a` / `.box-b`, `.tagline`, and the
  carried-over beamer sizes `.tiny .scriptsize .footnotesize .small .large`.
- Images live beside the deck, referenced bare: `![](figure12p2.png){fig-align="center"}`.
  Centered figures go inside `::: {.center}`. Two-up layouts use `::: {.columns}` blocks.
- Chapter references point at the Berk & DeMarzo textbook, e.g. `(Chap. 12.3)`. Keep them.
- Most decks end with a `## Quiz` slide.

## Writing for this audience

Management students with mixed backgrounds, not necessarily strong in mathematics. Write every
explanation as simply as possible and avoid heavy notation: no summation or product signs, no
limits, no epsilon-style conditions, no unexplained symbols. Prefer longhand
(`Div1/(1+r) + Div2/(1+r)^2 + …`) over a compact sigma expression, plain words over formal
conditions ("as long as growth is below the discount rate" rather than `|x| < 1`), and one
plain-language intuition line after any formula.

**Why:** notation that reads as concise to a quant reader is a barrier for them, and a slide they
cannot parse teaches nothing regardless of how correct it is.

**How to apply:** state the idea in words first, show at most one formula per step, name every
symbol the first time it appears. If a derivation needs several steps, spread it across slides
rather than compressing it. This governs new content; it does not require rewriting the
professor's own original slides unless asked.

## Git

Never add Claude as a co-author or author of commits, PRs, or issues. No `Co-Authored-By` trailer,
no "Generated with Claude Code" line.
