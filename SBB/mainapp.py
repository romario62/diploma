__author__ = 'velic'
# -*- coding: utf-8 -*-
import re
import random
import hashlib
import sys
import psycopg2
from psycopg2 import sql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLineEdit
from login import Ui_Login
from rega import Ui_forrmRegister
from bronir import Ui_Bronir
from bronirr import Ui_Bronirr
from search import Ui_Search
import time
def hashpass(passw): #принимает на вход пароль и шифрует в мд5
    password = str(passw)
    bpass = bytes(password, 'utf8')
    hash_object = hashlib.md5(bpass)
    md = hash_object.hexdigest()
    return md
class searchWindow(QtWidgets.QMainWindow, Ui_Search):
    def __init__(self):
        super().__init__()
        self.bronWin = None
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.openBron)

    def openBron(self):
        cityFrom = self.lineEditFrom.text()
        cityTo = self.lineEditTo.text()
        if not self.bronWin:
            self.bronWin = bronWindow(cityTo,cityFrom)
        self.bronWin.show()


class regWindow(QtWidgets.QMainWindow, Ui_forrmRegister):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.newUser)
        self.pushButton.clicked.connect(self.close)
    def showMessageBox(self, title, message):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()
    def checkStrongPassword(self, password): #проверка сложности пароля при регистрации
        passw = list(password)
        lower = re.search(r"[a-z]", password)
        upper = re.search(r"[A-Z]", password)
        number = re.search(r"[0-9]", password)
        chars = re.search(r"\W", password)
        if len(passw) >= 8 and lower and upper and number and chars:
            return 1
        else:
            return 0

    def newUser(self):
        login = str(self.lineLogin.text())
        passw = str(self.linePass.text())
        mail = str(self.lineMail.text())
        flag = self.checkStrongPassword(passw)
        if flag == 1:
            hpass = hashpass(passw)
            conn = psycopg2.connect(dbname='t', user='postgres', password='1234', host='localhost', port='5432')
            with conn.cursor() as cursor:
                conn.autocommit = True
                cursor.execute('select login from users')
                users = cursor.fetchall()
                if login in users:
                    err = 'логин существует'
                    QMessageBox.warning(self, "Внимание", "Регистрация неуспешна: "+err)
                else:
                    values = [
                        (login, hpass, mail)
                    ]
                    insert = sql.SQL('INSERT INTO users VALUES {}').format(
                        sql.SQL(',').join(map(sql.Literal, values))
                    )
                    cursor.execute(insert)
                    QMessageBox.warning(self, "Внимание", "Регистрация успешна")
                    self.close()
        if flag == 0:
            QMessageBox.warning(self,'Внимание', 'Пароль не соответствует требованиям')

class bronWindow(QtWidgets.QMainWindow, Ui_Bronir):
    def __init__(self, cityTo, cityFrom):
        super().__init__()
        self.setupUi(self)
        self.bronWinn = None
        self.pushButton_2.clicked.connect(self.openBronn)
        conn = psycopg2.connect(dbname='t', user='postgres', password='1234', host='localhost', port='5432')
        with conn.cursor() as cursor:
            cursor.execute("SELECT * from tickets where cityfrom = %s and cityto = %s",(cityFrom,cityTo))
            row = cursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(row):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


    def openBronn(self):
        flightId = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
        if not self.bronWinn:
            self.bronWinn = bronWindoww(flightId)
        self.bronWinn.show()


class bronWindoww(QtWidgets.QMainWindow, Ui_Bronirr):
    def __init__(self, flightId):
        super().__init__()
        self.setupUi(self)
        f = flightId
        self.pushButton_2.clicked.connect(self.bronirovanie(f))

    def bronirovanie(self, f):
        f = f
        ticket = random.choice(range(1,1000,1))
        name = self.lineEdit.text()
        cellPhone = self.lineEdit_2.text()
        seat = self.lineEdit_3.text()
        passport = self.lineEdit_4.text()
        try:
            conn = psycopg2.connect(dbname='t', user='postgres', password='1234', host='localhost', port='5432')
            with conn.cursor() as cursor:
                cursor.execute("insert into passengers values (%s,%s,%s)",(passport,name,cellPhone))
                cursor.execute("insert into ticket values ( %s, 'b777', %s, 8000, %s, %s)",(ticket,seat,passport,f))
            QMessageBox.warning(self,'Внимание','Забронировано')
        except Exception as l:
            print(l)
            QMessageBox.warning(self,'Внимание','Произошла ошибка')

class LoginWindow(QtWidgets.QMainWindow, Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.regWin = None
        self.searchWin = None

        self.pushButton_2.clicked.connect(self.openReg)
        self.pushButton.clicked.connect(self.onlog) #вернуть
        #self.pushButton.clicked.connect(self.openSearch)
    def showMessageBox(self, title, message):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()
    def openReg(self):
        if not self.regWin:
            self.regWin = regWindow()
        self.regWin.show()

    def openSearch(self):
        if not self.searchWin:
            self.searchWin = searchWindow()
        self.searchWin.show()

    def onlog(self):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        hpass = hashpass(password)
        conn = psycopg2.connect(dbname='t', user='postgres', password='1234', host='localhost', port='5432')
        with conn.cursor() as cursor:
            conn.autocommit = True
            cursor.execute('SELECT * from users where login = %s and passw = %s',(login,hpass))
            row = cursor.fetchall()
            if len(row):
                self.openSearch()
                self.close()
            else:
                self.pushButton.setEnabled(False)
                self.showMessageBox( 'Внимание!', 'Неверный логин или пароль. Ожидайте 5 секунд')
                time.sleep(5)
                self.pushButton.setEnabled(True)


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = LoginWindow()
    form.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()