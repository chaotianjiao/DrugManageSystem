import sys

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMainWindow, QApplication, QAbstractItemView, QTableView, QMessageBox, QAction, QInputDialog
from ui_code.sell_ui import sell_MainWindow
import pymysql
import decimal

# 打折函数，采用装饰器方式调用，如果需要传参，就用三层def


def discount(func):
    def wrapper(self, *args):
        discount, ok = QInputDialog.getDouble(
            self, "输入折扣", "范围0.01~0.99", min=0.01, max=0.99, decimals=2)
        discount = decimal.Decimal(discount)
        if ok:
            sql = 'select * from bill_information_table '
            self.cursor.execute(sql)
            all_data = self.cursor.fetchall()
            self.data_length = len(all_data)
            self.model = QStandardItemModel(self.data_length + 1, 4)
            self.model.setHorizontalHeaderLabels(['药品名称', '价格', '数量', '总价'])
            for number in range(self.data_length):
                drug_name_show = QStandardItem(
                    str(all_data[number]['drug_name']))
                price_show = QStandardItem(
                    str(round(all_data[number]['price'] * discount, 2)))
                number_show = QStandardItem(str(all_data[number]['number']))
                total_show = QStandardItem(str(all_data[number]['total']))
                self.model.setItem(number, 0, drug_name_show)
                self.model.setItem(number, 1, price_show)
                self.model.setItem(number, 2, number_show)
                self.model.setItem(number, 3, total_show)

            sql_total = 'select sum(number), sum(total) from bill_information_table'
            self.cursor.execute(sql_total)
            data_2 = self.cursor.fetchall()
            total_number = QStandardItem(str(data_2[0]['sum(number)']))
            total_price = QStandardItem(
                str(round(data_2[0]['sum(total)'] * discount, 2)))
            self.model.setItem(self.data_length, 0, QStandardItem('合计'))
            self.model.setItem(self.data_length, 2, total_number)
            self.model.setItem(self.data_length, 3, total_price)
            self.tableView.setModel(self.model)
    return wrapper


# 销售查询函数，同样采用装饰器定义以减少代码行数
def query(fuction_name):
    def wrapper(self):
        sql = 'select * from bill_information_table '
        self.cursor.execute(sql)
        all_data = self.cursor.fetchall()
        self.data_length = len(all_data)
        self.model = QStandardItemModel(self.data_length + 1, 4)
        self.model.setHorizontalHeaderLabels(['药品名称', '价格', '数量', '总价'])
        for number in range(self.data_length):
            drug_name_show = QStandardItem(str(all_data[number]['drug_name']))
            price_show = QStandardItem(str(all_data[number]['price']))
            number_show = QStandardItem(str(all_data[number]['number']))
            total_show = QStandardItem(str(all_data[number]['total']))
            self.model.setItem(number, 0, drug_name_show)
            self.model.setItem(number, 1, price_show)
            self.model.setItem(number, 2, number_show)
            self.model.setItem(number, 3, total_show)

        sql_total = 'select sum(number), sum(total) from bill_information_table'
        self.cursor.execute(sql_total)
        data_2 = self.cursor.fetchall()
        total_number = QStandardItem(str(data_2[0]['sum(number)']))
        total_price = QStandardItem(str(data_2[0]['sum(total)']))
        self.model.setItem(self.data_length, 0, QStandardItem('合计'))
        self.model.setItem(self.data_length, 2, total_number)
        self.model.setItem(self.data_length, 3, total_price)
        self.tableView.setModel(self.model)
    return wrapper

class Sell_MainWindow(QMainWindow, sell_MainWindow):
    def __init__(self):
        super(Sell_MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('销售界面')
        self.other()
        self.connect = pymysql.connect(host='localhost',
                                       port=3306,
                                       user='root',
                                       password='fyz98123',
                                       db='pycharm',
                                       charset='utf8',
                                       cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.connect.cursor()
        # 添加退药删除按钮并增加
        tool = self.addToolBar("退药操作")
        self.action = QAction('退药删除', self)
        tool.addAction(self.action)
        tool.actionTriggered[QAction].connect(self.delete)

    def other(self):
        # 连接销售及退药按钮
        self.sell_and_return_btn.clicked.connect(
            self.sell_and_return_btn_click)
        # 连接库存管理按钮
        self.store_manage_btn.clicked.connect(self.store_manage_btn_click)
        # 连接销售查询按钮
        self.sell_information_btn.clicked.connect(
            self.sell_information_btn_click)
        # 连接退药查询按钮
        self.return_query_btn.clicked.connect(self.return_query_btn_click)
        # 连接药品调拨按钮
        self.drug_allocate_btn.clicked.connect(self.drug_allocate_btn_click)
        # 连接药品拆分按钮
        self.drug_split_btn.clicked.connect(self.drug_split_btn_click)
        # 连接销售账目管理按钮
        self.sell_bill_manage_btn.clicked.connect(
            self.sell_bill_manage_btn_click)
        # 连接打折优惠按钮
        self.reduce_price_btn.clicked.connect(self.reduce_price_btn_click)
        # 连接促销按钮
        self.on_sale_btn.clicked.connect(self.on_sale_btn_click)

    @query
    def sell_and_return_btn_click(self):
        # sql = 'select * from bill_information_table '
        # self.cursor.execute(sql)
        # all_data = self.cursor.fetchall()
        # self.data_length = len(all_data)
        # self.model = QStandardItemModel(self.data_length + 1, 4)
        # self.model.setHorizontalHeaderLabels(['药品名称', '价格', '数量', '总价'])
        # for number in range(self.data_length):
        #     drug_name_show = QStandardItem(str(all_data[number]['drug_name']))
        #     price_show = QStandardItem(str(all_data[number]['price']))
        #     number_show = QStandardItem(str(all_data[number]['number']))
        #     total_show = QStandardItem(str(all_data[number]['total']))
        #     self.model.setItem(number, 0, drug_name_show)
        #     self.model.setItem(number, 1, price_show)
        #     self.model.setItem(number, 2, number_show)
        #     self.model.setItem(number, 3, total_show)
        #
        # sql_total = 'select sum(number), sum(total) from bill_information_table'
        # self.cursor.execute(sql_total)
        # data_2 = self.cursor.fetchall()
        # total_number = QStandardItem(str(data_2[0]['sum(number)']))
        # total_price = QStandardItem(str(data_2[0]['sum(total)']))
        # self.model.setItem(self.data_length, 0, QStandardItem('合计'))
        # self.model.setItem(self.data_length, 2, total_number)
        # self.model.setItem(self.data_length, 3, total_price)
        # self.tableView.setModel(self.model)
        # 设置只能选中一行
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        # 设置内容不可编辑
        self.tableView.setEditTriggers(QTableView.NoEditTriggers)
        # 设置只有行选中
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

    # 从数据库中删除逻辑函数
    def delete(self, action):
        if action.text() == '退药删除':
            context = self.tableView.selectionModel().selectedRows()
            if context:
                # 获取选中的行数
                self.index = self.tableView.currentIndex()
                # 拿到行数的药品名
                drug_name = self.index.data()
                #  先插
                sql_1 = 'insert into return_query_table SELECT * from bill_information_table WHERE `drug_name`  = "{}"'.format(
                    drug_name)
                self.cursor.execute(sql_1)
                #  再删
                sql = 'delete from bill_information_table where `drug_name` = "{}"'.format(
                    drug_name)
                self.cursor.execute(sql)
                # 否则插入不进去
                self.connect.commit()
                QMessageBox.about(self, '已删除该行', '重新点击按钮查询总价')

    def store_manage_btn_click(self):
        pass

    @query
    def sell_information_btn_click(self):
        pass

    def return_query_btn_click(self):
        # 查询退药的代码，跟上面的展示代码差不多
        sql = 'select * from return_query_table '
        self.cursor.execute(sql)
        all_data = self.cursor.fetchall()
        self.data_length = len(all_data)
        model = QStandardItemModel(self.data_length + 1, 4)
        model.setHorizontalHeaderLabels(['药品名称', '价格', '数量', '总价'])
        for number in range(self.data_length):
            drug_name_show = QStandardItem(str(all_data[number]['drug_name']))
            price_show = QStandardItem(str(all_data[number]['price']))
            number_show = QStandardItem(str(all_data[number]['number']))
            total_show = QStandardItem(str(all_data[number]['total']))
            model.setItem(number, 0, drug_name_show)
            model.setItem(number, 1, price_show)
            model.setItem(number, 2, number_show)
            model.setItem(number, 3, total_show)

        sql_total = 'select sum(number), sum(total) from return_query_table'
        self.cursor.execute(sql_total)
        data_2 = self.cursor.fetchall()
        total_number = QStandardItem(str(data_2[0]['sum(number)']))
        total_price = QStandardItem(str(data_2[0]['sum(total)']))
        model.setItem(self.data_length, 0, QStandardItem('合计'))
        model.setItem(self.data_length, 2, total_number)
        model.setItem(self.data_length, 3, total_price)
        self.tableView.setModel(model)

    def drug_allocate_btn_click(self):
        pass

    def drug_split_btn_click(self):
        pass

    def sell_bill_manage_btn_click(self):
        pass

    @discount
    def reduce_price_btn_click(self):
        pass

    @discount
    def on_sale_btn_click(self):
        pass


# 以下为测试代码，可以不用管
if __name__ == '__main__':
    app = QApplication(sys.argv)
    sell_ui = Sell_MainWindow()
    sell_ui.show()
    sys.exit(app.exec())
