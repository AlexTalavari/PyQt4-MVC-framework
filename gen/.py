# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/MainView.ui'
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

class Ui_MainView(object):
    def setupUi(self, MainView):
        MainView.setObjectName(_fromUtf8("MainView"))
        MainView.resize(163, 119)
        self.centralwidget = QtGui.QWidget(MainView)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.btnExport = QtGui.QPushButton(self.centralwidget)
        self.btnExport.setObjectName(_fromUtf8("btnExport"))
        self.verticalLayout_2.addWidget(self.btnExport)
        self.btnCsv = QtGui.QPushButton(self.centralwidget)
        self.btnCsv.setObjectName(_fromUtf8("btnCsv"))
        self.verticalLayout_2.addWidget(self.btnCsv)
        self.btnMachine = QtGui.QPushButton(self.centralwidget)
        self.btnMachine.setObjectName(_fromUtf8("btnMachine"))
        self.verticalLayout_2.addWidget(self.btnMachine)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainView.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainView)
        QtCore.QMetaObject.connectSlotsByName(MainView)

    def retranslateUi(self, MainView):
        MainView.setWindowTitle(_translate("MainView", "MainWindow", None))
        self.btnExport.setText(_translate("MainView", "Export To Mysql", None))
        self.btnCsv.setText(_translate("MainView", "Create CSVs", None))
        self.btnMachine.setText(_translate("MainView", "Machine Learning", None))

