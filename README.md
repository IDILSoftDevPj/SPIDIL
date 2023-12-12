# SPIDIL
This repository is a group project for the IDIL Ecology & Evolution masters degree software development unit : *https://bcharlier.github.io/HAB796B9/
## Code used to download the files used by the script

import os
import requests

def download_file(url, destination, filename):
    os.makedirs(destination, exist_ok=True)

    response = requests.get(url)
    if response.status_code == 200:
        full_path = os.path.join(destination, filename)
        with open(full_path, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded successfully to {full_path}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

Example usage:

url1 = "https://python.sdv.univ-paris-diderot.fr/data-files/english-common-words.txt"

url2 = "https://python.sdv.univ-paris-diderot.fr/data-files/human-proteome.fasta"

url3 = "https://python.sdv.univ-paris-diderot.fr/data-files/NC_001133.gbk"

download_directory = "C:/Users/Skydr/OneDrive/Documents/M1 IDIL ECO EVO/software development/project files txt/"

filename1 = "english-common-words.txt"

filename2 = "human-proteome.fasta"

filename3 = "NC_001133.gbk"

download_file(url1, download_directory, filename1)

download_file(url2, download_directory, filename2)

download_file(url3, download_directory, filename3)

# Aims of our project 

Analyzing the occurrence of common English words in a human proteome dataset and identify the most frequently occurring word

Extracting details about genes from a GenBank file, manipulating DNA sequences, and writing a fasta file

# Functions used in each file

## 1) Words in proteom functions:

### function read_file(file_path) 
reads the content of a file and counts the number of lines
### function read_words(file_path) and read_sequences(file_path) 
reading words from a file + reading protein sequences from a FASTA file
### function search_words_in_proteome(words, sequences) 
count how many times each word appears in the protein sequences
### function find_most_frequent_word(word_counts, total_sequences) 
finding the most frequent word + displaying related information
## 2) Genbank2fasta functions:

### function read_file(file_path) 
reads the content of a file and counts the number of lines
### function regular expression to extract the organism name from the GenBank file: 
#### function find_genes(file_content) 
extracts information about genes from the GenBank file
#### functions read_file(), extract_organism() + find_genes() 
obtain file content, organism name, and gene information
#### function write_fasta(file_name, comment, sequence) 
write a FASTA file with a given file name, comment, and DNA sequence

# Issues and Challenges solutions:

## Cloning:
git clone “https link”

## Name mislabeling:
git config --global --replace-all user.name "your name"
git config --global --replace-all user.email "your git email” 

## Access rights problems:
creating an organisation and placing every member as admin 

## Conflits: 
adjusting the code

## Mistakes in the code :
check code regularly

## Understanding python language, vscode and github :
reading and learning
One branch = one function NOT one branch = one person
Pip install to install packages

## Connection timeout error :
check internet network
 
