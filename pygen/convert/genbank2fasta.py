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

def find_genes(file_content):
    genes = []

    for line in file_content:
        if line.startswith('     gene            '):  # Check if the line indicates a gene
            is_antisense = 'complement' in line  # Check if it's an antisense gene
            line = line.replace('     gene            ', '')  # Remove unnecessary prefix
            line = line.replace('<', '').replace('>', '')  # Remove < and > symbols

            # Extract the start and end positions
            positions = [int(pos.strip()) for pos in line.replace('complement(', '').replace(')', '').split('..')]

            if len(positions) == 1:
                start = end = positions[0]
            else:
                start, end = positions

            if is_antisense:
                genes.append([start, end, 'antisense'])
            else:
                genes.append([start, end, 'sense'])

    return genes

# Define the file path
directory = "C:/Users/teren/Desktop/softdev_project"
file_name = "NC_001133.gbk"
file_path = os.path.join(directory, file_name)

# Call the read_file() function
file_content = read_file(file_path)

# Call the extract_organism() function
organism_name = extract_organism(file_content)

# Call the find_genes() function
genes = find_genes(file_content)

## Here it will print all the lines of the file:
print("All the lines")
for line in file_content:
    print(line.strip())

# Print the organism name
print(f"Organism name: {organism_name}")

# Print information about each gene
print("Information about each gene:")
for gene in genes:
    print(f"Start: {gene[0]}, End: {gene[1]}, Type: {gene[2]}")

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
