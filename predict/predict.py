import sys
sys.path.insert(0, '/Users/sandrk/Diplom/refactored_code/common')

from Tokenizator import Tokenizator
from OutputFormatter import OutputFormatter
from CRFPredictModel import CRFPredictModel
from Client import Client
from FeatureParser import FeatureParser

PATH_TO_MODEL = '/Users/sandrk/Diplom/pos-tagging/model.pkl'

tokenizator = Tokenizator()
outputFormatter = OutputFormatter()
featureParser = FeatureParser()
model = CRFPredictModel(PATH_TO_MODEL, featureParser)

client = Client(tokenizator, model, outputFormatter)
client.run()