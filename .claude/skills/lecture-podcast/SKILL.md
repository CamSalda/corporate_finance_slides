---
name: lecture-podcast
description: Make the companion podcast episode of one lecture of this Corporate Finance course (script from the deck's .qmd, MP3 rendered with The Finance and Economics Papers Podcast tools), or plan one. Use when asked for a lecture podcast, companion episode, audio companion, or to render or re-render an episode.
---

# Lecture companion podcast

Read `quarto slides/podcast-companion.md` first: it holds the rules (header, structure, equations, tone) and
the facts about the podcast repository. This file is the checklist.

## Before writing

1. Check the podcast repo is on the right branch and has its environment:
   `git -C C:/Users/camil/Documents/the-finance-papers-podcast branch --show-current` must print
   `escp-pronunciation` (switch to it if not), and `C:/Users/camil/Documents/the-finance-papers-podcast/.venv/Scripts/python.exe`
   must exist (recreate it with the commands in the guide if not).
2. Make sure no other render is running (`nvidia-smi` memory use near idle, no `make_podcast.py` process).
3. Read `quarto slides/LectureN/lectureN.qmd` in full and `quarto slides/Lecture11/lecture11_podcast_script.md`
   (the reference) or the previous lecture's script for continuity.
4. List the slides (`grep -nE '^##'`) and open every image whose numbers the script will quote.

## Planning (when asked for a plan first)

Give: slide count, formula-block count, recap-slide count, target length; a section-by-section outline naming
which examples and exercises are done with numbers and which equation blocks are summarised with a slide
pointer; the jokes planned; the figures to check. Then wait for "go ahead".

## Writing

- File: `quarto slides/LectureN/lectureN_podcast_script.md`, header copied from the reference script with the
  lecture's title, chapters and topics.
- Recap of the previous lecture first when the deck has recap slides, then the sections in the deck's order,
  then `## Wrap-up: the recap` with the quiz answers.
- Count spoken words with `grep -E '^(MEI|MIGUEL): ' <script> | wc -w`; divide by 172 for the minutes; set the
  `**Length:**` line. Under 24 minutes: add exchanges, not padding.
- Check every joke against the tone rules; keep "ESCP" written as is.

## Rendering

From the podcast repo, in the background, one at a time:

```
cd C:/Users/camil/Documents/the-finance-papers-podcast && .venv/Scripts/python.exe .agents/skills/paper-to-podcast/make_podcast.py "<abs path>/quarto slides/LectureN/lectureN_podcast_script.md" "<abs path>/quarto slides/LectureN/lectureN_podcast.mp3"
```

Both paths are required. The render takes about as long as the episode. While it runs, write the next script if
several lectures were asked for.

## After the render

1. Measure the MP3 (`soundfile`, see the guide) and set the header length to the measured minutes if it is off by
   one minute or more.
2. `git add` the script and the MP3, commit `Lecture N companion podcast episode` (no attribution lines), push
   the current branch.
3. Report: length, commit hash, what was done with numbers and what was pointed to the slides, the jokes used,
   anything to listen to first.

## Do not

- Render with the `main` branch of the podcast repo (ESCP would be read as a word).
- Run two renders at once (one GPU).
- Commit anything into the podcast repo for the course.
- Quote a number that is not on a slide.
- Walk through a derivation formula by formula.
