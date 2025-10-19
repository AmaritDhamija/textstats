"""
User interaction & file I/O. Implement guards (validation) + try/except here.

Guidance:
- Prompt for input filename (reject empty; re-prompt).
- Read text with UTF-8; handle FileNotFoundError, PermissionError, UnicodeDecodeError.
- Prompt for output filename (default to 'output.txt').
- If output exists, confirm overwrite (y/n; re-prompt on invalid).
- Write lines; handle PermissionError/OSError.
- Never crash on user mistakes; re-prompt or exit gracefully with a helpful message.

Note:
- Keep function responsibilities small and names descriptive.
- No heavy text-processing logic belongs here.
"""

# TODO: define small helpers such as:
# def prompt_nonempty(prompt_text: str) -> str: ...
# def read_text_file(path: str) -> str: ...
# def confirm_overwrite(path: str) -> bool: ...
# def write_lines(path: str, lines: list[str]) -> bool: ...


# --- Read the raw file text (assumes input.txt exists in the same folder) ---
# Add exception to alleviate assumption of input.txt files existance hw
# 

def input_filename():
    file_name = str(input("Please input file name: "))
    return file_name

def read_txt_file(file_name):     
    with open(file_name, "r", encoding="utf-8") as file_in:
        text_content = file_in.read()
    return text_content

def write_lines(word_count, unique_word_count, characters_with_spaces, characters_no_spaces, average_word_length_str, most_common_line):
    output_lines = [
    f"Word count: {word_count}",
    f"Unique words: {unique_word_count}",
    f"Characters (with spaces): {characters_with_spaces}",
    f"Characters (no spaces): {characters_no_spaces}",
    f"Average word length: {average_word_length_str}",
    most_common_line,
    ]
    return output_lines

def output_terminal(output_lines):
    line_index = 0
    while line_index < len(output_lines):
        print(output_lines[line_index])
        line_index += 1



def output_txt(output_lines):
    with open("output.txt", "w", encoding="utf-8") as file_out:
        line_index = 0
        while line_index < len(output_lines):
            file_out.write(output_lines[line_index] + ("\n" if line_index < len(output_lines) - 1 else ""))
            line_index += 1

