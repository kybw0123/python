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
        # 버튼에 기능을 연결하는 코드
        self.OK_Button.clicked.connect(self.button1Function)
        self.Cancel_Button.clicked.connect(self.button2Function)
        self.A_group.clicked.connect(self.groupboxRadFunction)
        self.B_group.clicked.connect(self.groupboxRadFunction)
        self.C_group.clicked.connect(self.groupboxRadFunction)
        self.D_group.clicked.connect(self.groupboxRadFunction)


    def button1Function(self):
        print('OK 버튼')
    def button2Function(self):
        print('Cancel 버튼')
    def groupboxRadFunction(self):
        if self.A_group.isChecked() : print('A_group Chekced')
        elif self.B_group.isChecked() : print('B_group Chekced')
        elif self.C_group.isChecked() : print('C_group Chekced')
        elif self.D_group.isChecked() : print('D_group Chekced')




if __name__ == "__main__" :
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowsClass의 인스턴스 생성
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
