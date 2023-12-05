# words_in_proteome.py

import os

def find_file(directory, file_name):
    """
    Find a file in the specified directory.

    Args:
    - directory (str): The directory to search in.
    - file_name (str): The name of the file to find.

    Returns:
    - str: The full path to the found file, or None if not found.
    """
    for root, dirs, files in os.walk(directory):
        if file_name in files:
            return os.path.join(root, file_name)
    return None

def read_words(file_path):
    """
    Read words from a file, convert them to uppercase, and filter words
    with less than 3 characters.

    Args:
    - file_path (str): The path to the file containing words.

    Returns:
    - list: A list of uppercase words with 3 or more characters.
    """
    try:
        with open(file_path, 'r') as file:
            words = [word.strip().upper() for word in file.readlines() if len(word.strip()) >= 3]
        return words
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

if __name__ == "__main__":
    # Specify the directory to search for files
    search_directory = "C:/Users/Skydr/OneDrive/Documents/M1 IDIL ECO EVO/software development/project files txt/"

    # Find the words file
    words_file_path = find_file(search_directory, "english-common-words.txt")
    if words_file_path is None:
        print("Error: 'english-common-words.txt' not found.")
    else:
        print(f"Found 'english-common-words.txt' at: {words_file_path}")

    # Continue with the rest of your script using the found file paths
    # ...

    if words_file_path :
        # Read words
        words_result = read_words(words_file_path)

        if words_result:
            print("\nWords in uppercase with 3 or more characters:")
            print(words_result)
            print(f"Number of selected words: {len(words_result)}")
        else:
            print("No words selected.")

#PROTEINS (india)

def read_sequence(file_path):
    pass


#SEARCHING FOR WORDS
def search_words_in_proteome(words, protein_sequences):
    """
    This functions finds words (from the list of words created by the read_words function) inside of the protein 
    sequences.

    Args:
    - file_path (str): The path to the file containing words.

    Returns:
    - list: A list of uppercase words found in the protein sequences and in how many sequences they appear in.
    """
    word_counts = {}
    for word in words:
        count = 0
        for sequence in protein_sequences.values():
            if word in sequence:
                count += 1
        word_counts[word] = count
        print(f"{word} found in {count} sequences")
    return word_counts
words = read_words("pygen\words\english-common-words.txt")
protein_sequences = read_sequence('human-proteome.fasta')
word_counts = search_words_in_proteome(words, protein_sequences)
print(word_counts)