# machinelearning_Classify_system
机器学习课程期末课设作业
# 功能
分类系统通过选择数据集，然后选择分类器，导入数据并设计好训练及比例后，运行代码开始进行训练，最后输出运行结果。通过对机器学习课程训练任务的分析和网上查阅资料，选用KNN、贝叶斯分类器、SVM、AdaBoost、深度森林、随机森林、SoftMax、决策树、逻辑回归、GBDT 10种分类模型，使用水果分类、好感度分析2个数据集，准确率、召回率、标准差3种评价指标。该系统包含了大部分
机器学习模型，大中小规模的结构化数据集与多个评价指标，系统设计较为科学、不同算法之间的对比较为全面。

# 所用模型与实现
- knn
- baynes
- random forest
- decision tree
- logistics
- softmax
- GBDT
- Adaboost
- SVM  
以上模型通过调用sklearn建模实现
- gcForest
通过调用GitHub上开源的 [深度森林](https://github.com/kingfengji/gcForest)实现
