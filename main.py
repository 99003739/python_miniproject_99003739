# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re
def keyword_search (word, file_text) :
    #count = file_text.count(word)
    match = re.findall(word, file_text, re.M | re.I)
    extension = ".txt"
    file_name = str(word)+extension
    file_creation = open(file_name, "w+")
    file_creation.write("The number of occurrences of keyword is:" + str(len(match)))
    #match = re.findall(word, file_text, re.M | re.I)
    print(len(match))
    print(match)

    return 0





if __name__ == '__main__':

    with open('input_file.txt') as input_file:
        read_file = input_file.read()
        print(read_file)

    keyword = input("Enter the keyword you wanted to search in file:")
    keyword_search(keyword, read_file)





''' import re

    with open('inpu.txt') as searchfile:
        text = searchfile.read()
        for m in re.finditer('(?:^|\s+\S+) software?(?:\s*\s+\S+|$)', text,  re.IGNORECASE):
            print(m)'''
