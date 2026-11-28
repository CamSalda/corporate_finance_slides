# Lecture companion episodes

How to turn a lecture deck of this course into an episode of The Finance and Economics Papers Podcast. The
hosts, the voices and the renderer are those of the podcast repository; the rules below are what changes for a
lecture instead of a paper. The Claude skill `.claude/skills/lecture-podcast/SKILL.md` at the root of this repo
follows this guide step by step.

## The podcast repository and its branch

- Local clone: `C:\Users\camil\Documents\the-finance-papers-podcast`
  (GitHub: `CamSalda/the-finance-and-economics-papers-podcast`).
- The renderer is `.agents/skills/paper-to-podcast/make_podcast.py`; the paper skill that documents it is
  `.agents/skills/paper-to-podcast/SKILL.md`. Kokoro's model files live in `.agents/skills/paper-to-podcast/models/`,
  Qwen3-TTS is downloaded to the Hugging Face cache on first use.
- **Branch `escp-pronunciation` must be checked out** when rendering. It differs from `main` in two lines of
  `make_podcast.py`: the pronunciation tables of both voices map `ESCP` to `E. S. C. P.`, so the school is
  spelled letter by letter instead of read as a word; and `.gitignore` ignores `.venv/`. This change is kept as a
  local branch only (PR #27 was closed on purpose, the podcast repo stays about papers). Check with
  `git -C <repo> branch --show-current`; if it says `main`, run `git -C <repo> switch escp-pronunciation`.
- Nothing from the course is committed to the podcast repo. Scripts and MP3s live here, beside each deck.

## The render environment

A uv virtual environment inside the podcast repo, ignored by git: `<repo>\.venv` (Python 3.11.15, torch 2.6.0
with CUDA 12.4, kokoro-onnx, qwen-tts, lameenc, scipy, soundfile). If it is missing, recreate it from the
podcast repo:

```
uv venv --clear --python 3.11 .venv
.venv\Scripts\python.exe -m pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu124
.venv\Scripts\python.exe -m pip install kokoro-onnx qwen-tts lameenc scipy soundfile
```

An NVIDIA GPU with about 8 GB of memory is required (Qwen3-TTS voices Miguel). On the RTX 4060 laptop a render
takes about as long as the episode: 25 to 30 minutes. Run it in the background and never two at once.

## Files

- Source: the deck's `.qmd` (the source of both the PDF and the HTML). Main deck only; the extras decks, the
  course-intro deck and the final-exam deck are left out unless asked.
- Output, beside the deck: `LectureN/lectureN_podcast_script.md` and `LectureN/lectureN_podcast.mp3`, both
  committed.
- `Lecture11/lecture11_podcast_script.md` is the reference script; Lectures 1 to 10 follow it.

## Workflow for one lecture

1. Read the deck's `.qmd` in full. Open every image whose numbers the script will quote (tables, figures with
   values, news headlines) and take the numbers from the image, not from memory.
2. Write the script (format below). Count the spoken words:
   `grep -E '^(MEI|MIGUEL): ' script.md | wc -w`. The voices average **172 words per minute** measured over
   ten episodes; set the header length from the count. Aim for 25 to 30 minutes; if the first draft is under
   24, add exchanges (Miguel's questions, a wrong answer corrected, a link to an earlier lecture) rather than
   padding Mei's monologues.
3. Render, from the podcast repo, in the background:
   `.venv\Scripts\python.exe .agents\skills\paper-to-podcast\make_podcast.py "<slides>\LectureN\lectureN_podcast_script.md" "<slides>\LectureN\lectureN_podcast.mp3"`.
   The output path is required: the renderer's default name parser expects a paper citation line.
4. When it finishes, measure the MP3 and fix the header if it is off by a minute or more:
   `python -c "import soundfile as sf; f=sf.SoundFile('lectureN_podcast.mp3'); print(f.frames/f.samplerate/60)"`.
5. Commit script and MP3 together, message `Lecture N companion podcast episode`, and push the current branch.
   No attribution lines in the commit.

If a render has to be stopped (script changed after it started), kill it, delete the partial MP3 and start again.

## Header

Title line `# The Finance and Economics Papers Podcast: Lecture Companion. Corporate Finance, Lecture N: <title>`,
then the "Lecture companion" block quote (course, school, year, textbook chapters, "all numbers and examples
come from the lecture slides"), then the list: Lecture, Textbook, Topics, Length, Hosts. Mei is the guide,
Miguel the student. Only lines starting with `MEI: ` or `MIGUEL: ` are spoken; `##` section headings are not.

## Opening

Same two welcome lines as every episode. Then Mei says it is a special format: a lecture companion, which
lecture of which course, at ESCP, which textbook chapters, and the plan of the lecture in a few sentences. When
the deck starts with recap slides of the previous lecture, the episode starts there too, briefly (two to four
minutes, however many recap slides there are).

## Structure

Follow the deck's sections in order (A, B, C...) and name them, so a student can follow with the slides open.
Worked examples and exercises are spoken with their numbers, step by step, because they are what the exam looks
like. Close with `## Wrap-up: the recap`: the lecture in one minute, section by section, then the quiz questions
from the last slides with their answers, Miguel's one-line takeaway, Mei's reading advice, and one line of
goodbye.

## Equations

The decks are heavy with equations. Do not walk through them one by one. For each block of formulas give the
general intuition in words, say that it is a set of equations, and send the listener to the slides: "this part
has a set of equations; we explain it in general terms, the best thing is to check them directly on the slides."
Name the slide numbers or the example so they can find it. Derivations that span several slides (MM II, the
beta formulas, the cost of equity with taxes) get the shape of each step in words and nothing more. Small
worked examples with numbers work well aloud and are always spelled out.

## Tone

- Positive about the course. Jokes say "this is exciting", "this one is great", never "this is boring" or "my
  soul is leaving my body".
- Innocent jokes about the professor and his slides are welcome: "Professor Saldarriaga really went far on this
  one", "he was clearly excited about this last class", the number of recap slides, the five exclamation marks,
  the names of the fictional firms (Tour moche SA, Perkscom, Genron), the pictures and examples he chose.
- One fallacy per lecture is a running theme of the course (the 15% discount rate, EPS and dilution, "fewer
  shares so the price rises", "bird in the hand"); call it out when it comes.
- ESCP is spelled letter by letter when spoken: the renderer on the `escp-pronunciation` branch turns "ESCP"
  into "E. S. C. P.". Write "ESCP" in the script.
- Every number comes from the slides. Short spoken sentences, no em-dashes, technical terms defined on first use.
  Running references to earlier lectures (Intel and Coca-Cola, Jérôme, the Dragon Ball theme park) are welcome.

## Episodes so far

| Lecture | Script words spoken | MP3 |
|:--|--:|--:|
| 1. Capital Markets and the Pricing of Risk | 4,363 | 26.4 min |
| 2. Portfolio Choice and Diversification | 4,207 | 24.5 min |
| 3. The Efficient Frontier and the Best Portfolio | 4,958 | 29.8 min |
| 4. The CAPM | 4,693 | 28.2 min |
| 5. Investor Behavior and Capital Market Efficiency | 4,391 | 26.2 min |
| 6. Estimating the Cost of Capital | 5,371 | 31.8 min |
| 7. Capital Structure in a Perfect Market (I) | 4,376 | 26.0 min |
| 8. Capital Structure in a Perfect Market (II) | 5,046 | 30.0 min |
| 9. Debt and Taxes | 4,994 | 29.6 min |
| 10. Payout Policy | 4,621 | 27.8 min |
| 11. Long-Term Financing | 5,690 | 33 min |
| 12. Options and Risk Management | 4,383 | 24.8 min |
