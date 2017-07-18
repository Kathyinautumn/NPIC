# -*- coding:utf-8 -*-
'''
Frist PyQt5 program
'''
__author__ = 'Qiushui Zhang'

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButton, QLineEdit, QVBoxLayout, \
    QMessageBox, QTextBrowser
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class ShowWindow(QWidget):
    def __init__(self):
        super(ShowWindow, self).__init__()
        self.initUI()

    def initUI(self):
        TextBr = QTextBrowser(self)
        TextBr.setGeometry(400, 300, 300, 100)
        self.inputLabel = QLabel("Input your text")
        self.editLine = QLineEdit()
        self.printButton = QPushButton("Login")
        self.clearButton = QPushButton("Cancel")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Qt/sources/background.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.printButton.clicked.connect(self.printText)
        self.clearButton.clicked.connect(self.clearText)

        inputLayout = QHBoxLayout()
        inputLayout.addWidget(self.inputLabel)
        inputLayout.addWidget(self.editLine)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.printButton)
        buttonLayout.addWidget(self.clearButton)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(inputLayout)
        mainLayout.addLayout(buttonLayout)

        self.setLayout(mainLayout)
        self.setWindowTitle('FristWindow')
        self.show()

    def printText(self):
        text = self.editLine.text()

        if text == '':
            QMessageBox.information(self, "Empty Text",
                                    "Please enter the letter.")
        else:
            QMessageBox.information(self, "Print Success",
                                    "Text: %s" % text)

    def clearText(self):
        text = self.editLine.text()

        if text == '':
            return
        else:
            self.editLine.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ShowWindow()
    sys.exit(app.exec_())
