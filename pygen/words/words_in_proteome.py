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

def read_sequences(file_path):
    """
    Read protein sequences from a FASTA file and return a dictionary with
    protein identifiers as keys and their associated sequences as values.

    Args:
    - file_path (str): The path to the FASTA file containing protein sequences.

    Returns:
    - dict: A dictionary with protein identifiers as keys and sequences as values.
    """
    sequences = {}
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            current_identifier = None
            current_sequence = []

            for line in lines:
                line = line.strip()
                if line.startswith('>'):
                    if current_identifier is not None:
                        sequences[current_identifier] = ''.join(current_sequence)
                    current_identifier = line[4:10]
                    current_sequence = []
                else:
                    current_sequence.append(line)

            if current_identifier is not None:
                sequences[current_identifier] = ''.join(current_sequence)

        return sequences
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

if __name__ == "__main__":
    # Specify the directory to search for files
    search_directory = "C:/Users/teren/Desktop/softdev_project"

    # Find the words file
    words_file_path = find_file(search_directory, "english-common-words.txt")
    if words_file_path is None:
        print("Error: 'english-common-words.txt' not found.")
    else:
        print(f"Found 'english-common-words.txt' at: {words_file_path}")
    
    # Find the proteome file
    proteome_file_path = find_file(search_directory, "human-proteome.fasta")
    if proteome_file_path is None:
        print("Error: 'human-proteome.fasta' not found.")
    else:
        print(f"Found 'human-proteome.fasta' at: {proteome_file_path}")
    
   
    def search_words_in_proteome(words, sequences):
   
        word_counts = {}
        for word in words:
            count = 0
            for sequence in sequences.values():
                if word in sequence:
                    count += 1
            word_counts[word] = count
            if count > 0:
                print(f"{word} found in {count} sequences")

        return word_counts
    
def find_most_frequent_word(word_counts, total_sequences):
    """
    Find the word found in the most sequences and display related information.

    Args:
    - word_counts (dict): A dictionary with words as keys and the number of sequences containing these words as values.
    - total_sequences (int): The total number of protein sequences in the proteome.

    Returns:
    - None
    """
    most_frequent_word = max(word_counts, key=word_counts.get)
    count = word_counts[most_frequent_word]

    print(f"\nMost Frequent Word:")
    print(f"=> {most_frequent_word} found in {count} sequences")
    print(f"=> Percentage of proteome sequences: {count / total_sequences * 100:.2f}%")

if __name__ == "__main__":
    # You can specify the file paths when running the script
    words_file_path = "english-common-words.txt"
    proteome_file_path = "human-proteome.fasta"


    if words_file_path :
        # Read words
        words_result = read_words(words_file_path)

        if words_result:
            print("\nWords in uppercase with 3 or more characters:")
            print(words_result)
            print(f"Number of selected words: {len(words_result)}")
        else:
            print("No words selected.")##

        # Read protein sequences
    sequences_result = read_sequences(proteome_file_path)

    if sequences_result:
        print("\nProtein Sequences:")
        for identifier, sequence in sequences_result.items():
            print(f"{identifier}: {sequence[:50]}...")  # Print the first 50 characters of each sequence
        print(f"Number of protein sequences: {len(sequences_result)}")
    else:
        print("No protein sequences found.")

 # Search words in the proteome
    if words_result and sequences_result:
        word_counts_result = search_words_in_proteome(words_result, sequences_result)
        print("\nWord Counts in the Proteome:")
        print(word_counts_result)
    else:
        print("No words or protein sequences available for search.")

# Find the most frequent word and display information
    find_most_frequent_word(word_counts_result, len(sequences_result))
else:
    print("No words or protein sequences available for search.")