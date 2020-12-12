# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bronir1.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Bronir(object):
    def setupUi(self, Bronir):
        Bronir.setObjectName("Bronir")
        Bronir.resize(597, 384)
        self.tableWidget = QtWidgets.QTableWidget(Bronir)
        self.tableWidget.setGeometry(QtCore.QRect(140, 90, 351, 191))
        self.tableWidget.setObjectName("columnView")
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(6)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Bronir)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(360, 300, 201, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(Bronir)
        self.label.setGeometry(QtCore.QRect(260, 60, 131, 21))
        self.label.setObjectName("label")

        self.retranslateUi(Bronir)
        QtCore.QMetaObject.connectSlotsByName(Bronir)

    def retranslateUi(self, Bronir):
        _translate = QtCore.QCoreApplication.translate
        Bronir.setWindowTitle(_translate("Bronir", "Form"))
        self.pushButton_2.setText(_translate("Bronir", "Забронировать"))
        self.pushButton.setText(_translate("Bronir", "Назад"))
        self.label.setText(_translate("Bronir", "Найденные варианты"))
