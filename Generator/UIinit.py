import sys
import time
import subprocess
import S13RNG
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("Project.ui")[0]
RNG = S13RNG.S13RNG()
notepad = ("C:\windows\System32\\notepad.exe")

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked)
        self.radioButton.setChecked(True)
        self.lineEdit_2.setText("0")
        self.lineEdit_3.setText("23457946398")
        self.lineEdit_4.setText("1")
        self.radioButton.clicked.connect(self.rB_Clicked)
        self.radioButton_2.clicked.connect(self.rB2_clicked)

    def rB_Clicked(self):
        self.lineEdit.setEnabled(False)

    def rB2_clicked(self):
        self.lineEdit.setEnabled(True)

    def btn_clicked(self):
        if self.radioButton.isChecked() == True:
            RNG.rng_seed = time.time()
        elif self.radioButton_2.isChecked() == True:
            if self.lineEdit.text() != "":
                RNG.rng_seed = int(self.lineEdit.text())
            else:
                QMessageBox.about(self, "Error", "Invaild Seed!")
        if self.lineEdit_2.text() != "" and self.lineEdit_3.text() != "":
            RNG.rng_modular = int(self.lineEdit_3.text()) - int(self.lineEdit_2.text()) + 1
            count = 0
            goal = int(self.lineEdit_4.text())
            numberlist = []
            while count < goal:
                count = count + 1
                numberlist.append(str(RNG.random()+int(self.lineEdit_2.text())))
            file = open("number.txt", 'w')
            file.write('\n'.join(numberlist))
            file.close()
            subprocess.run(['notepad','number.txt'])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()