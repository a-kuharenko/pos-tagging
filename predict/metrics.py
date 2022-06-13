
import sys

sys.path.insert(0, '/Users/sandrk/Diplom/refactored_code/common')
sys.path.insert(0, '/Users/sandrk/Diplom/refactored_code/train')

from DataLoader import DataLoader
from DataFormatter import DataFormatter
from MetricsCollector import MetricsCollector
from Tokenizator import Tokenizator
from OutputFormatter import OutputFormatter
from CRFPredictModel import CRFPredictModel
from FeatureParser import FeatureParser
from CRFTrainModel import CRFTrainModel

PATH_TO_MODEL = '/Users/sandrk/Diplom/refactored_code/model.pkl'

tokenizator = Tokenizator()
outputFormatter = OutputFormatter()
featureParser = FeatureParser()
predictModel = CRFPredictModel(PATH_TO_MODEL, featureParser)

PATH_TO_TEST_DATA = '/Users/sandrk/Diplom/refactored_code/train/data/test-sents.conllu'
PATH_TO_TRAIN_DATA = '/Users/sandrk/Diplom/refactored_code/train/data/train-sents.conllu'

dataLoader = DataLoader()
dataLoader.loadTestData(PATH_TO_TEST_DATA)
dataLoader.loadTrainData(PATH_TO_TRAIN_DATA)

dataFormatter = DataFormatter()
trainSentences = dataFormatter.formatDataIntoSentences(dataLoader.data['train'])
testSentences = dataFormatter.formatDataIntoSentences(dataLoader.data['test'])

trainModel = CRFTrainModel(c1=0.25, c2=0.35, maxIterations=100, featureParser=featureParser)
XtrainData = trainModel.prepareXtrainData(trainSentences)
YtrainData = trainModel.prepareYtrainData(trainSentences)

XtestData = trainModel.prepareXtrainData(testSentences)
yTestData = trainModel.prepareYtrainData(testSentences)

metricsCollector = MetricsCollector(predictModel)
trainMetrics = metricsCollector.getMetrics(XtrainData, YtrainData)
testMetrics = metricsCollector.getMetrics(XtestData, yTestData)

print('F1 score на датасеті тренування = {}\n'.format(trainMetrics[0]))
print('Точність на датасеті тренування = {}\n'.format(trainMetrics[1]))
print('Звіт классифікації для датасета тренування: \n\n{}'.format(trainMetrics[2]))

print('F1 score на датасеті тестування = {}\n'.format(testMetrics[0]))
print('Точність на датасеті тестування = {}\n'.format(testMetrics[1]))
print('Звіт классифікації для датасета тестування: \n\n{}'.format(testMetrics[2]))

metricsCollector.printTransitions()