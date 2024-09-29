class WordsFinder:
    file_names = []


    def __init__(self, *names):
        #self.name = name

        for file in names:
            self.file_names.append(file)

    def get_all_words(self):


finder2 = WordsFinder('test_file.txt')
print(finder2.file_names)