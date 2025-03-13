from stats import get_book_text, word_count, count_chars, sort_text, chars_to_sorted_list
import sys
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count_result = word_count(book_text)
    char_counts = count_chars(book_text)

    # Get the sorted list of character dictionaries
    sorted_chars = chars_to_sorted_list(char_counts)

    # Now print the report according to the format in the assignment
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count_result} total words")
    print("--------- Character Count -------")

    # Print each character and its count
    for char_dict in sorted_chars:
        char = char_dict["letters"]
        count = char_dict["total"]
        # Only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")
main()