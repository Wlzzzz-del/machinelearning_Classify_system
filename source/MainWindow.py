from __init__ import *


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.buttons = []
        self.filePath = ''
        self.lqrResult = pd.DataFrame([])
        self.lcgResult = []
        self.lcgResMeans = []
        self.zjfResult = []
        self.lcgFuncsName = []
        self.init_ui()


    def init_ui(self):

        self.leftUI()
        self.rightUI()
        mainFrame = QWidget(self)
        mainFrameHlayout = QHBoxLayout()

        # 将splitter添加进布局
        mainFrameHlayout.addWidget(self.leftSplitter)
        mainFrameHlayout.addWidget(self.rightSplitter)
        
        self.progressBar = QProgressBar(self)
        self.statusBar().addPermanentWidget(self.progressBar)
        self.progressBar.hide()
        mainFrame.setLayout(mainFrameHlayout)
        self.setCentralWidget(mainFrame)

        # self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        self.statusBar().showMessage("请选择...")
        self.setWindowTitle("功能选择")
        # self.setWindowIcon(QIcon("../icon/3_BigPic.png"))
        self.setinUI()

    """ 左侧 Frame """
    def leftUI(self):
        
        """ 任务选择 """
        taskFrame = QFrame(self)
        taskFrame.setFrameShape(QFrame.StyledPanel)
        taskFrameVlayout = QVBoxLayout(taskFrame)
        
        """ 按钮 """
        # 分类
        self.taskBtn1 = QPushButton(taskFrame)
        self.taskBtn1.setText("分  类")
        self.taskBtn1.clicked.connect(self.clickTaskBtn1)

        # 退出
        self.btn_quit = QPushButton(taskFrame)
        self.btn_quit.setText("退  出")
        self.btn_quit.clicked.connect(self.clickQuit)

        # 将按钮添加进任务布局
        taskFrameVlayout.addWidget(self.taskBtn1)
        taskFrameVlayout.addWidget(self.btn_quit)

        """ 时间表 """
        timeFrame = QFrame(self)
        timeFrame.setFrameShape(QFrame.StyledPanel)
        timeFrameVlayout = QVBoxLayout(timeFrame)

        # 北京时间
        timeLabel = QLabel(self)
        timeLabel.setText("北京时间")
        timeLabel.setAlignment(Qt.AlignCenter)
        timeLabel.setFont(QFont("微软雅黑", 18, QFont.Bold))

        # 电子表
        self.lcd = QLCDNumber()
        self.lcd.setDigitCount(10)
        self.lcd.setMode(QLCDNumber.Dec)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.lcd.display(time.strftime("%X", time.localtime()))

        self.timer = QTimer()
        self.timer.setSingleShot(False)
        self.timer.start()

        # 链接信号槽
        self.timer.timeout.connect(self.onTimeOut)
        
        timeFrameVlayout.addWidget(timeLabel)
        timeFrameVlayout.addWidget(self.lcd)

        """ 
        负责人
        """
        principalFrame = QFrame(self)
        principalFrame.setFrameShape(QFrame.StyledPanel)
        principalFrameVlayout = QVBoxLayout(principalFrame)

        lcgTask = QLabel(self)
        lcgTask.setText("分类系统")
        lcgTask.setAlignment(Qt.AlignLeft)
        lcgTask.setFont(QFont("微软雅黑", 15, QFont.Bold))

        lcgTaskText = QLabel(self)
        lcgTaskText.setText("吴立钊")
        lcgTaskText.setAlignment(Qt.AlignCenter)
        lcgTaskText.setFont(QFont("黑体", 13, QFont.Bold))


        principalFrameVlayout.addWidget(lcgTask)
        principalFrameVlayout.addWidget(lcgTaskText)

        self.leftSplitter = QSplitter(Qt.Vertical)
        self.leftSplitter.addWidget(taskFrame)
        self.leftSplitter.addWidget(timeFrame)
        self.leftSplitter.addWidget(principalFrame)

    def clickTaskBtn1(self):
        self.statusBar().showMessage("准备就绪...")
        self.rightStacked.setCurrentIndex(1)


    def clickTaskBtn2(self):
        self.statusBar().showMessage("准备就绪...")
        self.rightStacked.setCurrentIndex(2)


    def clickTaskBtn3(self):
        self.statusBar().showMessage("准备就绪...")
        self.rightStacked.setCurrentIndex(3)

    
    def onTimeOut(self):
        self.lcd.display(time.strftime("%X", time.localtime()))


    """ 退出按钮 """
    def clickQuit(self):
        # quit_sure = QMessageBox.question(self, "", "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        quit_sure = QMessageBox.question(self, "退出提示", "您确定要退出吗？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if quit_sure == QMessageBox.Yes:
            QCoreApplication.instance().quit()

    
    def rightUI(self):
        rightFrame = QFrame(self)
        rightFrame.setFrameShape(QFrame.StyledPanel)
        rightFrameVlayout = QVBoxLayout(rightFrame)
        # 设置 stackedWidget
        self.rightStacked = QStackedWidget()
        rightFrameVlayout.addWidget(self.rightStacked)

        # 面板初始化
        self.initFrame()
        # 分类
        self.classifyFrame()
        # # 预测
        # self.predictFrame()
        # # 聚类
        # self.clusterFrame()

        # 将面板加入 stacked widget
        self.rightStacked.addWidget(self.initForm)
        self.rightStacked.addWidget(self.classifyForm)
        # self.rightStacked.addWidget(self.predictForm)
        # self.rightStacked.addWidget(self.clusterForm)
        self.rightStacked.setCurrentIndex(0)
        self.rightSplitter = QSplitter(Qt.Vertical)
        self.rightSplitter.addWidget(rightFrame)


    """ 面板初始化 """
    def initFrame(self):
        self.initForm = QWidget()
        self.initFormLayout = QVBoxLayout(self.initForm)

        self.initForm = QFrame(self)
        self.initForm.setFrameShape(QFrame.StyledPanel)
        initFormVlayout = QVBoxLayout(self.initForm)

        photo_ai = QPixmap("../photo/55.jpg")
        photo_ai_lable = QLabel(self)
        photo_ai_lable.setPixmap(photo_ai)
        photo_ai_lable.setAlignment(Qt.AlignCenter)

        initFormVlayout.addWidget(photo_ai_lable)


    """ 分类 """
    def classifyFrame(self):
        self.classifyForm = QWidget()
        self.classifyFormLayout = QVBoxLayout(self.classifyForm)
        
        btnForm = QWidget()
        btnFormLayout = QHBoxLayout(btnForm)
        self.lcgExeBtn = QPushButton()
        self.lcgExeBtn.setText("执行")
        self.lcgExeBtn.clicked.connect(self.clickLcgExeBtn)

        self.lcgPlotBtn = QPushButton()
        self.lcgPlotBtn.setText("作图")
        self.lcgPlotBtn.clicked.connect(self.clickLcgPlotBtn)

        btnFormLayout.addWidget(self.lcgExeBtn)

        btnFormLayout.addWidget(self.lcgPlotBtn)

        self.buttons.append(self.lcgExeBtn)

        self.buttons.append(self.lcgPlotBtn)

        self.classifyFormLayout.addWidget(btnForm)

        self.textBrowser = QTextBrowser()
        # self.textBrowser.move(160,30)
        self.textBrowser.resize(100, 100)
        self.classifyFormLayout.addWidget(self.textBrowser)
    
    def clickLcgExeBtn(self):
        self.lcgSignal = ''
        self.lcg = Lcg() # 这里必须要有self，否则无法实时传值
        self.lcg.resMsgSignal.connect(self.setLcgMsgSignal)
        self.lcg.resultSignal.connect(self.lcgReslutSignal)
        self.lcg.resMeansSignal.connect(self.lcgResMeansSignal)
        self.lcg.funcsNameSignal.connect(self.lcgfuncsNameSignal)
        self.lcg.start()


    def setLcgMsgSignal(self, msg):
        self.lcgSignal += msg
        self.lcgSignal += '\n'
        self.textBrowser.setText(self.lcgSignal)

    def clickLcgPlotBtn(self):
        print(1)
        if (self.lcgFuncsName):
            print(self.lcgResMeans, type(self.lcgResMeans))
        # plt.plot(list(self.lcgResMeans))
        # plt.ion()
        # plt.show()
        # plt.plot([1,2,3,4])
        # # plt.plot([i for i in range(10)])
        # plt.show()
        # plt.close()
            #
            # plt.figure(figsize=(16, 9))
            # matplotlib.rcParams['font.family'] = ["simhei", 'Times new roman']
            # matplotlib.rcParams['font.size'] = 30
            # plt.style.use('ggplot')
            # plt.bar([i for i in range(len(self.lcgResMeans))], self.lcgResMeans, 0.4, color='b')
            # plt.xlabel('算法', fontsize=15)
            # plt.ylabel('正确率', fontsize=15)
            # plt.grid(True)
            # plt.xticks([i for i in range(len(self.lcgResMeans))], self.lcgResMeans, fontsize=13, rotation=30)
            # plt.close()

            

    def lcgReslutSignal(self, result):
        self.lcgResult = result

    def lcgResMeansSignal(self, resMeans):
        self.lcgResMeans = resMeans
        # print(self.lcgResMeans)

    def lcgfuncsNameSignal(self, names):
        self.lcgFuncsName = names




    """ 重写关闭事件 """
    def closeEvent(self, quit_event):
        
        # quit_sure = QMessageBox.question(self, "", "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        quit_sure = QMessageBox.question(self, "退出提示", "您确定要退出吗？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)


        if quit_sure == QMessageBox.Yes:
            quit_event.accept()
        else:
            quit_event.ignore()

    
    """ 将界面放于中间 """
    def setinUI(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()
    sys.exit(app.exec_())
