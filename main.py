from stats import get_num_words
from stats import get_characters
from stats import sort_dict
import sys

def get_book_text():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        with open(sys.argv[1]) as f:
            return f.read()

def main():
    get_num_words(get_book_text())
    get_characters(get_book_text())
    sort_dict(get_characters(get_book_text()))

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(get_book_text())} total words")
    print("--------- Character Count -------")
    for x in sort_dict(get_characters(get_book_text())):
        print(f"{x['char']}: {x['num']}")

    print("============= END ===============")

main()