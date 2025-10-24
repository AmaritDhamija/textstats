import re
from collections import Counter
from io_ops import read_txt_file, output_terminal, output_txt, write_lines, input_filename
from text_stats import character_counts, total_letters, word_extraction, word_statistics, avg_word_length, most_common_words

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
    file_name = input_filename()

    text_content = read_txt_file(file_name)

    characters_with_spaces, characters_no_spaces, char_index = character_counts(text_content)

    word_list = word_extraction(text_content)

    # --- Word statistics ---
    word_count, unique_word_count = word_statistics(word_list)

    
    total_letter_count = total_letters(word_list)

    average_word_length_str = avg_word_length(total_letter_count, word_count)

    most_common_line = most_common_words(word_count, word_list)

    output_lines = write_lines(word_count, unique_word_count, characters_with_spaces, characters_no_spaces, average_word_length_str, most_common_line)

    output_terminal(output_lines)

    output_txt(output_lines)



if __name__ == "__main__":
    main()


