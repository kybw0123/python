import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
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

        # 프로그램이 실행되면 DateTimeEdit의 값이 현재 날짜/시간으로 설정되게 하기
        self.currentDateTime = QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(self.currentDateTime)

        # 날짜 버튼에 기능 연결
        self.Displayinfo_bt.clicked.connect(self.displayDateTime)
        self.DateTime_bt.clicked.connect(self.enterDateTimeFunc)
        self.Date_bt.clicked.connect(self.enterDateFunc)
        self.Time_bt.clicked.connect(self.enterTimeFunc)
        self.Changeformat_bt.clicked.connect(self.changeDisplayFormat)
        self.Showrange_bt.clicked.connect(self.showRangeFunc)
        self.Editmax_bt.clicked.connect(self.extendMaximum)
        self.Editmin_bt.clicked.connect(self.extendMinimum)

        #QCalendarWidget의 시그널
        self.calendarWidget.clicked.connect(self.calendarClicked)
        self.calendarWidget.currentPageChanged.connect(self.calendarPageChanged)
        self.calendarWidget.selectionChanged.connect(self.calendarSelectionChanged)

        #QCalendarWidget이 자동으로 오늘 날짜가 있는 달력을 보여주게 설정
        self.todayDate = QDate.currentDate()
        self.calendarWidget.setCurrentPage(self.todayDate.year(), self.todayDate.month())

        #버튼에 기능 연결
        self.PMonth_bt.clicked.connect(self.prevMonth)
        self.NMonth_bt.clicked.connect(self.nextMonth)
        self.Today_bt.clicked.connect(self.today)





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

    def displayDateTime(self):
        #DateTimeEdit의 값을 사용할 때는 아래와 같이 객체를 만들고, 그 객체에 값을 저장한 후 사용해야 합니다.
        self.displayDateTimeVar = self.dateTimeEdit.dateTime()
        self.displayDateVar = self.dateTimeEdit.date()
        self.displayTimeVar = self.dateTimeEdit.time()

        #QDateTime, QDate, QTime 객체들의 값을 Label에 표시합니다.
        #toString 함수는 02.12QDateTimeEdit의 하위페이지에 있는 QDateTime, QDate, QTime 함수를 참고하시기 바랍니다.
        self.yyyymmdd24_lb.setText(self.displayDateTimeVar.toString('yyyy-MM-dd AP hh:mm:ss'))
        self.yyyymmdd_lb.setText(self.displayDateVar.toString('yyyy-MM-dd'))
        self.time_lb.setText(self.displayTimeVar.toString('AP hh:mm:ss'))

    def enterDateTimeFunc(self):
        # LineEdit에서 글자를 가져온 후, fromString 함수를 이용해서 QDate객체를 만듭니다.
        # 그 후, setDate 함수를 이용해 DateTimeEdit에 적용합니다.
        self.enterDateTimeText = self.Datetime_edit.text()
        self.enterDateTimeVar = QDateTime.fromString(self.enterDateTimeText, 'yyyy-MM-dd hh:mm:ss')
        self.dateTimeEdit.setDateTime(self.enterDateTimeVar)

    def enterDateFunc(self):
        #LineEdit에서 글자를 가져온 후, fromString 함수를 이용해서 QDate객체를 만듭니다.
        #그 후, setDate 함수를 이용해 DateTimeEdit에 적용합니다.
        self.enterDateText = self.Date_edit.text()
        self.enterDateVar = QDate.fromString(self.enterDateText, 'yyyy-MM-dd')
        self.dateTimeEdit.setDate(self.enterDateVar)

    def enterTimeFunc(self):
        #LineEdit에서 글자를 가져온 후, fromString 함수를 이용해서 QDate객체를 만듭니다.
        #그 후, setDate 함수를 이용해 DateTimeEdit에 적용합니다.
        self.enterTimeText = self.Time_edit.text()
        self.enterTimeVar = QTime.fromString(self.enterTimeText, 'hh:mm:ss')
        self.dateTimeEdit.setTime(self.enterTimeVar)

    def changeDisplayFormat(self):
        #LineEdit에서 글자를 가져온 후, 그 글자를 DateTimeEdit의 형식문자로 지정합니다.
        self.displyFormatText = self.Display_edit.text()
        self.dateTimeEdit.setDisplayFormat(self.displyFormatText)

    def showRangeFunc(self):
        print(self.dateTimeEdit.minimumDateTime())
        print(self.dateTimeEdit.maximumDateTime())

    def extendMaximum(self):
        #DateTimeEdit의 현재 maximumDateTime을 가저옵니다.
        #그 후 addDays 함수를 이용하여 최대값을 10일 연장시킨 후, setMaximumDateTime을 이용하여 DateTimeEdit에 적용시킵니다.
        self.currentMaximumDateTime = self.dateTimeEdit.maximumDateTime()
        self.currentMaximumDateTime = self.currentMaximumDateTime.addDays(10)
        self.dateTimeEdit.setMaximumDateTime(self.currentMaximumDateTime)

    def extendMinimum(self):
        # DateTimeEdit의 현재 maximumDateTime을 가저옵니다.
        # 그 후 addDays 함수를 이용하여 최대값을 10일 연장시킨 후, setMaximumDateTime을 이용하여 DateTimeEdit에 적용시킵니다.
        self.currentMinimumDateTime = self.dateTimeEdit.minimumDateTime()
        self.currentMinimumDateTime = self.currentMinimumDateTime.addDays(-10)
        self.dateTimeEdit.setMaximumDateTime(self.currentMinimumDateTime)

    #CalendarWidget의 시그널에 연결된 함수들
    def calendarClicked(self):
        print(self.calendarWidget.selectedDate())

    def calendarPageChanged(self):
        self.year = str(self.calendarWidget.yearShown()) + '년'
        self.month = str(self.calendarWidget.monthShown()) + '월'
        self.Date_lb.setText(self.year + " " + self.month)

    def calendarSelectionChanged(self):
        self.selectedDateVar = self.calendarWidget.selectedDate()
        self.Page_lb.setText(self.selectedDateVar.toString())

    #버튼에 연결된 함수들
    def prevMonth(self):
        self.calendarWidget.showPreviousMonth()

    def nextMonth(self):
        self.calendarWidget.showNextMonth()

    def today(self):
        self.calendarWidget.showToday()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
