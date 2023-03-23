# Author: On Tu Quoc Dat - Control System Engineer
# Company : Sonion Viet Nam Co.,Ltd
# Version : 1.0
# Update: 24/02/2023
# Built = Python 3.10.7 

#Special command python -m PyQt5.uic.pyuic -x inteface.ui -o interface.py

from asyncio.windows_events import NULL
#from asyncore import write
import sys
from tempfile import TemporaryDirectory
from tracemalloc import start
from PyQt5.QtWidgets import QApplication,QMainWindow
# from data_process import create_excel
# from interface import Ui_ExcelSupportApp
from Page1 import Ui_UserAccess
from Page2 import Ui_DLSupporter_Input
import control_page2
from PyQt5 import QtCore,QtGui,QtWidgets,uic


class Page1:
    def __init__(self):
        self.win1 = QMainWindow()
        self.page1 = Ui_UserAccess()
        self.page1.setupUi(self.win1)

    def show_win1(self):
        self.win1.show()


    def call_page2(self):
        # self.main_win.close
        window2 = Page2()
        window2.show_win2()

class Page2:
    def __init__(self):
        self.win2 = QMainWindow()
        self.page2 = Ui_DLSupporter_Input()
        self.page2.setupUi(self.win2)

    def show_win2(self):
        self.win2.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window1 = Page1()
    window1.show_win1()
    
    #Trigger Event
    
    window1.page1.Enter_page1.clicked.connect(window1.call_page2)

    sys.exit(app.exec())
