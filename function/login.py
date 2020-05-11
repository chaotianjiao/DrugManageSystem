import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QCompleter, QMessageBox, QLineEdit, QAction
from ui_code.login_ui import Login_MainWindow
from function.buy import Buy_MainWindow
from function.sell import Sell_MainWindow
from function.sign_up import SignUp_MainWindow

class LoginWindow(QMainWindow, Login_MainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('敏敏的药房')
        tool = self.addToolBar("菜单")
        self.action = QAction('注册', self)
        tool.addAction(self.action)
        tool.actionTriggered[QAction].connect(self.sign_up)
        self.login_btn.clicked.connect(self.click_login)
        # 智能补全
        self.complete = ['minmin','minmin小仙女','minmin大美女']
        self.user_input.setCompleter(QCompleter(self.complete))
        # 隐藏密码
        self.pwd_input.setEchoMode(QLineEdit.Password)
        # 这里要初始化好两个窗口，否则会报内存错误 Process fininshed code 17545645
        # 这个BUG改的我心累
        self.buy = Buy_MainWindow()
        self.sell = Sell_MainWindow()
        self.sign_up =SignUp_MainWindow()

    # 登录控制函数和跳转函数
    def click_login(self):
        user = self.user_input.text()
        pwd = self.pwd_input.text()
        if user == 'minmin' and pwd == 'piaoliang':
            self.buy.show()
            self.close()
        elif user == 'minmin' and pwd == 'meili':
            # 这里的sell也是定义在最下面
            self.sell.show()
            self.close()
        else:
            QMessageBox.about(self, "警告", "用户名或密码错误！")

    def sign_up(self):
        self.sign_up.show()
# 以下是测试用代码可以不管
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = LoginWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
