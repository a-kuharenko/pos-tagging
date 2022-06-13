import string, re



class FeatureParser:
    def __init__(self):
        self.features = {}

    def parseFeaturesForWord(self, sentence, wordIndex):
        self.features = {}
        word = sentence[wordIndex][0]
        self.__parseCurrentWorkFeatures(word)
        if wordIndex > 0: 
            self.__parsePreviousWordFeatures(sentence[wordIndex-1][0])
        if wordIndex == 0:
            self.features['BOS'] = True
        if wordIndex > 1:
            self.__parseTwoPlacesBeforeWordFeatures(sentence[wordIndex-2][0])
        if wordIndex < len(sentence)-1:
            self.__parseNextWordFeatures(sentence[wordIndex+1][0])
        if wordIndex < len(sentence)-2:
            self.__parseNextWordFeatures(sentence[wordIndex+2][0])
        if wordIndex == len(sentence)-1:
            self.features['EOS'] = True
        return self.features
    
    def parseSentTofeatures(self, sentence):
        return [self.parseFeaturesForWord(sentence, i) for i in range(len(sentence))]

    def parseSentTolabels(self, sentence):
        return [w[1] for w in sentence]

    def parseSentTotokens(self, sentence):
        return [w[0] for w in sentence]

    def __parseCurrentWorkFeatures(self, word):
        self.features.update({
            'bias': 1.0,
            'word': word,
            'length': len(word),
            'word[:4]': self.__getSuffix(word, 4),
            'word[:3]': self.__getSuffix(word, 3),
            'word[:2]': self.__getSuffix(word, 2),
            'word[-2:]': self.__getPrefix(word, 2),
            'word[-3:]': self.__getPrefix(word, 3),
            'word[-4:]': self.__getPrefix(word, 4),
            'word.lower()': word.lower(),
            'word.stemmed': self.__getStemmedWord(word),
            'word.ispunctuation': self.__isPunct(word),
            'word.__isDigit()': self.__isDigit(word),
        })

    def __parsePreviousWordFeatures(self, word):
        self.features.update({
            '-1:word': word,
            '-1:length': len(word),
            '-1:word.lower()': word.lower(),
            '-1:word.stemmed': self.__getStemmedWord(word),
            '-1:word[:3]': self.__getSuffix(word, 3),
            '-1:word[:2]': self.__getSuffix(word, 2),
            '-1:word[-3:]': self.__getPrefix(word, 3),
            '-1:word[-2:]': self.__getPrefix(word, 2),
            '-1:word.__isDigit()': self.__isDigit(word),
            '-1:word.ispunctuation': self.__isPunct(word),
        })

    def __parseTwoPlacesBeforeWordFeatures(self, word):
        self.features.update({
            '-2:word': word,
            '-2:length': len(word),
            '-2:word.lower()': word.lower(),
            '-2:word[:3]': self.__getSuffix(word, 3),
            '-2:word[:2]': self.__getSuffix(word, 2),
            '-2:word[-3:]': self.__getPrefix(word, 3),
            '-2:word[-2:]': self.__getPrefix(word, 2),
            '-2:word.__isDigit()': self.__isDigit(word),
            '-2:word.ispunctuation': self.__isPunct(word),
        })

    def __parseNextWordFeatures(self, word):
        self.features.update({
            '+1:word': word,
            '+1:length': len(word),
            '+1:word.lower()': word.lower(),
            '+1:word.stemmed': self.__getStemmedWord(word),
            '+1:word[:3]': self.__getSuffix(word, 3),
            '+1:word[:2]': self.__getSuffix(word, 2),
            '+1:word[-3:]': self.__getPrefix(word, 3),
            '+1:word[-2:]': self.__getPrefix(word, 2),
            '+1:word.__isDigit()': self.__isDigit(word),
            '+1:word.ispunctuation': self.__isPunct(word),
        })

    def parseTwoPlacesNextWordFeatures(self, word):
        self.features.update({
            '+2:word': word,
            '+2:length': len(word),
            '+2:word.lower()': word.lower(),
            '+2:word.stemmed': self.__getStemmedWord(word),
            '+2:word[:3]': self.__getSuffix(word, 3),
            '+2:word[:2]': self.__getSuffix(word, 2),
            '+2:word[-3:]': self.__getPrefix(word, 3),
            '+2:word[-2:]': self.__getPrefix(word, 2),
            '+2:word.__isDigit()': self.__isDigit(word),
            '+2:word.ispunctuation': self.__isPunct(word),
        })

    def __getStemmedWord(self, word): 
        return re.sub(r'(.{2,}?)([іиауе(ий)(ом)(ох)(ів)(їв)(ар)(зм)]+$)',r'\1', word.lower())
    
    def __getSuffix(self, word, length): 
        return word[:length]

    def __getPrefix(self, word, length): 
        return word[-length:]
    
    def __isPunct(self, word): 
        return (word in string.punctuation)
    
    def __isDigit(self, word): 
        return word.isdigit()
