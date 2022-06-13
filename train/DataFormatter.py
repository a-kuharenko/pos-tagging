import math

class DataFormatter:    
    def __isEmptyLine(self, data, lineNumber):
        return math.isnan(data.iloc[lineNumber, 0])
    
    def __isSentBeggining(self, data, lineNumber):
        return data.iloc[lineNumber, 0] == 1.0

    def __filterEmptyWords(self, sents): 
        for sentence in sents:
            for i, word in enumerate(sentence):
                if type(word[0]) != str:
                    del sentence[i] 

    def formatDataIntoSentences(self, data):
        sents = []
        for i in range(len(data)):
            if self.__isEmptyLine(data, i):
                continue
            if self.__isSentBeggining(data, i):
                word = data.iloc[i, 1]
                tag = data.iloc[i, 3]
                sents.append([[word, tag]])
            else:
                word = data.iloc[i, 1]
                tag = data.iloc[i, 3]
                sents[-1].append([word, tag])
        self.__filterEmptyWords(sents)
        return sents
