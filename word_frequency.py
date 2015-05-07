import re
import os
import os.path



name = "sample.txt"
path = "/Users/willflowers/Documents/The_Iron_Yard"

# Function to look for sample.txt

def look(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            """Join "two" paths together"""
            return os.path.join(root, name)

"""I originally was going to copy the text into a new text called copied_sample, but I didn't
know if I needed to """

# def copy():
#     location = look(name, path)
#     original_file= open(location, "r")
#     copied_sample = open("copied_sample.txt", "w")
#     for line in original_file:
#         copied_sample.write(line)
#     original_file.close()
#     copied_sample.close()
#     return copied_sample.txt



def word_freq():
    location = look(name, path)
    with open(location, "r") as jane_eyre:
        sample_string=jane_eyre.read().replace('"','').replace('[','').replace(']','').replace('*','').replace(',','').replace('.','').replace('?','').replace('!','').replace('-','').replace('\n',' ').replace(':','').replace(';','').replace('()','').lower()
    #initialize list
    sample_list = []
    #Split words into list and populate
    for word in sample_string.split(' '):
        sample_list.append(word)
    #Create/initialize dictionary
    word_dictionary = {}

    for word in sample_list:
        word_dictionary[word] = word_dictionary.get(word, 0) + 1

    sorted_dict = sorted(word_dictionary.items(), key=lambda x: x[1], reverse=True)

    for i in range(0,20):
        print(sorted_dict[i])

    #Wasn't quite able to make it "pretty" output, but it works

word_freq()


#My functions may be too dependent on each other, not sure
