def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_counts = {}
    for char in text:
        lowercase_char = char.lower()
        if lowercase_char in char_counts:
            char_counts[lowercase_char] +=1
        else:
            char_counts[lowercase_char] = 1
    return char_counts

def sort_text(dict):
    return dict["total"]

def chars_to_sorted_list(char_counts):
    result = []  # Create a list to hold our dictionaries
    for char, count in char_counts.items(): # Loop through each character and its count in the char_counts dictionary
        char_dict = {"letters": char, "total": count}  # Create a dictionary for this character with "letters" and "total" keys
        result.append(char_dict)  # Add this dictionary to our result list
    result.sort(reverse=True, key=sort_text)
    return result