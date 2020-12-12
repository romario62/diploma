# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Search(object):
    def setupUi(self, Search):
        Search.setObjectName("Search")
        Search.resize(471, 326)
        self.verticalLayoutWidget = QtWidgets.QWidget(Search)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(280, 240, 121, 61))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.gridLayoutWidget = QtWidgets.QWidget(Search)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(120, 80, 231, 81))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditFrom = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEditFrom.setObjectName("lineEditFrom")
        self.gridLayout.addWidget(self.lineEditFrom, 0, 1, 1, 1)
        self.lineEditTo = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEditTo.setObjectName("lineEditTo")
        self.gridLayout.addWidget(self.lineEditTo, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Search)
        self.label_3.setGeometry(QtCore.QRect(200, 30, 81, 31))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Search)
        QtCore.QMetaObject.connectSlotsByName(Search)

    def retranslateUi(self, Search):
        _translate = QtCore.QCoreApplication.translate
        Search.setWindowTitle(_translate("Search", "Поиск билетов"))
        self.pushButton.setText(_translate("Search", "Выход"))
        self.label_2.setText(_translate("Search", "Откуда"))
        self.label.setText(_translate("Search", "Куда"))
        self.pushButton_3.setText(_translate("Search", "Поиск"))
        self.label_3.setText(_translate("Search", "Поиск билетов"))
