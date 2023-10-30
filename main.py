def main():
    letter_count = {}
    book_path = "books/frankenstein.txt"


    with open(book_path) as f:
        content = f.read()

    words = content.split()

    for char in content:
        if char.lower().isalpha():
            letter_count[char.lower()] = 1 + letter_count.get(char.lower(), 0)


    print(f"--- Begin report of {book_path} ---")
    print(f"{len(words)} words found in the document")
    print("")
    for key, value in sorted(letter_count.items(), key=lambda x: x[1], reverse=True):
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")

if __name__ == "__main__":
    main()