import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_code.buy_plan_ui import Buy_Plan_MainWindow

class BuyPlanMainWindow(QMainWindow, Buy_Plan_MainWindow):
    def __init__(self):
        super(BuyPlanMainWindow, self).__init__()
        self.setupUi(self)


# 以下为测试代码，可以不用管
if __name__ == '__main__':
    app = QApplication(sys.argv)
    buy_plan_window = BuyPlanMainWindow()
    buy_plan_window.show()
    sys.exit(app.exec())



