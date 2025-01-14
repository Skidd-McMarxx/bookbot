def bookreport(book_path:str):
    with open(book_path) as f:
        file_contents = f.read()

        print(file_contents)


if __name__ == "__main__":
    bookreport("books/frankenstein.txt")

