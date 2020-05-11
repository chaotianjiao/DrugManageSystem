from ui_code.sign_up_ui import Sign_up_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
import pymysql
class SignUp_MainWindow(QMainWindow,Sign_up_MainWindow):
    def __init__(self):
        super(SignUp_MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('注册')
        self.ok_btn.clicked.connect(self.ok)
        self.connect = pymysql.connect(host='localhost',
                                       port=3306,
                                       user='root',
                                       password='fyz98123',
                                       db='pycharm',
                                       charset='utf8',
                                       cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.connect.cursor()
    def ok(self):
        username = self.username_input.text()
        pwd = self.pwd_input.text()
        name = self.name_input.text()
        phone = self.phone_input.text()
        sex = self.sex_input.text()
        sql = 'Insert into user_table(`roleid`,`username`,`password`,' \
              '`truename`,`phone`,`sex`)VALUES ("{}","{}","{}","{}","{}","{}")'.format(520,
                                                                                       username,pwd,name,phone,sex)
        self.cursor.execute(sql)
        self.connect.commit()
        QMessageBox.about(self, '以提交', '请查询数据库')



