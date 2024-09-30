import re

class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names


    def get_all_words(self):
        all_words = {}
        for file_name in self.file.names:
            with open(file_names, 'r', encoding='utf-8') as file:
                for line in file:
                    line1 = line.lower()
                    import string
                    string.punctuation
                    for p in string.punctuation:
                        if p in line1:
                            line2 = line1.replace(p, '')




    # def find(self, word):
    #
    #
    # def count(self, word):

finder2 = WordsFinder('test_file.txt')
print(finder2.file_names)