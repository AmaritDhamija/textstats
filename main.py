import re
from collections import Counter
from io_ops import read_txt_file, output_terminal, output_txt, write_lines
from text_stats import character_counts, total_letters, word_extraction

"""
Entry point (orchestration only).

TODO (team):
- Prompt for input file path (interactive) — keep logic minimal.
- Call functions from text_stats.py to compute results.
- Print six output lines in exact format.
- Prompt for output file, confirm overwrite, write lines via io_ops.py.
- Ensure this file stays "thin" — no heavy logic here.
"""

# from io_ops import ...   # TODO: import the small set of I/O helpers you create
# from text_stats import ...  # TODO: import your pure functions

def main() -> None:
    # TODO: glue together a simple flow:
    # 1) get input path (prompt)
    # 2) read text (io_ops)
    # 3) compute metrics (text_stats)
    # 4) print to console
    # 5) write to output file (io_ops)
    # Assignment 1 – Text Stats Project (deliberately NO functions / NO try/except)
# Reads input.txt, prints results, and writes them to output.txt in the exact format.

    text_content = read_txt_file()

    
    characters_with_spaces, characters_no_spaces, char_index = character_counts(text_content)

    word_list = word_extraction(text_content)



    # --- Word statistics ---
    word_count = len(word_list)
    unique_word_count = len(set(word_list))


    # total letters across all words
    total_letter_count = total_letters(word_list)


    # average word length with one decimal; 0.0 if there are no words
    average_word_length = (total_letter_count / word_count) if word_count != 0 else 0.0
    average_word_length_str = f"{average_word_length:.1f}"

    # --- Most common word(s) and frequency ---
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


    output_lines = write_lines(word_count, unique_word_count, characters_with_spaces, characters_no_spaces, average_word_length_str, most_common_line)

    output_terminal(output_lines)

    output_txt(output_lines)



if __name__ == "__main__":
    main()


