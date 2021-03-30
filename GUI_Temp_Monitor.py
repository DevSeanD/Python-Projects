#!/usr/bin/python

# -*- coding: utf-8 -*-
# GUI Temp Monitor - This project expands upon my terminal based temp monitor by introducing a gui using PYQT5
#
# Created by: DevSeanD
#



from PyQt5 import QtCore, QtGui, QtWidgets

import os
from os import system
import time
import sys

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
    ui.label.setStyleSheet("color: white")
    ui.label.setText(tempString)        

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setStyleSheet("background-color: black")
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.label.setStyleSheet("color: white")
    MainWindow.show()
   
    timer = QtCore.QTimer()
    timer.timeout.connect(updateLabel)
    
    if(len(sys.argv) == 1):
        timer.start(3000) 
    if(len(sys.argv) != 1) and (str(sys.argv[1]) == "-e"):
        timer.start(10000)

    sys.exit(app.exec_())
