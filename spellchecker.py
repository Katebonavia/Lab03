import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multdic = md.MultiDictionary()
        self.single_words = []

    def handleSentence(self, txtIn, language):
        txtIn2=replaceChars(txtIn)
        print(txtIn2)
        self.single_words=txtIn2.split()
        print(self.single_words)
        self.multdic.searchWord(self.single_words,language)

    def handleSentenceLinear(self, txtIn, language):
        txtIn2 = replaceChars(txtIn)
        self.single_words = txtIn2.split()
        self.multdic.searchWordLinear(self.single_words, language)

    def handleSentenceDichotomic(self, txtIn, language):
        txtIn2 = replaceChars(txtIn)
        self.single_words = txtIn2.split()
        self.multdic.searchWordDichotomic(self.single_words, language)

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.?!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text