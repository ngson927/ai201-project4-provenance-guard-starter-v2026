"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics

# Window for the moving-average type-token ratio, in words.
TTR_WINDOW = 50

# The marks punctuation_density counts. An opening bracket counts once per
# pair; a hyphen counts only when spaced, as a dash.
EXPRESSIVE_PUNCTUATION = re.compile(r"[;:—–(!?]|\s-\s")


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies. ← TODO

    Returns:
        A float. Decide yourself what scale it's on and which direction means
        "more human" — then write that down, because your combining rule
        depends on knowing it.

    A hint on what you're reaching for: the standard deviation of sentence
    lengths, probably divided by the mean so a long text and a short one are
    comparable. `statistics.stdev` is imported for you.

    Watch the edge case: a one-sentence submission has no spread at all, and
    `stdev` raises on fewer than two values. Decide what that should return
    before the attack set decides for you.

    Mine: the coefficient of variation of words-per-sentence (stdev / mean).
    0.0 means every sentence is the same length; human prose usually lands
    around 0.4–0.8. **Higher means more human.** Fewer than two sentences
    returns 0.0, and `style_signal` treats that as "no evidence", not as AI.
    """
    lengths = [len(words(s)) for s in sentences(text)]
    lengths = [n for n in lengths if n]
    if len(lengths) < 2:
        return 0.0
    return statistics.stdev(lengths) / statistics.mean(lengths)


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words. ← TODO

    Returns:
        A float between 0 and 1. Higher means more varied vocabulary.

    Worth knowing before you rely on it: this measure falls as text gets
    longer, because common words repeat. Two texts of different lengths aren't
    directly comparable on it, and if your test inputs vary a lot in length,
    that alone can look like a signal.

    Mine is the moving-average version: the plain ratio inside every window
    of TTR_WINDOW words, averaged. That keeps a 300-word text and a 60-word
    one comparable. Shorter than one window falls back to the plain ratio.
    **Higher means more human.**
    """
    toks = words(text)
    if not toks:
        return 0.0
    if len(toks) <= TTR_WINDOW:
        return len(set(toks)) / len(toks)
    ratios = [
        len(set(toks[i:i + TTR_WINDOW])) / TTR_WINDOW
        for i in range(len(toks) - TTR_WINDOW + 1)
    ]
    return statistics.mean(ratios)


def punctuation_density(text: str) -> float:
    """
    How much punctuation, relative to length. ← TODO

    Returns:
        A float. Whether you count all punctuation or only some kinds — commas,
        semicolons, dashes — is a real choice. Semicolons and em dashes are
        more interesting than full stops, because they vary more between
        writers.

    Mine counts only the expressive marks — ; : — – ( ! ? and a spaced
    hyphen used as a dash — per 100 words. Full stops and commas are left
    out: every writer uses them, so they say little. **Higher means more
    human.**
    """
    n = len(words(text))
    if not n:
        return 0.0
    marks = len(EXPRESSIVE_PUNCTUATION.findall(text))
    return 100.0 * marks / n


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.** ← TODO

    Combine your three measures into one number. Same direction as
    `detector.model_signal`, so that `scoring.combine_signals` can treat them
    the same way — if one of your signals runs backwards, everything above it
    is wrong in a way that's hard to see.

    Two things to decide and write down:

      1. Which direction each measure points. Low spread means more AI-ish, so
         it needs flipping. Work out which of your three need that.
      2. How to get each onto a comparable scale. A raw type-token ratio sits
         between 0 and 1; a raw punctuation count doesn't. Adding them
         unscaled means whichever has the bigger numbers wins by default.

    Test it on the four calibration inputs from Milestone 4 — clearly AI,
    clearly human, plain conventional human writing, lightly-edited AI — before
    you trust it. Plain and ordinary, not formal: formal prose reads as *human*
    to signal one, and it is plain writing that gets accused.

    Mine averages three AI-ness readings, each 0–1, each pointing the same way:

      spread     low sentence_length_spread → AI.     CV 0.20 → 1.0, 0.70 → 0.0
      punct      few expressive marks → AI.            0 per 100 words → 1.0,
                                                       2.5 or more → 0.0
      mid-length mean sentence length in the even,     14–22 words → 1.0, falling
                 "most likely" band → AI.              to 0.0 at 9 and at 32

    type_token_ratio is computed but NOT used. On the calibration set it
    pointed the opposite way from the hypothesis (the AI paragraph had the
    *highest* ratio, 0.90; Twain the lowest, 0.71) across a narrow range. I'm
    not putting a direction learned from six texts into the score.

    The mid-length reading is there on purpose: signal one's blind spot is
    short, plain sentences, and this measure does NOT reward them — so the two
    signals stop sharing a blind spot for the plain writer from DESIGN.md §3.
    Its own blind spot: AI told to write short or very long sentences.

    Fewer than two sentences gives no spread to read, so that reading is
    dropped rather than counted as AI.
    """
    readings = []
    if len(sentences(text)) >= 2:
        readings.append(_falling(sentence_length_spread(text), 0.20, 0.70))
    readings.append(_falling(punctuation_density(text), 0.0, 2.5))
    readings.append(_mid_length(text))
    return round(statistics.mean(readings), 4)


def _falling(value: float, ai_at: float, human_at: float) -> float:
    """1.0 at or below `ai_at`, 0.0 at or above `human_at`, linear between."""
    return min(max((human_at - value) / (human_at - ai_at), 0.0), 1.0)


def _mid_length(text: str) -> float:
    """How close the mean sentence length sits to the 14–22 word band."""
    lengths = [len(words(s)) for s in sentences(text)]
    lengths = [n for n in lengths if n]
    if not lengths:
        return 0.0
    mean = statistics.mean(lengths)
    if mean < 14:
        return max((mean - 9) / 5, 0.0)
    if mean > 22:
        return max((32 - mean) / 10, 0.0)
    return 1.0


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
