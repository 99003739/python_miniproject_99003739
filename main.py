"""
Author: Prateek Chauhan
PS NO.- 99003739
Mail- prateek.chauhan@ltts.com

Program Steps:
1. The program is reading the input file.
2. user will be asked for the keyword, user wants bto search.
3. The keyword will be searched then a file will be created
   with the name of the keyword.
4. The newly created file will have the count of number of times keyword
   appeared and the lines with previous word and the next word with the keyword
5. The process will be repeated 5 times and the user will obtain 5 files at the
   end of program.
"""
import re
# regular expression imported


# Class SearchWord created
class SearchWord:

    # constructor defined
    def __init__(self, keyword_given, file_text):
        self.keyword_given = keyword_given
        self.file_text = file_text

    # Keyword_Search method defined
    def keyword_search(self):

        match = re.findall(self.keyword_given, self.file_text, re.M | re.I)
        # Finding the keyword in the  input file
        extension = ".txt"
        file_name = str(self.keyword_given)+extension
        # .txt extension added to file name
        file_creation = open(file_name, "w+")  # file created in writing mode
        file_creation.write("The number of occurrences of keyword is:" + str(len(match)))
        # writing count to file
        file_creation.write(str("\n\n"))
        # two times line changed in the file
        split_file_text = self.file_text.split()
        # input file is getting split and given file handler split_file_text
        file_append = open(file_name, "a+")
        # created file is opened in append mode
        for cycle in range(len(split_file_text)):
            # iterating for range of number of lines in given file
            matching = re.match(self.keyword_given, split_file_text[cycle], re.M | re.I)
            # matching keyword in file
            if matching:
                # if keyword got matched saving the three words in tuple
                three_word = (split_file_text[cycle-1]+" "+split_file_text[cycle]+" "+split_file_text[cycle+1]+"\n")
                file_append.writelines(str(three_word))
                # appending the file with tuple generated


if __name__ == '__main__':

    with open('input_file.txt') as input_file:  # opening the input_file.txt
        read_file = input_file.read()  # giving file handler to the file
    for x in range(5):
        keyword = input("Enter the keyword you wanted to search in file:")
        # asking user to enter keyword to search
        d = SearchWord(keyword, read_file)
        d.keyword_search()
