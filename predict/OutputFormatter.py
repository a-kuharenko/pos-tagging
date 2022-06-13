class OutputFormatter:
    def __init__(self):
        self.dictionary = {
            'NOUN': 'Іменник',
            'ADJ': 'Прикметник',
            'PUNCT': 'Знак пунктуації',
            'PRON': 'Займенник',
            'CCONJ': 'Сурядний сполучник',
            'VERB': 'Дієслово',
            'DET': 'Присвійний займенник',
            'PROPN': 'Власна назва',
            'PART': 'Частка',
            'SCONJ': 'Підрядний сполучник',
            'ADP': 'Прийменник',
            'ADV': 'Прислівник',
            'AUX': 'Дієслово',
            'NUM': 'Числівник',
            'INTJ': 'Вигук',
            'X': 'Інше'
        }

    def tagToTerm(self, tag):
        return self.dictionary[tag]

