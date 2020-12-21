import warnings

from PyQt5.QtCore import QThread
from matplotlib import pyplot as plt
import adaboost
import adaboost_dating
import bayes
import bayes_dating
import GBDT
import GBDT_dating
import knn
import knn_dating
import logistic
import logistic_dating
import randomforest
import randomforest_dating
import svm
import svm_dating
import decesionTree
import decesionTree_dating
import softmax
import softmax_dating
import deepForest
import deepForest_dating
from __init__ import *

warnings.filterwarnings('ignore')


class Lcg(QThread):
    # 自定义信号
    resMsgSignal = pyqtSignal(str)
    resultSignal = pyqtSignal(list)
    resMeansSignal = pyqtSignal(list)
    funcsNameSignal = pyqtSignal(list)

    def __init__(self):
        super(Lcg, self).__init__()

    def __del__(self):
        self.wait()

    def execution(self):
        funcsName = ['adaboost', 'adaboost_dating', 'bayes', 'bayes_dating', 'GBDT', 'GBDT_dating', 'knn', 'knn_dating', 'logistic', 'logistic_dating', 'randomforest', 'randomforest_dating', 'svm', 'svm_dating','decesionTree','decesionTree_dating','softmax','softmax_dating','deepForest','deepForest_dating']
        self.funcsNameSignal.emit(funcsName)
        funcs = [adaboost, adaboost_dating, bayes, bayes_dating, GBDT, GBDT_dating, knn, knn_dating, logistic, logistic_dating, randomforest, randomforest_dating, svm, svm_dating, decesionTree, decesionTree_dating, softmax, softmax_dating,deepForest,deepForest_dating]

        resMsgs = []
        resMeans = []
        result = []
        for func in funcs:
            res = func.main()
            # print(res[1], type(res[1]))
            result.append(res[0][0])
            resMsgs.append(res[1])
            resMeans.append(res[2])
            self.resMsgSignal.emit(res[1])

        # print(result)

        self.resultSignal.emit(result)
        self.resMeansSignal.emit(resMeans)
        # print("信号在这",resMsgs)

    def run(self):
        self.execution()


if __name__ == "__main__":
    a = Lcg()
    a.execution()
    # a.plot()