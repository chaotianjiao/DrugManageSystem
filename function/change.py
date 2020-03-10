import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_code.change_ui import change_MainWindow

class ChangeMainWindow(QMainWindow, change_MainWindow):
    def __init__(self):
        super(ChangeMainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('修改界面')


# 以下为测试代码，可以不用管
if __name__ == '__main__':
    app = QApplication(sys.argv)
    change_ui = ChangeMainWindow()
    change_ui.show()
    sys.exit(app.exec())
