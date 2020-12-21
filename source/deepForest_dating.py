import pandas
import matplotlib.pyplot as plt
import GCForest
from sklearn import model_selection
from GCForest import  accuracy_score

def main():
    dataframe = pandas.read_csv("../Data/dating.csv")
    dataframe = dataframe.astype(float)
    array = dataframe.values  # 将格式转化为array数组
    X = array[:, 0:8]
    Y = array[:, 8]
    seed = 7
    model = GCForest.gcForest(shape_1X=4, window=2, tolerance=0.0)
    model.fit(X,Y)
    predict = model.predict(X)
    # print(predict)
    accuracy = accuracy_score(y_true=Y, y_pred=predict)
    print(accuracy)
    resMsg = "GCForest: %f"%(accuracy)
    return predict, resMsg, accuracy
if __name__ == '__main__':
    main()
