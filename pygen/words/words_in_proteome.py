# words_in_proteome.py

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
    # You can specify the file paths when running the script
    words_file_path = "C:/Users/Skydr/OneDrive/Documents/M1 IDIL ECO EVO/software development/project_root_dir/pygen/words/english-common-words.txt"

    # Read words
    words_result = read_words(words_file_path)

    if words_result:
        print("Words in uppercase with 3 or more characters:")
        print(words_result)
        print(f"Number of selected words: {len(words_result)}")
    else:
        print("No words selected.")
