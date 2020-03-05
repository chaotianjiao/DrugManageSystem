# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class change_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(701, 474)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input_price_label = QtWidgets.QLabel(self.centralwidget)
        self.input_price_label.setGeometry(QtCore.QRect(190, 180, 191, 51))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(24)
        self.input_price_label.setFont(font)
        self.input_price_label.setObjectName("input_price_label")
        self.number_input_label = QtWidgets.QLabel(self.centralwidget)
        self.number_input_label.setGeometry(QtCore.QRect(190, 300, 191, 51))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(24)
        self.number_input_label.setFont(font)
        self.number_input_label.setObjectName("number_input_label")
        self.price_input = QtWidgets.QLineEdit(self.centralwidget)
        self.price_input.setGeometry(QtCore.QRect(400, 180, 191, 51))
        self.price_input.setObjectName("price_input")
        self.number_input = QtWidgets.QLineEdit(self.centralwidget)
        self.number_input.setGeometry(QtCore.QRect(400, 300, 191, 51))
        self.number_input.setObjectName("number_input")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(240, 70, 221, 71))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(30)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.ok_btn = QtWidgets.QPushButton(self.centralwidget)
        self.ok_btn.setGeometry(QtCore.QRect(220, 390, 91, 31))
        self.ok_btn.setObjectName("ok_btn")
        self.cancel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_btn.setGeometry(QtCore.QRect(440, 390, 91, 31))
        self.cancel_btn.setObjectName("cancel_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 701, 23))
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
        self.input_price_label.setText(_translate("MainWindow", "输入新单价："))
        self.number_input_label.setText(_translate("MainWindow", "输入新数量："))
        self.title.setText(_translate("MainWindow", "初始化"))
        self.ok_btn.setText(_translate("MainWindow", "确定"))
        self.cancel_btn.setText(_translate("MainWindow", "取消"))
