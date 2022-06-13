import PySimpleGUI as sg

FONT = ('', 18)
THEME_NAME = 'BluePurple'

CLEAR_KEY = '-CLEAR-'
TAG_KEY = '-TAG-'
TREE_KEY = '-TREE-'
INPUT_KEY = '-IN-'


class Client:
    def __init__(self, tokenizator, model, outputFormatter):
        sg.theme(THEME_NAME)
        treedata = sg.TreeData()
        self.tokenizator = tokenizator
        self.model = model
        self.outputFormatter = outputFormatter
        layout = [[sg.Text('Введіть текст для POS-тегування:', font=FONT)],
                  [sg.Multiline(key=INPUT_KEY, size=(250, 10), font=FONT)],
                  [sg.Button('Тегувати', key=TAG_KEY, auto_size_button=True, font=FONT), sg.Button(
                      'Очистити', key=CLEAR_KEY, auto_size_button=True, font=FONT)],
                  [sg.Tree(treedata, ['Частина мови'], num_rows=30, col0_width=122, key=TREE_KEY, justification='center', row_height=20, font=('', 14))]]
        self.window = sg.Window('POS-тегування', layout, size=(1400, 800))

    def __fillTree(self, sentences, tokenized, prediction):
        treedata = sg.TreeData()
        i = 0
        for s in sentences:
            treedata.Insert("", s, s, [])
            j = 0
            for w in tokenized[i]:
                word = w[0]
                tag = prediction[i][j]
                term = self.outputFormatter.tagToTerm(tag)
                treedata.Insert(s, s+word, w, [term])
                j = j + 1
            i = i + 1
        return treedata

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == CLEAR_KEY:
                treedata = sg.TreeData()
                self.window[INPUT_KEY].update('')
                self.window[TREE_KEY].update(treedata)
            if event == TAG_KEY:
                text = values[INPUT_KEY]
                tokenized = self.tokenizator.tokenizeText(text)
                sentences = self.tokenizator.tokenizeSentences(text)

                predictData = self.model.preparePredictData(tokenized)
                result = self.model.predict(predictData)

                treedata = self.__fillTree(sentences, tokenized, result)
                self.window[TREE_KEY].update(treedata)
        self.window.close()
