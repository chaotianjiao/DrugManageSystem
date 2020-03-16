import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog, QMessageBox, QComboBox, QPushButton
from PyQt5.uic.properties import QtCore

from ui_code.buy_ui import buy_MainWindow
from function.change import ChangeMainWindow
from function.buy_plan import BuyPlanMainWindow
from function.qrcode import QR_MainWindow
import pymysql


class Buy_MainWindow(QMainWindow, buy_MainWindow):
    def __init__(self):
        # 重写父类
        super(Buy_MainWindow, self).__init__()
        # 设置UI
        self.setupUi(self)
        # 加载逻辑函数代码
        self.initUI()
        # 连接数据库
        self.connect = pymysql.connect(host='localhost',
                                       port=3306,
                                       user='root',
                                       password='fyz98123',
                                       db='pycharm',
                                       charset='utf8',
                                       cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.connect.cursor()

    def initUI(self):
        self.setWindowTitle('采购界面')
        # 连接采购药品信息查询按钮
        self.drug_information.clicked.connect(self.drug_information_click)
        # 连接供货商信息查询按钮
        self.supply_information.clicked.connect(self.supply_information_click)
        # 连接采购账目修改按钮
        self.change_purchase_bill.clicked.connect(self.change_purchase_bill_click)
        # 修改界面
        self.change = ChangeMainWindow()
        self.change.ok_btn.clicked.connect(self.change_ok_btn_click)
        self.change.cancel_btn.clicked.connect(self.change_cancel_btn)
        # 连接采购账目查询按钮
        self.bill_information.clicked.connect(self.bill_information_click)
        # 连接采购计划制定按钮
        self.buy_plan_make.clicked.connect(self.buy_plan_make_click)
        # 采购计划制定界面功能函数
        self.buy_plan = BuyPlanMainWindow()
        self.buy_plan.check_btn.clicked.connect(self.buy_plan_check_btn_click)
        self.buy_plan.cancel_btn.clicked.connect(self.buy_plan_cancel_btn_click)
        self.buy_plan.total_label.mousePressEvent = self.buy_plan_total_label_click

        # 连接采购药品入库按钮
        self.procurement_of_drugs.clicked.connect(self.procurement_of_drugs_click)
        # 连接药品结算按钮
        self.drug_settlement.clicked.connect(self.drug_settlement_click)
        self.pay = QR_MainWindow()
        # 连接药品采购按钮
        self.drug_purchase.clicked.connect(self.drug_purchase_click)
        # 连接药品退货按钮
        self.drug_return.clicked.connect(self.drug_return_click)

    def drug_information_click(self):
        # 获取药品名
        drug_name, ok = QInputDialog.getText(self, "输入药品名", "需要查询的药品名：")
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
                production_date_show = QStandardItem(str(data[0]['production_date']))
                expiry_date_show = QStandardItem(str(data[0]['expiry_date']))
                model.setItem(0, 0, drug_name_show)
                model.setItem(1, 0, manufacturer_show)
                model.setItem(2, 0, production_date_show)
                model.setItem(3, 0, expiry_date_show)
                self.tableView.setModel(model)
            else:
                QMessageBox.about(self, '没有找到您要查询的药品', '请检查输入')

    def supply_information_click(self):
        # 获取厂商名
        factory_name, ok = QInputDialog.getText(self, "输入厂商名", "需要查询的厂商名：")
        if ok:
            # 执行查询
            sql = "select * from manufacturer_information_table where `factory_name` = '{}'".format(factory_name)
            self.cursor.execute(sql)
            # 取数据
            data = self.cursor.fetchall()
            if data:
                # 设置显示模型
                model = QStandardItemModel(3, 1)
                model.setVerticalHeaderLabels((['厂商名称', '厂址', '主营产品']))
                factory_name_show = QStandardItem(str(data[0]['factory_name']))
                address_show = QStandardItem(str(data[0]['address']))
                main_business_show = QStandardItem(str(data[0]['main_business']))
                model.setItem(0, 0, factory_name_show)
                model.setItem(1, 0, address_show)
                model.setItem(2, 0, main_business_show)
                self.tableView.setModel(model)
            else:
                QMessageBox.about(self, '没有找到您要查询的厂商', '请检查输入')

    def change_purchase_bill_click(self):
        sql = "select drug_name from bill_information_table"
        self.cursor.execute(sql)
        data_of_drug_name = self.cursor.fetchall()
        # 取出药品名，并展现在下拉菜单中
        drug_list = [data_of_drug_name[i]['drug_name'] for i in range(len(data_of_drug_name))]
        self.change_drug_name, ok = QInputDialog.getItem(self, '选取药品', '药品', drug_list)
        if self.change_drug_name and ok:
            # 显示修改窗口
            self.change.title.setText(self.change_drug_name)
            self.change.show()

    def bill_information_click(self):
        # model不固定，依据数据库中的数据来确定
        sql = 'select max(id) from bill_information_table'
        self.cursor.execute(sql)
        # 这里取表格的行列数
        data = self.cursor.fetchall()
        row = data[0]['max(id)']
        model = QStandardItemModel(int(row) + 1, 4)
        model.setHorizontalHeaderLabels(['药品名称', '单价', '数量','总价'])
        # 这里取展示表的信息
        sql_1 = 'select * from bill_information_table'
        self.cursor.execute(sql_1)
        data_1 = self.cursor.fetchall()
        # 这里还没找到整张表导入的方法，暂时双循环遍历，效率可能有点低下
        for a in range(row):
            # 先取数值出来
            drug_name_show = QStandardItem(str(data_1[a]['drug_name']))
            price_show = QStandardItem(str(data_1[a]['price']))
            number_show = QStandardItem(str(data_1[a]['number']))
            total_show = QStandardItem(str(data_1[a]['total']))
            model.setItem(a, 0, drug_name_show)
            model.setItem(a, 1, price_show)
            model.setItem(a, 2, number_show)
            model.setItem(a, 3, total_show)
        sql_2 = 'select sum(number),sum(total) from bill_information_table'
        self.cursor.execute(sql_2)
        # 这里取总和（单价总和没有意义，所以没有计算）
        data_2 = self.cursor.fetchall()
        total_number = QStandardItem(str(data_2[0]['sum(number)']))
        total_price = QStandardItem(str(data_2[0]['sum(total)']))
        model.setItem(row, 0, QStandardItem('合计'))
        model.setItem(row, 2, total_number)
        model.setItem(row, 3, total_price)
        self.tableView.setModel(model)

    def buy_plan_make_click(self):
        self.buy_plan.show()

    # 执行把计划里的表插入药品表
    def procurement_of_drugs_click(self):
        question = QMessageBox.question(self,'合并确认','是否合并')
        # yes = question.addButton('确定', QMessageBox.YesRole)
        # no = question.addButton('取消', QMessageBox.NoRole)

        # 点击事件已经完成
        if QMessageBox.Yes:
            sql = 'Insert into bill_information_table(`drug_name`,`price`,`number`,`total`) select `drug_name`,`price`,`number`,`total` from plan_table'
            self.cursor.execute(sql)
            self.connect.commit()
            QMessageBox.about(self, '完成', '合并完成')
        else:
            question.close()

    def drug_settlement_click(self):
        self.pay.show()

    def drug_purchase_click(self):
        pass

    def drug_return_click(self):
        pass

    def change_ok_btn_click(self):
        # 获取新输入
        new_price = self.change.price_input.text()
        new_number = self.change.number_input.text()
        try:
            float(new_price)
            int(new_number)
            # 修改数据库
            sql = 'UPDATE bill_information_table set `price` = "{}",`number` = "{}",`total`=`price`*`number` where `drug_name`="{}"'.format(
                new_price, new_number, self.change_drug_name)
            self.cursor.execute(sql)
            self.connect.commit()
            QMessageBox.about(self, '修改', '修改成功！')
            self.change.close()
        except ValueError:
            QMessageBox.warning(self, '输入错误', '请检查输入')

    # 修改界面取消按钮
    def change_cancel_btn(self):
        self.change.close()

    # 制定界面确定按钮
    def buy_plan_check_btn_click(self):
        # 遍历吧，不想在eval了
        drug_names = [self.buy_plan.drug_name_input_1.text(),
                      self.buy_plan.drug_name_input_2.text(),
                      self.buy_plan.drug_name_input_3.text(),
                      self.buy_plan.drug_name_input_4.text()]
        for index, drug_name in enumerate(drug_names, start=1):
            # 好像还是要eval
            if drug_name != '':
                price = eval('self.buy_plan.price_input_' + '{}'.format(index)).text()
                number = eval('self.buy_plan.number_input_' + '{}'.format(index)).text()
                price = round(float(price),2)
                number = int(number)
                sql = 'Insert into plan_table (`drug_name`, `price`, `number`, `total`) VALUES ("{}","{}","{}","{}")'.format(drug_name,price,number,round(price*number, 2))
                self.cursor.execute(sql)
                self.connect.commit()
            else:
                break
        # 把通知的确定按钮改成中文的
        information = QMessageBox()
        information.setWindowTitle('通知')
        information.setText('执行成功')
        information.addButton(QPushButton('确定'), QMessageBox.YesRole)
        information.setSizeGripEnabled(True)
        # 始终修改不了通知窗口的大小，先暂定这样
        information.resize(1000, 200)
        information.exec_()
        self.buy_plan.close()

    def buy_plan_cancel_btn_click(self):
        self.buy_plan.close()

    # 这个灰色参数不要删除，否则会报错
    def buy_plan_total_label_click(self, total_label):
        drug_name_input = 'self.buy_plan.drug_name_input_'
        price_input = 'self.buy_plan.price_input_'
        number_input = 'self.buy_plan.number_input_'
        total_input = 'self.buy_plan.total_input_'
        limit_int = QIntValidator()
        limit_int.setRange(1, 1000)
        limit_double = QDoubleValidator()
        limit_double.setRange(0.01, 999.99)
        limit_double.setDecimals(2)
        for a in range(1, 5):
            # eval去掉字符串，变成正常的代码
            if eval(drug_name_input + str(a)).text() != '':
                eval(price_input + str(a)).setValidator(limit_double)
                eval(number_input + str(a)).setValidator(limit_int)
                get_price = eval(price_input + str(a)).text()
                get_number = eval(number_input + str(a)).text()
                # 保留小数点后两位显示
                eval(total_input + str(a)).setText(str(round(float(get_price) * int(get_number), 2)))
            else:
                break


# 以下为测试代码，可以不用管
if __name__ == '__main__':
    app = QApplication(sys.argv)
    buy_ui = Buy_MainWindow()
    buy_ui.show()
    sys.exit(app.exec())
