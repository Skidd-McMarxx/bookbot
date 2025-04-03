def get_word_count(s:str) -> int:
    return len(s.split())


def get_char_count(s:str) -> list[dict]:
    char_count = {}
    for c in s:
        char = c.lower()
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    # char_count = [{"name":key, "num":val} for key, val in char_count.items()]
    return char_count


def sort_on(dict:dict):
    return dict["num"]


def sort_char_count(char_count:dict) -> list[dict]:
    sorted_chars = []
    for char in char_count:
        sorted_chars.append({"char":char, "num":char_count[char]})
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars