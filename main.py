def bookreport(book_path:str):
    with open(book_path) as f:
        file_contents = f.read()

        print(count_words(file_contents))
        print(count_characters(file_contents))


def count_words(s:str) -> int:
    return len(s.split())


def count_characters(s:str):
    char_count = {}
    for char in s.lower():
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    return char_count


if __name__ == "__main__":
    bookreport("books/frankenstein.txt")

