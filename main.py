def bookreport(book_path:str):
    with open(book_path) as f:
        file_contents = f.read()

        print_report(book_path, file_contents)


def count_words(s:str) -> int:
    return len(s.split())


def count_characters(s:str) -> list[dict]:
    char_count = {}
    for char in s.lower():
        if not char.isalpha():
            continue
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    char_count = [{"name":key, "num":val} for key, val in char_count.items()]
    return char_count


def sort_on(dict:dict):
    return dict["num"]


def print_report(book_path:str, s:str):
    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words(s)} words found in the document\n")
    char_count = count_characters(s)
    char_count.sort(reverse=True, key=sort_on)
    for character in char_count:
        char, val = character["name"], character["num"]
        print(f"The '{char}' character was found {val} times")
    print("--- End report ---")

if __name__ == "__main__":
    bookreport("books/frankenstein.txt")

