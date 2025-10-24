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

    # --- Word extraction: letters only (A–Z/a–z), case-insensitive for counting/uniqueness ---
import re
def word_extraction(text_content):
    lowered_text = text_content.lower()
    word_list = re.findall(r"[a-zA-Z]+", lowered_text)
    return word_list

def word_statistics(word_list):
    word_count = len(word_list)
    unique_word_count = len(set(word_list))
    return word_count, unique_word_count


def total_letters(word_list):
    total_letter_count = 0
    word_index = 0
    while word_index < len(word_list):
        total_letter_count += len(word_list[word_index])
        word_index += 1

    return total_letter_count

def avg_word_length(total_letter_count, word_count):
    average_word_length = (total_letter_count / word_count) if word_count != 0 else 0.0
    average_word_length_str = f"{average_word_length:.1f}"

    return average_word_length_str

def most_common_words(word_count, word_list):
    if word_count == 0:
        most_common_line = "Most common word(s): (0)"
    else:
        word_counts = Counter(word_list)
        highest_frequency = 0
        for word in word_counts:
            if word_counts[word] > highest_frequency:
                highest_frequency = word_counts[word]
        most_frequent_words = []
        for word in word_counts:
            if word_counts[word] == highest_frequency:
                most_frequent_words.append(word)
        most_frequent_words.sort()
        if len(most_frequent_words) == 1:
            most_common_line = f"Most common word(s): {most_frequent_words[0]} ({highest_frequency})"
        else:
            most_common_line = f"Most common word(s): {', '.join(most_frequent_words)} ({highest_frequency})"
    
    return most_common_line
