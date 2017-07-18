# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox

from user_service import UserPassword


class Ui_Login(QWidget):
    # setup the login window.
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.setWindowTitle("Login")
        self.login = Login
        # this is for the size of the window.
        Login.resize(1000, 600)
        Login.setMinimumSize(QtCore.QSize(1000, 600))
        Login.setMaximumSize(QtCore.QSize(1000, 600))
        # this is for the button boxes
        self.buttonBox = QtWidgets.QDialogButtonBox(Login)
        self.buttonBox.setGeometry(QtCore.QRect(390, 490, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.textBrowser = QtWidgets.QTextBrowser(Login)
        self.textBrowser.setGeometry(QtCore.QRect(440, 310, 411, 221))
        self.textBrowser.setStyleSheet("background-color: rgb(0, 255, 255);\n"
                                       "background-color: rgb(91, 185, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Login)
        self.pushButton.setGeometry(QtCore.QRect(-10, 0, 1021, 621))
        self.pushButton.setText("")
        # this is for setting the background
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Qt/sources/background.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(1000, 600))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Login)
        self.lineEdit.setGeometry(QtCore.QRect(540, 370, 241, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Login)
        self.lineEdit_2.setEchoMode(2)
        self.lineEdit_2.setGeometry(QtCore.QRect(540, 430, 241, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton.raise_()
        self.textBrowser.raise_()
        self.buttonBox.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()

        self.retranslateUi(Login)
        self.buttonBox.accepted.connect(self.printText)
        self.buttonBox.rejected.connect(self.clearText)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def printText(self):
        text = self.lineEdit.text()
        text1 = self.lineEdit_2.text()

        if text == '' or text1 == '':
            QMessageBox.information(self, "Empty Text",
                                    "Please enter the letter.")
        else:
            username = str(text)
            password = str(text1)
            return_value = UserPassword.checkPassword(self, username, password)
            if return_value:
                self.login.hide()
            else:
                QMessageBox.information(self, "Error",
                                        "Incorrect Username or Password.")
        return text

    def clearText(self):
        text = self.lineEdit.text()
        text1 = self.lineEdit_2.text()

        if text == '' or text1 == '':
            return
        else:
            self.lineEdit.clear()
            self.lineEdit_2.clear()

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Dialog"))
        self.textBrowser.setHtml(_translate("Login",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600;\">登录</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">用户名</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">密码</span></p></body></html>"))
