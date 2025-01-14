def bookreport(book_path:str):
    with open(book_path) as f:
        file_contents = f.read()

        print(count_words(file_contents))


def count_words(s:str) -> int:
    return len(s.split())


if __name__ == "__main__":
    bookreport("books/frankenstein.txt")

