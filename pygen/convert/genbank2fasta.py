import os

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            print(f"Number of lines read: {len(lines)}")
            return lines
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []

# Define the file path
directory = "C:/Users/India ELLIOTT/Documents/SPIDIL"
file_name = "NC_001133.gbk"
file_path = os.path.join(directory, file_name)

# Call the read_file() function
file_content = read_file(file_path)

# You can now use the 'file_content' list for further processing
# For example, printing the first 10 lines:

##print("First 10 lines:")
##for line in file_content[:10]:
##    print(line.strip())

## Here it will print all the lines of the file:
print("All the lines")
for line in file_content:
    print(line.strip())