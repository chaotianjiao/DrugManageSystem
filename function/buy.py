import sys
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog, QMessageBox
from ui_code.buy_ui import buy_MainWindow
import pymysql


class Buy_MainWindow(QMainWindow, buy_MainWindow):
    def __init__(self):
        # 重写父类
        super(Buy_MainWindow, self).__init__()
        # 设置UI
        self.setupUi(self)
        # 加载逻辑函数代码
        self.initUI()
        self.connect = pymysql.connect(host='localhost',
                                       port=3306,
                                       user='root',
                                       password='fyz98123',
                                       db='pycharm',
                                       charset='utf8',
                                       cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.connect.cursor()
        sql = "select * from drug_table where `drug_name` = '{}'".format('阿司匹林')
        self.cursor.execute(sql)
        # 取数据
        data = self.cursor.fetchall()

    def initUI(self):
        # 连接采购药品信息查询按钮
        self.drug_information.clicked.connect(self.drug_information_click)
        # 连接供货商信息查询按钮
        self.supply_information.clicked.connect(self.supply_information_click)
        # 连接采购账目修改按钮
        self.change_purchase_bill.clicked.connect(self.change_purchase_bill_click)
        # 连接采购账目查询按钮
        self.bill_information.clicked.connect(self.bill_information_click)
        # 连接采购计划制定按钮
        self.buy_plan_make.clicked.connect(self.buy_plan_make_click)
        # 连接采购药品入库按钮
        self.procurement_of_drugs.clicked.connect(self.procurement_of_drugs_click)
        # 连接药品结算按钮
        self.drug_settlement.clicked.connect(self.drug_settlement_click)
        # 连接药品采购按钮
        self.drug_purchase.clicked.connect(self.drug_purchase_click)
        # 连接药品退货按钮
        self.drug_return.clicked.connect(self.drug_return_click)

    def drug_information_click(self):
        # 获取药品名
        drug_name, ok = QInputDialog.getText(self, "请输入要查询的药品名", "需要查询的药品名：")
        if ok:
            # 执行查询
            sql = "select * from drug_table where `drug_name` = '{}'".format(drug_name)
            self.cursor.execute(sql)
            # 取数据
            data = self.cursor.fetchall()
            if data:
                # 设置显示模型
                model = QStandardItemModel(4, 1)
                model.setVerticalHeaderLabels((['药品名称', '制造商', '生产时间', '保质期(年)']))
                drug_name_show = QStandardItem(str(data[0]['drug_name']))
                manufacturer_show = QStandardItem(str(data[0]['manufacturer']))
                production_date_show =QStandardItem(str(data[0]['production_date']))
                expiry_date_show = QStandardItem(str(data[0]['expiry_date']))
                model.setItem(0, 0, drug_name_show)
                model.setItem(1, 0, manufacturer_show)
                model.setItem(2, 0, production_date_show)
                model.setItem(3, 0, expiry_date_show)
                self.tableView.setModel(model)
            else:
                QMessageBox.about(self, '没有找到您要查询的药品', '请检查输入')

    def supply_information_click(self):
        pass

    def change_purchase_bill_click(self):
        pass

    def bill_information_click(self):
        pass

    def buy_plan_make_click(self):
        pass

    def procurement_of_drugs_click(self):
        pass

    def drug_settlement_click(self):
        pass

    def drug_purchase_click(self):
        pass

    def drug_return_click(self):
        pass


# 以下为测试代码，可以不用管
if __name__ == '__main__':
    app = QApplication(sys.argv)
    buy_ui = Buy_MainWindow()
    buy_ui.show()
    sys.exit(app.exec())
