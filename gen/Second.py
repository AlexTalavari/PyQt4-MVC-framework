# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Second.ui'
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

class Ui_Second(object):
    def setupUi(self, Second):
        Second.setObjectName(_fromUtf8("Second"))
        Second.resize(800, 600)
        self.centralwidget = QtGui.QWidget(Second)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 190, 85, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        Second.setCentralWidget(self.centralwidget)

        self.retranslateUi(Second)
        QtCore.QMetaObject.connectSlotsByName(Second)

    def retranslateUi(self, Second):
        Second.setWindowTitle(_translate("Second", "MainWindow", None))
        self.pushButton.setText(_translate("Second", "PushButton", None))

