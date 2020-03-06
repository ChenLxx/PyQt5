import sys
from PyQt5.QtWidgets import QApplication,QWidget
import PyQt5
if __name__=='__main__':
    app=QApplication(sys.argv)
    w=QWidget()
    w.resize(1200,600)
    w.move(600,300)
    w.setWindowTitle("第一个窗口应用")
    w.show()

    #进入程序主循环，通过exit 函数确保安全结束
    sys.exit(app.exec_())
