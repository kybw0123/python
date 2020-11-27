import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("python_ui2.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #Vertical Slider의 시그널 사용
        self.verticalSlider.valueChanged.connect(self.showVerticalSliderValue)
        self.verticalSlider.rangeChanged.connect(self.printRangeChanged)

        #Horizontal Slider의 시그널 사용
        self.horizontalSlider.valueChanged.connect(self.showHorizontalSliderValue)
        self.horizontalSlider.rangeChanged.connect(self.printRangeChanged)

        #Dial의 시그널 사용
        self.dial.valueChanged.connect(self.showDialValue)
        self.dial.rangeChanged.connect(self.printRangeChanged)

        #버튼에 기능 연결
        self.VInfo_bt.clicked.connect(self.getVerticalInfo)
        self.VRange_bt.clicked.connect(self.setVertical)
        self.HInfo_bt.clicked.connect(self.getHorizontalInfo)
        self.HRange_bt.clicked.connect(self.setHorizontal)
        self.DInfo_bt.clicked.connect(self.getDialInfo)
        self.DRange_bt.clicked.connect(self.setDial)




    def printRangeChanged(self) :
        print("Range Changed")

    #Vertical slider에 관련된 함수들

    def showVerticalSliderValue(self) :
        #Vertical Slider의 시그널 이용 - Vertical Slider의 값이 변경되면 Label에 값을 표시
        self.label2.setText(str(self.verticalSlider.value()))

    def getVerticalInfo(self) :
        #Vertical Slider의 최대/최소값과 PageStep/SingleStep값을 출력합니다.
        print("Maximum : " + str(self.verticalSlider.maximum()))
        print("Minimum : " + str(self.verticalSlider.minimum()))
        print("PageStep : " + str(self.verticalSlider.pageStep()))
        print("SigleStep : " + str(self.verticalSlider.singleStep()))

    def setVertical(self) :
        #Vertical Slider의 최대/최소값과 PageStep/SingleStep값을 변경합니다.
        self.verticalSlider.setMaximum(500)
        self.verticalSlider.setMinimum(-500)
        self.verticalSlider.setPageStep(100)
        self.verticalSlider.setSingleStep(20)

    #Hoeizontal Slider에 관련된 함수들

    def showHorizontalSliderValue(self) :
        #Horizontal Slider의 시그널 이용 - Horizontal Slider의 값이 변경되면 Label에 값을 표시
        self.label.setText(str(self.horizontalSlider.value()))

    def getHorizontalInfo(self) :
        #Horizontal Slider의 최대/최솟값과 PageStep/SingleStep값을 출력합니다.
        print("Maximum : " + str(self.horizontalSlider.maximum()))
        print("Minimum : " + str(self.horizontalSlider.minimum()))
        print("PageStep : " + str(self.horizontalSlider.pageStep()))
        print("SingleStep : " + str(self.horizontalSlider.singleStep()))

    def setHorizontal(self) :
        self.horizontalSlider.setMaximum(500)
        self.horizontalSlider.setMinimum(-500)
        self.horizontalSlider.setPageStep(100)
        self.horizontalSlider.setSingleStep(20)

    #Dial에 관련된 함수들

    def showDialValue(self) :
        #Dial의 시그널 이용 - dial의 값이 변경되면 Label에 값을 표시
        self.label3.setText(str(self.dial.value()))

    def getDialInfo(self) :
        #Dial의 최대/최솟값과 PageStep/SingleStep값을 출력합니다.
        print("Maximum : " + str(self.dial.maximum()))
        print("Minimum : " + str(self.dial.minimum()))
        print("PageStep : " + str(self.dial.pageStep()))
        print("SingleStep : " + str(self.dial.singleStep()))

    def setDial(self) :
        #Dial의 최대/최솟값과 PageStep/SingleStep값을 변경합니다.
        self.dial.setMaximum(500)
        self.dial.setMinimum(-500)
        self.dial.setPageStep(100)
        self.dial.setSingleStep(20)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
