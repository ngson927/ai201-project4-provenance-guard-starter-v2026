#!/usr/bin/env python3
"""
Run both signals, and the combined score, over a fixed set of inputs.

    python calibrate.py            # the table
    python calibrate.py --raw      # plus the three raw style measures

The four the brief asks for (clearly AI, clearly human, formal human,
lightly-edited AI) plus plain human writing, which is the false positive from
DESIGN.md §3. Rerun this after changing anything in config.py, stylometry.py
or scoring.py — it's how you see what a change did before the attack set does.

⚠️ "plain human" and "ornate human" were written as stand-ins. Real
calibration needs writing a person actually produced; swap your own in.
"""

import sys

import detector
import scoring
import stylometry

CLEARLY_AI = (
    "Artificial intelligence has transformed numerous industries in recent "
    "years, offering significant benefits in terms of efficiency, accuracy, "
    "and scalability. However, it is important to consider the ethical "
    "implications of these technologies. Organizations must ensure that their "
    "AI systems are transparent, fair, and accountable. Additionally, they "
    "should invest in training programs that help employees adapt to new "
    "workflows. By taking a thoughtful and balanced approach, businesses can "
    "harness the power of AI while minimizing potential risks. Ultimately, "
    "the successful integration of AI depends on collaboration between "
    "technical experts, policymakers, and the broader community."
)

# The same text after a quick human pass: contractions, one sentence cut
# short, one aside, two words swapped. The kind of edit that takes a minute.
LIGHTLY_EDITED_AI = (
    "AI has changed a lot of industries in recent years, and the gains in "
    "efficiency, accuracy and scale are real. But we can't ignore the ethics. "
    "Organizations have to make sure their systems are transparent, fair, and "
    "accountable — not just say so. They should also invest in training that "
    "helps staff adapt to new workflows. Taken carefully, businesses can use "
    "AI while keeping the risks down. In the end it comes down to "
    "collaboration between engineers, policymakers, and everyone else."
)

# Mark Twain, Adventures of Huckleberry Finn (1884), ch. 1. Public domain.
CLEARLY_HUMAN = (
    "You don't know about me without you have read a book by the name of The "
    "Adventures of Tom Sawyer; but that ain't no matter. That book was made "
    "by Mr. Mark Twain, and he told the truth, mainly. There was things which "
    "he stretched, but mainly he told the truth. That is nothing. I never "
    "seen anybody but lied one time or another, without it was Aunt Polly, "
    "or the widow, or maybe Mary. Aunt Polly—Tom's Aunt Polly, she is—and "
    "Mary, and the Widow Douglas is all told about in that book, which is "
    "mostly a true book, with some stretchers, as I said before."
)

# John Stuart Mill, On Liberty (1859), ch. 1. Public domain.
FORMAL_HUMAN = (
    "The object of this Essay is to assert one very simple principle, as "
    "entitled to govern absolutely the dealings of society with the "
    "individual in the way of compulsion and control, whether the means used "
    "be physical force in the form of legal penalties, or the moral coercion "
    "of public opinion. That principle is, that the sole end for which "
    "mankind are warranted, individually or collectively, in interfering "
    "with the liberty of action of any of their number, is self-protection. "
    "That the only purpose for which power can be rightfully exercised over "
    "any member of a civilized community, against his will, is to prevent "
    "harm to others. His own good, either physical or moral, is not a "
    "sufficient warrant."
)

PLAIN_HUMAN = (
    "I moved to this city two years ago for my job. At first it was very "
    "hard because I did not know anyone. I worked every day and I went home "
    "every night. Then I started to go to a running club on Saturday. Now I "
    "have some good friends there. We run in the park and after we drink "
    "coffee together. I think it is important to try new things when you are "
    "lonely. It is not easy but it is worth it."
)

ORNATE_HUMAN = (
    "My grandmother kept her buttons in a Danish cookie tin, the blue one, "
    "and whenever it rained we'd tip them out across the kitchen lino and "
    "sort them by some rule she invented on the spot — sometimes colour, "
    "sometimes 'ones that look like they've been on a coat in Belgium'. I "
    "never found out what that meant. The tin's on my shelf now. Still "
    "smells faintly of butter, or maybe I imagine that."
)

# AI prose prompted to vary its rhythm: fragments, a question, a dash. Aimed
# at the style signal's blind spot, so the two signals should split here.
VARIED_AI = (
    "Remote work is here to stay. Numerous studies have consistently shown "
    "that employees value flexibility, and as a result many organizations "
    "have embraced hybrid models that combine the benefits of both in-office "
    "and remote collaboration. Productivity? Often higher. However, it is "
    "important to note that company culture can suffer without intentional "
    "effort — regular check-ins, clear communication, and shared goals are "
    "essential. Ultimately, success depends on balance."
)

INPUTS = [
    ("clearly AI", CLEARLY_AI),
    ("lightly-edited AI", LIGHTLY_EDITED_AI),
    ("AI, varied rhythm", VARIED_AI),
    ("clearly human (Twain)", CLEARLY_HUMAN),
    ("formal human (Mill)", FORMAL_HUMAN),
    ("plain human", PLAIN_HUMAN),
    ("ornate human", ORNATE_HUMAN),
]


def main():
    raw = "--raw" in sys.argv
    head = f"{'input':<24}{'model':>8}{'style':>8}{'combined':>10}  label"
    if raw:
        head += f"   {'spread':>7}{'mattr':>7}{'punct':>7}"
    print(head)
    print("-" * len(head))
    for name, text in INPUTS:
        m = detector.model_signal(text)
        s = stylometry.style_signal(text)
        c = scoring.combine_signals(m, s)
        guess, _ = scoring.score_to_label(c)
        row = f"{name:<24}{m:>8.3f}{s:>8.3f}{c:>10.3f}  {guess}"
        if raw:
            row += (f"   {stylometry.sentence_length_spread(text):>7.3f}"
                    f"{stylometry.type_token_ratio(text):>7.3f}"
                    f"{stylometry.punctuation_density(text):>7.2f}")
        print(row)


if __name__ == "__main__":
    main()
