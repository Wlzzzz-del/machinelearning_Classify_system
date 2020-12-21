import pandas
import matplotlib. pyplot as plt
from sklearn import model_selection
from sklearn.svm import SVC

def main1():
    #读取并处理数据
    dataframe = pandas.read_csv("../Data/dating.csv")
    dataframe =dataframe.astype(float)
    array = dataframe.values#将格式转化为array数组
    X = array[:, 0:8]
    Y = array[:, 8]
    seed = 7
    models = []
    models.append(('SVM', SVC()))
    results = []
    names = []
    scoring = 'accuracy'#评价指标
    for name, model in models:
        kfold = model_selection.KFold(n_splits=15, random_state=seed)#交叉验证
        cv_results = model_selection.cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
        results.append(cv_results)
        names.append(name)
        resMsg = "%s: %f(%f)" % (name, cv_results.mean(), cv_results.std())
        # print(resMsg)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_xticklabels(names)

    return results, resMsg, cv_results.mean()

if __name__ == '__main__':
    main1()