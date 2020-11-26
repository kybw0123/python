import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
from_class = uic.loadUiType('python_ui.ui')[0]

# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fontSize = 10
        # 버튼에 기능을 연결하는 코드
        self.OK_Button.clicked.connect(self.button1Function)
        self.Cancel_Button.clicked.connect(self.button2Function)
        self.A_group.clicked.connect(self.groupboxRadFunction)
        self.B_group.clicked.connect(self.groupboxRadFunction)
        self.C_group.clicked.connect(self.groupboxRadFunction)
        self.D_group.clicked.connect(self.groupboxRadFunction)

        # GroupBox 안에 있는 CheckBox에 기능 연결
        self.A_group_check.stateChanged.connect(self.groupchkFunction)
        self.B_group_check.stateChanged.connect(self.groupchkFunction)
        self.C_group_check.stateChanged.connect(self.groupchkFunction)
        self.D_group_check.stateChanged.connect(self.groupchkFunction)

        # 텍스트 박스 옆에 있는 버튼들에 대한 기능 연결
        self.Print_bt.clicked.connect(self.printTextFunction)
        self.SetText_bt.clicked.connect(self.changeTextFunction)
        self.AppendText_bt.clicked.connect(self.appendTextFunction)
        self.Clear_bt.clicked.connect(self.clearTextFunction)

        # LineEdit 버튼들에 대한 기능을 할당하는 코드
        self.ChangeLabel.textChanged.connect(self.lineeditTextFunction)
        self.ChangeLabel.returnPressed.connect(self.printTextFunction)
        self.ChangeLabel_bt.clicked.connect(self.changeTextFunction)

        # TextEdit와 관련된 버튼에 기능 연결
        self.PrintText_bt.clicked.connect(self.printTextEdit)
        self.ClearText_bt.clicked.connect(self.clearTextEdit)
        self.SetFont_bt.clicked.connect(self.setFont)
        self.SetItalic_bt.clicked.connect(self.fontItalic)
        self.FontRed_bt.clicked.connect(self.fontColorRed)
        self.FontUp_bt.clicked.connect(self.fontSizeUp)
        self.FontDown_bt.clicked.connect(self.fontSizeDown)

        # ComboBox 관련 버튼에 기능 연결
        self.comboBox.currentIndexChanged.connect(self.comboBoxFunction)

        # 버튼에 기능 연결
        self.PrintItem_bt.clicked.connect(self.printComboBoxItem)
        self.ClearItem_bt.clicked.connect(self.clearComboBoxItem)
        self.AddItem_bt.clicked.connect(self.addComboBoxItem)
        self.DeleteItem_bt.clicked.connect(self.deleteComboBoxItem)

        # SpinBox에 대한 기능 연결
        self.spinBox.valueChanged.connect(self.printValue)
        self.ShowInfo_bt.clicked.connect(self.printInfo)
        self.Change_bt.clicked.connect(self.changeRangeStep)

        # DoubleSpinBox에 대한 기능 연결
        self.doubleSpinBox.valueChanged.connect(self.printDoubleValue)
        self.ShowInfo2_bt.clicked.connect(self.printDoubleInfo)
        self.Change2_bt.clicked.connect(self.doublechangeRangeStep)

    # OK 버튼 연결
    def button1Function(self):
        print('OK 버튼')

# Cancel버튼 연결
    def button2Function(self):
        print('Cancel 버튼')

# Groupbox버튼 연결
    def groupboxRadFunction(self):
        if self.A_group.isChecked() : print('A_group Checked')
        elif self.B_group.isChecked() : print('B_group Checked')
        elif self.C_group.isChecked() : print('C_group Checked')
        elif self.D_group.isChecked() : print('D_group Checked')

# Groupcheckbox버튼 연결
    def groupchkFunction(self):
        if self.A_group_check.isChecked(): print('A_group_check isChecked')
        if self.B_group_check.isChecked(): print('B_group_check isChecked')
        if self.C_group_check.isChecked(): print('C_group_check isChecked')
        if self.D_group_check.isChecked(): print('D_group_check isChecked')

    def printTextFunction(self):
        # self.Textbrowser이름.toPlainText()
        # Textbrowser에 있는 글자를 가져오는 메서드
        print(self.Textbrowser.toPlainText())

    def changeTextFunction(self):
        #self.Textbrowser이름.setPlainText()
        #Textbrowser에 있는 글자를 가져오는 메서드
        self.Textbrowser.setPlainText('This is Textbrowser - Change Text')

    def appendTextFunction(self):
        #self.Textbrowser이름.append()
        #Textbrowser에 있는 글자를 가져오는 메서드
        self.Textbrowser.append("Append Text")

    def clearTextFunction(self):
        #self.Textbrowser이름.clear()
        #Textbrowser에 있는 글자를 지우는 메서드
        self.Textbrowser.clear()

    def lineeditTextFunction(self):
        self.lbl_textHere.setText(self.ChangeLabel.text())

    def printTextFunction(self):
        #self.lineedit이름.text()
        #Lineedit에 있는 글자를 가져오는 메서드
        print(self.ChangeLabel.text())

    def changeTextFunction(self):
        #self.lineedit이름.setText('String')
        #Lineedit의 글자를 바꾸는 메서드
        self.ChangeLabel.setText("Change Text")

    def printTextEdit(self):
        print(self.Textbrowser.toPlainText())

    def clearTextEdit(self):
        self.Textbrowser.clear()

    def setFont(self):
        fontvar = QFont('Apple SD Gothic Neo', 15)
        self.Textbrowser.setCurrentFont(fontvar)

    def fontItalic(self):
        self.Textbrowser.setFontItalic(True)

    def fontColorRed(self):
        colorvar = QColor(255, 0, 0)
        self.Textbrowser.setTextColor(colorvar)


    def fontSizeUp(self):
        self.fontSize = self.fontSize + 1
        self.Textbrowser.setFontPointSize(self.fontSize)

    def fontSizeDown(self):
        self.fontSize = self.fontSize - 1
        self.Textbrowser.setFontPointSize(self.fontSize)

    def syncComboBox(self):
        for i in range(0,self.comboBox.count()):
            self.comboBox2.addItem(self.comboBox.itemText(i))

    def comboBoxFunction(self):
        self.Display_lb.setText(self.comboBox.currentText())

    def clearComboBoxItem(self):
        self.comboBox.clear()
        self.comboBox2.clear()

    def printComboBoxItem(self):
        print(self.comboBox.currentText())

    def addComboBoxItem(self):
        self.comboBox.addItem(self.AddCombobox_edit.text())
        self.comboBox2.addItem(self.AddCombobox_edit.text())
        print("Item Added")

    def deleteComboBoxItem(self):
        self.delidx = self.comboBox2.currentIndex()
        self.comboBox.removeItem(self.delidx)
        self.comboBox2.removeItem(self.delidx)
        print("Item Deleted")

    def printValue(self):
        print(self.spinBox.value())

    def printInfo(self):
        print("Maximum value is", self.spinBox.maximum())
        print("Minimum value is", self.spinBox.minimum())
        print('Step Size is', self.spinBox.singleStep())

    def changeRangeStep(self):
        self.spinBox.setRange(0,1000)
        self.spinBox.setSingleStep(10)

    def printDoubleValue(self):
        print(self.doubleSpinBox.value())

    def printDoubleInfo(self):
        print("Maximum value is", self.doubleSpinBox.maximum())
        print("Minimum value is", self.doubleSpinBox.minimum())
        print('Step Size is', self.doubleSpinBox.singleStep())

    def doublechangeRangeStep(self):
        self.doubleSpinBox.setRange(0,1000)
        self.doubleSpinBox.setSingleStep(1.5)







if __name__ == "__main__" :
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowsClass의 인스턴스 생성
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()

