import io
from pprint import pprint


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for f_names in self.file_names:
            with open(f_names, encoding='utf-8') as file:
                lower_read = file.read().lower()
                for symbol in ['.', '=', '!', '?', ';', ':', ' - ']:
                    lower_read = lower_read.replace(symbol, '')
                words_str = lower_read.split()
            all_words[f_names] = words_str
        return all_words

    def find(self, word):
        word_find = {}
        word = word.lower()
        for f_name, words in self.get_all_words().items():
            if word in words:
                word_find[f_name] = words.index(word) + 1
        return word_find

    def count(self, word):
        count_word = {}
        word = word.lower()
        for f_name, words in self.get_all_words().items():
            if word in words:
                count_word[f_name] = words.count(word)
        return count_word


finder1 = WordsFinder('test.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
