# Lecture companion episodes

How to turn a lecture deck of this course into an episode of The Finance and Economics Papers Podcast. The
tools, hosts and renderer are those of the podcast repository
(`C:\Users\camil\Documents\the-finance-papers-podcast`, skill `.agents/skills/paper-to-podcast/SKILL.md`). The
rules below are what changes for a lecture instead of a paper. `Lecture11/lecture11_podcast_script.md` is the
reference script.

## Files

- Source: the deck's `.qmd` (the source of both the PDF and the HTML). Main deck only; the extras decks and the
  course-intro deck are left out unless asked.
- Output, beside the deck: `LectureN/lectureN_podcast_script.md` and `LectureN/lectureN_podcast.mp3`.
- Render, from the podcast repo, with its `.venv` (Python 3.11, CUDA):
  `.venv\Scripts\python.exe .agents\skills\paper-to-podcast\make_podcast.py <script.md> <lectureN_podcast.mp3>`.
  The output path is required: the renderer's default name parser expects a paper citation. Rendering takes about
  as long as the episode (about 30 minutes on the RTX 4060 laptop); run it in the background, one at a time.

## Header

Copy the header of the Lecture 11 script. Title line `# The Finance and Economics Papers Podcast: Lecture
Companion. Corporate Finance, Lecture N: <title>`, then the "Lecture companion" block quote (course, school,
year, textbook chapters, "all numbers and examples come from the lecture slides"), then the list: Lecture,
Textbook, Topics, Length, Hosts. Mei is the guide, Miguel the student.

## Opening

Same two welcome lines as every episode. Then Mei says it is a special format: a lecture companion, which
lecture of which course, at ESCP, which textbook chapters, and the plan of the lecture in a few sentences. When
the deck starts with recap slides of the previous lecture, the episode starts there too, briefly.

## Structure

Follow the deck's sections in order (A, B, C...) and name them, so a student can follow with the slides open.
Close with `## Wrap-up: the recap`: the lecture in one minute, section by section, then the quiz questions from
the last slides with their answers, then one line of goodbye.

## Equations

The decks are heavy with equations. Do not walk through them one by one. For each block of formulas give the
general intuition in words, say that it is a set of equations, and send the listener to the slides: "this part
has a set of equations; we explain it in general terms, the best thing is to check them directly on the slides."
Name the slide or the example so they can find it. Spell out small worked examples with numbers, which work well
aloud; skip derivations.

## Tone

- Positive about the course. Jokes say "this is exciting", "this one is great", never "this is boring" or "my
  soul is leaving my body".
- Innocent jokes about the professor and his slides are welcome: "Professor Saldarriaga really went far on this
  one", "he was clearly excited about this last class", remarks on the pictures and examples he chose.
- ESCP is spelled letter by letter when spoken: the renderer turns "ESCP" into "E. S. C. P." Write "ESCP" in the
  script.
- Every number comes from the slides. Short spoken sentences, no em-dashes, technical terms defined on first use.
- About 150 words per minute. Aim for 25 to 30 minutes; a long deck may run a little over, as Lecture 11 did
  at 33.
