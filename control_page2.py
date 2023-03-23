import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import PyQt5
qt_Page2 = "Page2.ui"

class Page2(QWidget):
    def __init__(self):
        super(Page2,self).__init__()
        uic.loadUi(Page2,self)
        self.show()



if __name__ == "__main__":
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    window = Page2()
    sys.exit(app.exec_())