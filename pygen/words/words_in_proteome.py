# words_in_proteome.py

import os

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
    # Specify the folder where the file is located
    folder_path = "C:/Users/Skydr/OneDrive/Documents/M1 IDIL ECO EVO/software development/project files txt/"

    # Construct the full file path
    file_name = "english-common-words.txt"
    file_path = os.path.join(folder_path, file_name)

    result = read_words(file_path)

    if result:
        print("Words in uppercase with 3 or more characters:")
        print(result)
        print(f"Number of selected words: {len(result)}")
    else:
        print("No words selected.")
