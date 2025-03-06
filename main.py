import sys
from stats import get_num_words, get_char_count, sort_char_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    try:
        with open(book_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: The file {book_path} was not found.")
        sys.exit(1)

    num_words = get_num_words(text)
    char_count = get_char_count(text)
    sorted_char_list = sort_char_count(char_count)

    print(f"Number of words: {num_words}")
    print("Character counts (sorted):")
    for item in sorted_char_list:
        print(f"{item['character']}: {item['count']}")

if __name__ == "__main__":
    main()
