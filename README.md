# Corporate Finance slides

Quarto slide decks for the Corporate Finance course, ESCP Business School (Camilo Saldarriaga,
2025/2026). Migrated from the original beamer decks in `../slides/`.

Each deck renders to two formats: a reveal.js HTML deck for teaching and a beamer PDF for
handouts.

## Usage

```bash
pixi run render     # render every deck, both formats
pixi run preview    # live preview in the browser while editing
pixi run clean      # drop quarto build artifacts
```

The beamer PDF needs a LaTeX installation on the system (MiKTeX or TeX Live). It is not pulled
into the pixi environment.

## Layout

```
quarto slides/
  _quarto.yml            shared format config for every deck
  escp.scss              the ESCP theme: corporate blue #240085
  _beamer-preamble.tex   matching colors for the PDF output
  Lecture1/ ... Lecture12/
```

One folder per lecture, holding its `.qmd` files, the ESCP logo and only the images that lecture
uses. Restyling the whole course means editing `escp.scss` alone.
