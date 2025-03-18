import dictionary as d
import richWord as rw
import importlib.resources as resources

class MultiDictionary:
    def __init__(self):
        self.dict_words = []
        self.rich_words = []
        self.false_rw = []
        self.dict = d.Dictionary()

    def printDic(self, language):
        if language.__eq__("english"):
            path = resources.read_text('resources', 'English.txt')
            self.dict_words = self.dict.loadDictionary(path)
        if language.__eq__("italian"):
            path = resources.read_text('resources', 'Italian.txt')
            self.dict_words = self.dict.loadDictionary(path)
        if language.__eq__("spanish"):
            path = resources.read_text('resources', 'Spanish.txt')
            self.dict_words = self.dict.loadDictionary(path)


    def searchWord(self, words, language):
        self.printDic(language)
        for word in words:
            #print(word)
            richword = rw.RichWord(word)
            if self.dict_words.__contains__(word):
                #print(f"la parola {word} esiste")
                richword.corretta = True
            self.rich_words.append(richword)
            if richword.corretta.__eq__(False):
                #print(f"la parola {word} NON esiste")
                self.false_rw.append(word)
        for n in self.false_rw:
            print(n)
        self.false_rw=[]

    def searchWordLinear(self, words, language):
        for word in words:
            # print(word)
            richword = rw.RichWord(word)
            for d in self.dict_words:
                if d==word:
                    richword.corretta = True
            self.rich_words.append(richword)
            if richword.corretta.__eq__(False):
                # print(f"la parola {word} NON esiste")
                self.false_rw.append(word)
        for n in self.false_rw:
            print(n)
        self.false_rw = []

    def searchWordDichotomic(self, words, language):
        pass




