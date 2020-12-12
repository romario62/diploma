# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rega.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_forrmRegister(object):
    def setupUi(self, forrmRegister):
        forrmRegister.setObjectName("formRegister")
        forrmRegister.resize(426, 364)
        self.horizontalLayoutWidget = QtWidgets.QWidget(forrmRegister)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(240, 280, 171, 80))
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
        self.gridLayoutWidget = QtWidgets.QWidget(forrmRegister)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(120, 50, 201, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineLogin = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineLogin.setObjectName("lineLogin")
        self.gridLayout.addWidget(self.lineLogin, 0, 1, 1, 1)
        self.linePass = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.linePass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.linePass.setObjectName("linePass")
        self.gridLayout.addWidget(self.linePass, 1, 1, 1, 1)
        self.lineMail = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineMail.setObjectName("lineMail")
        self.gridLayout.addWidget(self.lineMail, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.retranslateUi(forrmRegister)
        QtCore.QMetaObject.connectSlotsByName(forrmRegister)

    def retranslateUi(self, forrmRegister):
        _translate = QtCore.QCoreApplication.translate
        forrmRegister.setWindowTitle(_translate("forrmRegister", "Окно регистрации"))
        self.pushButton_2.setText(_translate("forrmRegister", "Регистрация"))
        self.pushButton.setText(_translate("forrmRegister", "Отмена"))
        self.label.setText(_translate("forrmRegister", "Логин"))
        self.label_2.setText(_translate("forrmRegister", "Пароль"))
        self.label_4.setText(_translate("forrmRegister", "E-mail"))
