
import sklearn_crfsuite
import joblib

class CRFTrainModel:
    def __init__(self, c1, c2, maxIterations, featureParser):
        self.model = sklearn_crfsuite.CRF(
            algorithm = 'lbfgs',
            c1 = c1,
            c2 = c2,
            max_iterations = maxIterations,
            all_possible_transitions=True
        )
        self.featureParser = featureParser

    def train(self, Xtrain, Ytrain):
        self.model.fit(Xtrain, Ytrain) 

    def saveModel(self, path):
        joblib.dump(self.model, path) 
    
    def prepareXtrainData(self, trainSentences):
        return [self.featureParser.parseSentTofeatures(s) for s in trainSentences]
    
    def prepareYtrainData(self, trainSentences):
        return [self.featureParser.parseSentTolabels(s) for s in trainSentences]