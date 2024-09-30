import re
import string
string.punctuation
class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names


    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    line1 = line.lower()
                    for p in string.punctuation:
                        if p in line1:
                            line2 = line1.replace(p, '')
                            all_words[self.file_names] = line2
        return all_words






    # def find(self, word):
    #
    #
    # def count(self, word):

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова