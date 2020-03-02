import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_code.buy_ui import buy_MainWindow

class Buy_MainWindow(QMainWindow, buy_MainWindow):
    def __init__(self):
        super(Buy_MainWindow,self).__init__()
        self.setupUi(self)
    # def initUI(self):
    #     pass


# 以下为测试代码，可以不用管
if __name__ =='__main__':
    app = QApplication(sys.argv)
    buy_ui = Buy_MainWindow()
    buy_ui.show()
    sys.exit(app.exec())
