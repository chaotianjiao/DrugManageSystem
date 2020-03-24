import sys

from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_code.buy_plan_ui import Buy_Plan_MainWindow

class BuyPlanMainWindow(QMainWindow, Buy_Plan_MainWindow):
    def __init__(self):
        super(BuyPlanMainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('采购计划制定界面')
        limit_int = QIntValidator()
        limit_int.setRange(1, 1000)
        limit_double = QDoubleValidator()
        limit_double.setRange(0.01, 999.99)
        limit_double.setDecimals(2)
        limit_double.StandardNotation = 1
        self.price_input_1.setValidator(limit_int)
        self.price_input_2.setValidator(limit_int)
        self.price_input_3.setValidator(limit_int)
        self.price_input_4.setValidator(limit_int)
        self.number_input_1.setValidator(limit_double)
        self.number_input_2.setValidator(limit_double)
        self.number_input_3.setValidator(limit_double)
        self.number_input_4.setValidator(limit_double)



# 以下为测试代码，可以不用管
if __name__ == '__main__':
    app = QApplication(sys.argv)
    buy_plan_window = BuyPlanMainWindow()
    buy_plan_window.show()
    sys.exit(app.exec())



