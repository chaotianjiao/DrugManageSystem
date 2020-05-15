# -*- coding: utf-8 -*-
# @Time : 2020/5/15 10:00
# @Author : Felix
import sys

from ui_code.show_ui import Show_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication


class ShowMainWindow(QMainWindow, Show_MainWindow):
    def __init__(self):
        super(ShowMainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('展示界面')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    change_ui = ShowMainWindow()
    change_ui.show()
    sys.exit(app.exec())
