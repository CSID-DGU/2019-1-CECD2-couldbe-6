# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Project.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
import time
import subprocess
import S13RNG
from PyQt5 import QtCore, QtGui, QtWidgets
RNGA = S13RNG.S13RNG()
notepad = ("C:\windows\System32\\notepad.exe")


class Ui_RNG(object):
    def setupUi(self, RNG):
        RNG.setObjectName("RNG")
        RNG.setEnabled(True)
        RNG.resize(500, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RNG.sizePolicy().hasHeightForWidth())
        RNG.setSizePolicy(sizePolicy)
        RNG.setMinimumSize(QtCore.QSize(500, 300))
        RNG.setMaximumSize(QtCore.QSize(500, 300))
        RNG.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(RNG)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(500, 300))
        self.centralwidget.setMaximumSize(QtCore.QSize(500, 300))
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 200, 100, 40))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(340, 90, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 411, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(150, 90, 90, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(250, 90, 71, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 125, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 130, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(300, 133, 21, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(315, 130, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 170, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 170, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        RNG.setCentralWidget(self.centralwidget)
        self.pushButton.clicked.connect(self.btn_clicked)
        self.radioButton.setChecked(True)
        self.lineEdit_2.setText("0")
        self.lineEdit_3.setText("23457946398")
        self.lineEdit_4.setText("1")
        self.radioButton.clicked.connect(self.rB_Clicked)
        self.radioButton_2.clicked.connect(self.rB2_clicked)

        self.retranslateUi(RNG)
        QtCore.QMetaObject.connectSlotsByName(RNG)

    def retranslateUi(self, RNG):
        _translate = QtCore.QCoreApplication.translate
        RNG.setWindowTitle(_translate("RNG", "RNG"))
        self.pushButton.setText(_translate("RNG", "Generate"))
        self.label.setText(_translate("RNG", "Random Number Generator"))
        self.label_2.setText(_translate("RNG", "Initial Seed"))
        self.radioButton.setText(_translate("RNG", "Use Default"))
        self.radioButton_2.setText(_translate("RNG", "Manual"))
        self.label_3.setText(_translate("RNG", "Number Range"))
        self.label_4.setText(_translate("RNG", "-"))
        self.label_5.setText(_translate("RNG", "Amount"))

    def rB_Clicked(self):
        self.lineEdit.setEnabled(False)

    def rB2_clicked(self):
        self.lineEdit.setEnabled(True)

    def btn_clicked(self):
        if self.radioButton.isChecked() == True:
            RNGA.rng_seed = time.time()
        elif self.radioButton_2.isChecked() == True:
            if self.lineEdit.text() != "":
                RNGA.rng_seed = int(self.lineEdit.text())
            else:
                QMessageBox.about(self, "Error", "Invaild Seed!")
        if self.lineEdit_2.text() != "" and self.lineEdit_3.text() != "":
            RNGA.rng_modular = int(self.lineEdit_3.text()) - int(self.lineEdit_2.text()) + 1
            count = 0
            goal = int(self.lineEdit_4.text())
            numberlist = []
            while count < goal:
                count = count + 1
                numberlist.append(str(RNGA.random()+int(self.lineEdit_2.text())))
            file = open("number.txt", 'w')
            file.write('\n'.join(numberlist))
            file.close()
            subprocess.run(['notepad','number.txt'])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RNG = QtWidgets.QMainWindow()
    ui = Ui_RNG()
    ui.setupUi(RNG)
    RNG.show()
    sys.exit(app.exec_())
