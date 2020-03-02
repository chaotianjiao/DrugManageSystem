# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from resource import login_rc


class Login_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(803, 608)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(130, 410, 571, 111))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.user_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(18)
        self.user_label.setFont(font)
        self.user_label.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.user_label)
        self.user_input = QtWidgets.QLineEdit(self.layoutWidget)
        self.user_input.setText("")
        self.user_input.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.user_input)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pwd_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(18)
        self.pwd_label.setFont(font)
        self.pwd_label.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.pwd_label)
        self.pwd_input = QtWidgets.QLineEdit(self.layoutWidget)
        self.pwd_input.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.pwd_input)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.login_btn = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(18)
        self.login_btn.setFont(font)
        self.login_btn.setObjectName("pushButton")
        self.pic_label = QtWidgets.QLabel(self.centralwidget)
        self.pic_label.setEnabled(True)
        self.pic_label.setGeometry(QtCore.QRect(150, 90, 521, 281))
        self.pic_label.setStyleSheet("image: url(../picture/timg.jpg);")
        self.pic_label.setText("")
        self.pic_label.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 20, 240, 48))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.user_label.setText(_translate("MainWindow", "用户名："))
        self.pwd_label.setText(_translate("MainWindow", "密  码："))
        self.login_btn.setText(_translate("MainWindow", "登录"))
        self.label.setText(_translate("MainWindow", "敏敏大药房"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Login_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
