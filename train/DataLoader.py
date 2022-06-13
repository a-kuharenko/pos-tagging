import pandas as pd

class DataLoader:
    def __init__(self):
        self.data = {}

    def loadTrainData(self, path, sep = '\t'):
        self.data['train'] = pd.read_csv(filepath_or_buffer=path,  sep=sep)

    def loadTestData(self, path, sep = '\t'):
        self.data['test'] = pd.read_csv(filepath_or_buffer=path,  sep=sep)
