# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 477)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_chckPrx = QtWidgets.QLabel(self.centralwidget)
        self.label_chckPrx.setObjectName("label_chckPrx")
        self.verticalLayout.addWidget(self.label_chckPrx)
        self.textBrowser_chckPrx = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_chckPrx.setObjectName("textBrowser_chckPrx")
        self.verticalLayout.addWidget(self.textBrowser_chckPrx)
        self.label_wrkPrx = QtWidgets.QLabel(self.centralwidget)
        self.label_wrkPrx.setObjectName("label_wrkPrx")
        self.verticalLayout.addWidget(self.label_wrkPrx)
        self.textBrowser_wrkPrx = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_wrkPrx.setObjectName("textBrowser_wrkPrx")
        self.verticalLayout.addWidget(self.textBrowser_wrkPrx)
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")
        self.verticalLayout.addWidget(self.pushButton_start)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_txtStat = QtWidgets.QLabel(self.centralwidget)
        self.label_txtStat.setObjectName("label_txtStat")
        self.verticalLayout.addWidget(self.label_txtStat)
        self.label_stat = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_stat.setFont(font)
        self.label_stat.setText("")
        self.label_stat.setObjectName("label_stat")
        self.verticalLayout.addWidget(self.label_stat)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_chckPrx.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Proxies to check</span></p></body></html>"))
        self.label_wrkPrx.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Working proxies</span></p></body></html>"))
        self.pushButton_start.setText(_translate("MainWindow", "Start "))
        self.label_txtStat.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">STATUS:</span></p></body></html>"))

