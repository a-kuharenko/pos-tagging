import sys
sys.path.insert(0, '/Users/sandrk/Diplom/refactored_code/common')

from CRFTrainModel import CRFTrainModel
from DataFormatter import DataFormatter
from DataLoader import DataLoader
from FeatureParser import FeatureParser

PATH_TO_TEST_DATA = '/Users/sandrk/Diplom/pos-tagging/train/data/test-sents.conllu'
PATH_TO_TRAIN_DATA = '/Users/sandrk/Diplom/pos-tagging/train/data/train-sents.conllu'
PATH_TO_MODEL = 'model.pkl'

dataLoader = DataLoader()
dataLoader.loadTestData(PATH_TO_TEST_DATA)
dataLoader.loadTrainData(PATH_TO_TRAIN_DATA)

dataFormatter = DataFormatter()
trainSentences = dataFormatter.formatDataIntoSentences(dataLoader.data['train'])

featureParser = FeatureParser()
model = CRFTrainModel(c1=0.25, c2=0.35, maxIterations=100, featureParser=featureParser)

XtrainData = model.prepareXtrainData(trainSentences)
YtrainData = model.prepareYtrainData(trainSentences)

model.train(XtrainData, YtrainData)
model.saveModel(PATH_TO_MODEL)
