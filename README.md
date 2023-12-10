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

# Example usage:
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
 