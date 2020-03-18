import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_code.sell_ui import sell_MainWindow

class Sell_MainWindow(QMainWindow, sell_MainWindow):
    def __init__(self):
        super(Sell_MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('销售界面')
        self.other()

    def other(self):
        # 连接销售及退药按钮
        self.sell_and_return_btn.clicked.connect(self.sell_and_return_btn_click)
        # 连接库存管理按钮
        self.store_manage_btn.clicked.connect(self.store_manage_btn_click)
        # 连接销售查询按钮
        self.sell_information_btn.clicked.connect(self.sell_information_btn_click)
        # 连接退药查询按钮
        self.return_query_btn.clicked.connect(self.return_query_btn_click)
        # 连接药品调拨按钮
        self.drug_allocate_btn.clicked.connect(self.drug_allocate_btn_click)
        # 连接药品拆分按钮
        self.drug_split_btn.clicked.connect(self.drug_split_btn_click)
        # 连接销售账目管理按钮
        self.sell_bill_manage_btn.clicked.connect(self.sell_bill_manage_btn_click)
        # 连接打折优惠按钮
        self.reduce_price_btn.clicked.connect(self.reduce_price_btn_click)
        # 连接促销按钮
        self.on_sale_btn.clicked.connect(self.on_sale_btn_click)

    def sell_and_return_btn_click(self):
        pass

    def store_manage_btn_click(self):
        pass

    def sell_information_btn_click(self):
        pass

    def return_query_btn_click(self):
        pass

    def drug_allocate_btn_click(self):
        pass

    def drug_split_btn_click(self):
        pass

    def sell_bill_manage_btn_click(self):
        pass

    def reduce_price_btn_click(self):
        pass

    def on_sale_btn_click(self):
        pass

    
# 以下为测试代码，可以不用管
if __name__ == '__main__':
    app = QApplication(sys.argv)
    sell_ui = Sell_MainWindow()
    sell_ui.show()
    sys.exit(app.exec())

