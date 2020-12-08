import sys
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.Qt import PYQT_VERSION_STR
print(PYQT_VERSION_STR)

form_class = uic.loadUiType("python_ui3.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        print('1')

        #WebEngineView의 시그널
        self.webEngineView.loadStarted.connect(self.printLoadStart)
        self.webEngineView.loadProgress.connect(self.printLoading)
        self.webEngineView.loadFinished.connect(self.printLoadFinished)
        self.webEngineView.urlChanged.connect(self.urlChangedFunction)

        #버튼들에 기능을 연결
        self.Go_bt.clicked.connect(self.urlGo)
        self.Back_bt.clicked.connect(self.btnBackFunc)
        self.Forward_bt.clicked.connect(self.btnForwardFunc)
        self.Reload_bt.clicked.connect(self.btnReloadFunc)
        self.Stop_bt.clicked.connect(self.btnStopFunc)

    #WebEngineView의 시그널에 연결된 함수들
    def printLoadStart(self): print('Start Loading')
    def printLoading(self): print('Loading')
    def printLoadFinished(self): print('Load Finished')

    def urlChangedFunction(self):
        self.Url_edit.setText(self.webEngineView.url().toString())
        print('URL Changed')


    #버튼을 눌렀을 때 실행될 함수들
    def urlGo(self):
        self.webEngineView.load(QUrl(self.Url_edit.text()))

    def btnBackFunc(self):
        self.webEngineView.back()

    def btnForwardFunc(self):
        self.webEngineView.forward()

    def btnReloadFunc(self):
        self.webEngineView.reload()

    def btnStopFunc(self):
        self.webEngineView.stop()



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()


#병합해보자
