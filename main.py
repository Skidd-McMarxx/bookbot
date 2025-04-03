import sys

from stats import get_word_count, get_char_count, sort_char_count


def bookreport(book_path:str):
    with open(book_path) as f:
        file_contents = f.read()

        print_report(book_path, file_contents)


def print_report(book_path:str, s:str):
    print(f"--- Begin report of {book_path} ---")
    print(f"{get_word_count(s)} words found in the document\n")
    char_count = get_char_count(s)
    sorted_char_count = sort_char_count(char_count)
    for character in sorted_char_count:
        char, num = character["char"], character["num"]
        if not char.isalpha():
            continue
        print(f"{char}: {num}")
    print("--- End report ---")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bookreport(sys.argv[1])