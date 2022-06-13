from sklearn_crfsuite import metrics
from collections import Counter


class MetricsCollector:
    def __init__(self, model):
        self.model = model
        self.labels = list(model.model.classes_)
        self.labels.remove('X')

    def getMetrics(self, predictData, yData):
        sortedLabels = sorted(self.labels, key=lambda n: (n[1:], n[0]))
        ypred = self.model.predict(predictData)
        f1 = metrics.flat_f1_score(yData, ypred, average='weighted', labels=sortedLabels)
        accuracy = metrics.flat_accuracy_score(yData, ypred)
        report = metrics.flat_classification_report(yData, ypred)
        return f1, accuracy, report

    def __printTransitions(self, transitionFeatures):
        print("TAG_FROM -> TAG_TO WEIGHT")
        for (labelFrom, labelTo), weight in transitionFeatures:
            print("%-6s -> %-7s %0.6f" % (labelFrom, labelTo, weight))

    def printTransitions(self):
        TOP = 10
        print("Top 10 найбільш імовірних переходів: \n")
        self.__printTransitions(Counter(self.model.model.transition_features_).most_common(TOP))
        print("\n\n")
        print("Top 10 найменш імовірних переходів: \n")
        self.__printTransitions(Counter(self.model.model.transition_features_).most_common()[-TOP:])