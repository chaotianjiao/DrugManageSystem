from function.login import *
import sys
import os


if __name__ == '__main__':
    # 更改路径后图片能够正常显示
    os.chdir('./function')
    app = QApplication(sys.argv)
    start = LoginWindow()
    start.show()
    sys.exit(app.exec_())
