import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_code.sell_ui import sell_MainWindow

class Sell_MainWindow(QMainWindow, sell_MainWindow):
    def __init__(self):
        super(Sell_MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('销售界面')

# 以下为测试代码，可以不用管
if __name__ == '__main__':
    app = QApplication(sys.argv)
    sell_ui = Sell_MainWindow()
    sell_ui.show()
    sys.exit(app.exec())

