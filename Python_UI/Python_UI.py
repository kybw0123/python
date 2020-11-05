import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
from_class = uic.loadUiType('python_ui.ui')[0]

# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
<<<<<<< HEAD
        # 버튼에 기능을 연결하는 코드
        self.OK_Button.clicked.connect(self.button1Function)
        self.Cancel_Button.clicked.connect(self.button2Function)

    def button1Function(self):
        print('OK 버튼')
    def button2Function(self):
        print('Cancel 버튼')

=======
>>>>>>> 5e2af573da7988bdb1e8a047f0180238b05d34d8

if __name__ == "__main__" :
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowsClass의 인스턴스 생성
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
