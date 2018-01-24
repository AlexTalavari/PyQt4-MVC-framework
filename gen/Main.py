# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName(_fromUtf8("Main"))
        Main.resize(163, 119)
        self.centralwidget = QtGui.QWidget(Main)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.btnOne = QtGui.QPushButton(self.centralwidget)
        self.btnOne.setObjectName(_fromUtf8("btnOne"))
        self.verticalLayout_2.addWidget(self.btnOne)
        self.btnTwo = QtGui.QPushButton(self.centralwidget)
        self.btnTwo.setObjectName(_fromUtf8("btnTwo"))
        self.verticalLayout_2.addWidget(self.btnTwo)
        self.btnThree = QtGui.QPushButton(self.centralwidget)
        self.btnThree.setObjectName(_fromUtf8("btnThree"))
        self.verticalLayout_2.addWidget(self.btnThree)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2.addLayout(self.verticalLayout)
        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        Main.setWindowTitle(_translate("Main", "MainWindow", None))
        self.btnOne.setText(_translate("Main", "Button 1", None))
        self.btnTwo.setText(_translate("Main", "Button 2", None))
        self.btnThree.setText(_translate("Main", "Button 3", None))

