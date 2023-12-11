import os
import re

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            print(f"Number of lines read: {len(lines)}")
            return lines
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []

def extract_organism(file_content):
    organism_pattern = re.compile(r'^\s*ORGANISM\s*(.*?)\s*$', re.MULTILINE)
    match = organism_pattern.search("".join(file_content))
    if match:
        return match.group(1)
    else:
        return "Organism name not found."

# Define the file path
directory = "C:/Users/India ELLIOTT/Documents/SPIDIL"
file_name = "NC_001133.gbk"
file_path = os.path.join(directory, file_name)

# Call the read_file() function
file_content = read_file(file_path)

# Call the extract_organism() function
organism_name = extract_organism(file_content)

# You can now use the 'file_content' list for further processing
# For example, printing the first 10 lines:

##print("First 10 lines:")
##for line in file_content[:10]:
##    print(line.strip())

## Here it will print all the lines of the file:
print("All the lines")
for line in file_content:
    print(line.strip())

# Print the organism name
print(f"Organism name: {organism_name}")

# Reverse complementory sequence
def construct_comp_inverse(dna_sequence):
    # Define a dictionary for complementary bases
    comp_dict = {'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}
    
    # Convert the DNA sequence to lowercase
    dna_sequence = dna_sequence.lower()
    
    # Take the complementary sequence
    comp_sequence = ''.join(comp_dict[base] for base in dna_sequence)
    
    # Take the reverse of the complementary sequence
    comp_inverse_sequence = comp_sequence[::-1]
    
    return comp_inverse_sequence

# Test the function with the provided sequences
sequence1 = "atcg"
sequence2 = "AATTCCGG"
sequence3 = "gattaca"

result1 = construct_comp_inverse(sequence1)
result2 = construct_comp_inverse(sequence2)
result3 = construct_comp_inverse(sequence3)

print("Original Sequence 1:", sequence1)
print("Result 1:", result1)

print("\nOriginal Sequence 2:", sequence2)
print("Result 2:", result2)

print("\nOriginal Sequence 3:", sequence3)
print("Result 3:", result3)

#writing a fasta file

def write_fasta(file_name, comment, sequence):
    # Open the file in write mode
    with open(file_name, 'w') as fasta_file:
        # Write the comment line
        fasta_file.write(f'>{comment}\n')

        # Write the sequence in lines of 80 characters
        for i in range(0, len(sequence), 80):
            line = sequence[i:i+80]
            fasta_file.write(f'{line}\n')

# Test the function
file_name = 'test.fasta'
comment = 'my comment'
sequence = 'atcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcg'

write_fasta(file_name, comment, sequence)