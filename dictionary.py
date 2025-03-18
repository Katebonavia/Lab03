class Dictionary:
    def __init__(self):
        self.words = []

    def loadDictionary(self,path):
        self.words = path.split()
        return self.words


    def printAll(self):
        for word in self.words:
            print(word)


    @property
    def dict(self):
        return self._dict

