"""
Pure text-processing functions (no I/O or exceptions).

Responsibilities:
- Tokenize words (A–Z only, case-insensitive).
- Count characters (with and without spaces).
- Compute: word count, unique words, average word length (one decimal).
- Determine most common word(s) and frequency; alphabetical order for ties.
- Format the six output lines in the exact required text format.

Rules:
- No input(), no print(), no file I/O, no try/except here.
- Keep functions small, composable, and testable.
"""

# Hints (do not implement here yet):
# - Consider a constant regex pattern for words.
# - Separate calculation from formatting.
# - Return data structures that are easy to test.
import re
from collections import Counter

    # --- Character counts ---
def character_counts(text_content):
    characters_with_spaces = len(text_content)
    characters_no_spaces = 0
    char_index = 0
    while char_index < len(text_content):
        current_char = text_content[char_index]
        if not current_char.isspace():
            characters_no_spaces += 1
        char_index += 1

    return characters_with_spaces, characters_no_spaces, char_index

def word_extraction(text_content):
    lowered_text = text_content.lower()
    word_list = re.findall(r"[a-zA-Z]+", lowered_text)

    return word_list

def total_letters(word_list):
    total_letter_count = 0
    word_index = 0
    while word_index < len(word_list):
        total_letter_count += len(word_list[word_index])
        word_index += 1

    return total_letter_count

