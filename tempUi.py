# -*- coding: utf-8 -*-
# GUI Temp Monitor - This project expands upon my terminal based temp monitor by introducing a gui using PYQT5
#
# Created by: DevSeanD
#



from PyQt5 import QtCore, QtGui, QtWidgets

import os
from os import system

def fetchCpuTemp():
    os.system("sensors | grep Core > tempSave.txt")

    f = open("tempSave.txt", "r")
    content_list = [line.rstrip('\n') for line in f]
    f.close()

    return content_list

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(375, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(27, 10, 401, 160))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 446, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
    
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        tempList = fetchCpuTemp()
        tempString = '\n'.join([str(elm) for elm in tempList])
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GUI Temp Monitor"))
        self.label.setText(_translate("MainWindow", tempString))

def updateLabel():
    tempList = fetchCpuTemp()
    tempString = '\n'.join([str(elm) for elm in tempList])
    ui.label.setText(tempString)        

if __name__ == "__main__":
    import sys
    import time
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    timer = QtCore.QTimer()
    timer.timeout.connect(updateLabel)
    timer.start(3000)

    sys.exit(app.exec_())
