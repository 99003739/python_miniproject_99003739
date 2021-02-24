# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re


def keyword_search(keyword_given, file_text):
    counting = 0
    match = re.findall(keyword_given, file_text, re.M | re.I)
    extension = ".txt"
    file_name = str(keyword_given)+extension
    file_creation = open(file_name, "w+")
    file_creation.write("The number of occurrences of keyword is:" + str(len(match)))
    file_creation.write(str("\n"))
    split_file_text = file_text.split()

    f = open(file_name, "a+")
    for iteration in range(len(split_file_text)):
        matching = re.match(keyword_given, split_file_text[iteration], re.M | re.I)
        if matching:
            counting += 1
            y = (split_file_text[iteration-1]+" "+split_file_text[iteration]+" "+split_file_text[iteration+1]+"\n")
            f.writelines(str(y))


if __name__ == '__main__':

    with open('input_file.txt') as input_file:
        read_file = input_file.read()
        print(read_file)
    for x in range(5):
        keyword = input("Enter the keyword you wanted to search in file:")
        keyword_search(keyword, read_file)
