def main():
    # Path to the file
    path_to_file = "/home/vaashcrome/workspace/github.com/DimWhit/bookbot/books/frankenstein.txt"
    
    # Open the file and read its contents
    with open(path_to_file, 'r') as file:
        file_contents = file.read()
    
    # Count the words in the text
    word_count = count_words(file_contents)
    print(f"The book contains {word_count} words.")
    
    # Count the frequency of each character in the text
    character_frequencies = count_character_frequencies(file_contents)
    print("\nCharacter frequencies:")
    for char, freq in sorted(character_frequencies.items()):
        print(f"{repr(char)}: {freq}")

def count_words(text):
    """
    Count the number of words in a string.

    :param text: str - The input text
    :return: int - The number of words in the text
    """
    # Split the text into words using whitespace and count them
    words = text.split()
    return len(words)

def count_character_frequencies(text):
    """
    Count the frequency of each character in a string.

    :param text: str - The input text
    :return: dict - A dictionary with characters as keys and their frequencies as values
    """
    # Convert all characters to lowercase
    text = text.lower()
    
    # Initialize a dictionary to hold character counts
    character_counts = {}
    
    # Iterate over each character in the text
    for char in text:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    
    return character_counts

if __name__ == "__main__":
    main()
