import re

class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names


    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                for sym in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(sym, '')
                    value = text.split()
                    all_words[name] = value
        return all_words

    def find(self, word):
        places = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                places[key] = value.index(word.lower()) + 1
            else:
                print('Слово не найдено')
        return places


    def count(self, word):
        quantity = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                quantity[key] = value.count(word.lower())
            else:
                print('Слово не найдено')
        return quantity



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего