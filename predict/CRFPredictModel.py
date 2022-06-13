
import joblib


class CRFPredictModel:
    def __init__(self, path, featureParser):
        self.model = joblib.load(path)
        self.featureParser = featureParser

    def predict(self, data):
        return self.model.predict(data)

    def preparePredictData(self, tokenizedData):
        return [self.featureParser.parseSentTofeatures(s) for s in tokenizedData]
