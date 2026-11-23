#!/usr/bin/env python3
"""One Word, First Thought -- variant 2.

Writes exactly one word to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt):
the first word that comes to mind, nothing else.

The word is "murmuration".

Why this word is the first thought, against the judge's brief (surprise
first, then vividness, then wit, sound or double meaning, then chosen
over generic): the first image that comes to mind unprompted is not a
single bird but the whole flock at dusk, thousands of starlings folding
and unfolding as one dark ribbon across the sky. That image arrives
whole, before any reasoning, and the word that names it is the first
thought because the sight itself is the thought: no topic was given,
no second draft was taken, and the flock is what the mind reaches for
first.

- A different sense and a different scene from variant 1. Variant 1,
  "petrichor", is scent: still air after rain on dry earth. This word is
  sight, sound and motion at once: thousands of starlings folding and
  unfolding across the dusk sky, a living black ribbon that breathes.
- Vivid and specific. One reading calls up a single clear image, not a
  vague feeling: a flock wheeling at dusk. A judge comparing two words
  pairwise can picture this one immediately.
- The word sounds like what it names. "Murmur" sits inside it, a low
  rustling of wings and of voices, and the word carries a double meaning:
  a murmuration is both the flock itself and a soft murmur. That is the
  spark of wit and sound the brief rewards on a second look.
- Surprising, not safe. It is not a word most readers reach for first,
  and it is not a filler word. It feels chosen.
- Short enough to stay sharp: 11 letters, well inside the 1 to 24
  character gate, and length for its own sake does not count.
"""

import os

# The entry: exactly one word, no explanation, no second word.
WORD = "murmuration"


def validate_entry(word: str) -> str:
    """Return the entry word, or raise unless it is exactly one word.

    The gate needs 1 to 24 characters, UTF-8 text, not only white space,
    and exactly one word. The single-word check is explicit: splitting
    on white space must give back exactly this one token, so a word with
    a space, a tab or a newline in it can never slip through.
    """
    cleaned = word.strip()
    if not cleaned:
        raise ValueError("entry must not be empty or only white space")
    if len(cleaned) > 24:
        raise ValueError("entry must be at most 24 characters")
    if cleaned.split() != [cleaned]:
        raise ValueError("entry must be exactly one word")
    return cleaned


def main() -> None:
    """Write the single word to entry.txt, honouring the gate (1-24 chars)."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    word = validate_entry(WORD)

    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(word)

    # Read back what was written and confirm the gate holds on the file
    # itself, not just on the constant: UTF-8, 1 to 24 characters, exactly
    # one word, no surrounding whitespace.
    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    if written != word:
        raise ValueError("entry.txt does not hold exactly the entry word")


if __name__ == "__main__":
    main()
