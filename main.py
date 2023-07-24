#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
from typing import List

# Declare variables
name_path = "./Input/Names/invited_names.txt"
template_path = "./Input/Letters/starting_letter.txt"
output_path = "./Output/ReadyToSend/"
names = []
template = []

# This function will read the file containing all names into a list.
def readNames(file_path):
    with open(file_path, 'r', newline='\n') as file:
        names = file.readlines()
        return names

# This function will clean the list of names.
def cleanNamesList(list):
    for i, v in enumerate(names):
        if "\n" in v:
            v = v.strip()
            list[i] = v
    return list

# This function will perform the mail merge.
def mailMerge(template_path, output_path, name):
    with open(template_path, 'r') as file:
        file = file.readlines()
        with open(output_path, 'w') as output:
            for i, v in enumerate(file):
                if "[name]" in v:
                    v = v.replace("[name]", name)
                    output.write(v)
                else:
                    output.write(v)


# Create list of names
names = readNames(name_path)
names = cleanNamesList(names)

# Call mailMerge method for each name in the names list.
for name in names:
    updated_output_path = output_path+name+".txt"
    mailMerge(template_path, updated_output_path, name)


