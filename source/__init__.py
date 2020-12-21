import os
import sys
import time
import warnings

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import qdarkstyle
from hmmlearn.hmm import GaussianHMM
from pgmpy.estimators import (BayesianEstimator, BicScore, HillClimbSearch,
                              MaximumLikelihoodEstimator, ParameterEstimator)
from pgmpy.models import BayesianModel
from PyQt5.Qt import QUrl
from PyQt5.QtCore import (QCoreApplication, QRect, Qt, QThread, QTimer,
                          pyqtSignal)
from PyQt5.QtGui import QBrush, QColor, QFont, QIcon, QMovie, QPixmap
from PyQt5.QtMultimedia import (QMediaContent, QMediaPlayer, QMediaPlaylist,
                                QSound)
from PyQt5.QtWidgets import (QApplication, QCheckBox, QDesktopWidget, QDialog,
                             QFileDialog, QFrame, QHBoxLayout, QHeaderView,
                             QLabel, QLCDNumber, QLineEdit, QMainWindow,
                             QMessageBox, QProgressBar, QPushButton,
                             QRadioButton, QSplitter, QStackedWidget,
                             QTableWidget, QTableWidgetItem, QTextBrowser,
                             QTextEdit, QVBoxLayout, QWidget)
from sklearn import preprocessing, tree
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (accuracy_score, f1_score, mean_absolute_error,
                             median_absolute_error, precision_score, r2_score,
                             recall_score)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import (LabelEncoder, OneHotEncoder,
                                   PolynomialFeatures)
from sklearn.tree import DecisionTreeRegressor

# import Algorithms as agt
# import BIRCHCITY as bc
# import BIRCHPOINTS as bps
# import BIRCHPOS as bp
# import DBSCANCITY as dc
# import DBSCANPOINTS as dps
# import DBSCANPOS as dp
# import DevideData as dvd
# import GMMCITY as gc
# import GMMPOINTS as gps
# import GMMPOS as gp
# import KMEANCITY as kc
# import KMEANPOINTS as kps
# import KMEANPOS as kp
# import OPTICSCITY as oc
# import OPTICSPOINTS as ops
# import OPTICSPOS as op
# import PlotPhoto as plp
# import xgboost
from lcgMain import Lcg
# import zjfMain as zjfM

warnings.filterwarnings('ignore')






plt.axis('off')
