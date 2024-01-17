def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_word = count_word(text)
    num_letter = count_letter(text)
    report_letter(num_letter, book_path, num_word)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_word(texte):
    list_word = texte.split()
    return len(list_word)

def count_letter(texte):
    dict_letter = {}
    for letter in texte.lower():
        if letter not in dict_letter:
            dict_letter[letter]  = 1
        else:
            dict_letter[letter] += 1
    return dict_letter

def report_letter(info, path_livre, num_word):
    print(f"--- Begin report of {path_livre} ---")
    print(f"{num_word} words found in the document")
    print(f"")

    for key, value in info.items():
        print(f"The {key} character was found {value} times")
    
    print(f"--- End report ---")
main()