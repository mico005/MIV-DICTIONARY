from PyDictionary import PyDictionary
import difflib
import json

dict = PyDictionary()

english_json = "./words.json"
mivetran_json = "./mivetra_lang.json"

with open(english_json, 'r') as file:
    eng_data = json.load(file)

with open(mivetran_json, 'r') as file:
    miv_data = json.load(file)

all_data = eng_data + miv_data


def translate(word):
    word = word.lower()

    if word in eng_data:
        index = eng_data.index(word)
        return miv_data[index]
    elif word in miv_data:
        index = miv_data.index(word)
        return eng_data[index]
    else:
        return difflib.get_close_matches(word, all_data, n=5, cutoff=0.8)


class meanings:
    def __init__(self, word):
        self.word = word.lower()

        if self.word not in eng_data:
            index = miv_data.index(self.word)
            self.word = eng_data[index]

        self.meaning = dict.meaning(self.word)

    def Noun(self):
        if self.meaning:
            if "Noun" in self.meaning:
                return ". ".join(self.meaning["Noun"])
            else:
                return "None"
        else:
            return "None"

    def Verb(self):
        if self.meaning:
            if "Verb" in self.meaning:
                return ". ".join(self.meaning["Verb"])
            else:
                return "None"
        else:
            return "None"

    def Adjective(self):
        if self.meaning:
            if "Adjective" in self.meaning:
                return ". ".join(self.meaning["Adjective"])
            else:
                return "None"
        else:
            return "None"
