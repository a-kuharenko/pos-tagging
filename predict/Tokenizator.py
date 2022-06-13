import nltk

class Tokenizator:
    def tokenizeText(self, text):
        sentences = nltk.sent_tokenize(text)
        tokenized = list(map(self.__mapSentenceTokenize, sentences))
        return tokenized

    def tokenizeSentences(self, text):
        return nltk.sent_tokenize(text)

    def __mapWord(self, w):
        return [w]

    def __mapSentenceTokenize(self, s):
        words = nltk.word_tokenize(s)
        return list(map(self.__mapWord, words))
