# Corporate Finance slides

Quarto slide decks for the Corporate Finance course, ESCP Business School (Camilo Saldarriaga,
2026/2027). Migrated from the original beamer decks in `../slides/`.

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

## Podcast companions

Each lecture has a companion audio episode beside its deck, `LectureN/lectureN_podcast.mp3`, with its full
script in `LectureN/lectureN_podcast_script.md`. Two hosts walk through the lecture in 25 to 30 minutes,
following the slides section by section. The episodes are made with the open-source tools of
[The Finance and Economics Papers Podcast](https://github.com/CamSalda/the-finance-and-economics-papers-podcast)
(Kokoro and Qwen3-TTS voices, rendered locally on a GPU).

How to make one is in [quarto slides/podcast-companion.md](quarto%20slides/podcast-companion.md): the format
of the script, the tone rules, the podcast repository, its `escp-pronunciation` branch and its environment,
and the render command. The Claude Code skill `.claude/skills/lecture-podcast/SKILL.md` runs that procedure.
