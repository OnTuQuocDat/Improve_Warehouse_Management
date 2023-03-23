# Author: On Tu Quoc Dat - Control System Engineer
# Company : Sonion Viet Nam Co.,Ltd
# Version : 1.0
# Update: 24/02/2023
# Built = Python 3.10.7 

#Special command python -m PyQt5.uic.pyuic -x inteface.ui -o interface.py


from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5 import QtWidgets
import sys
import mysql.connector
from Page1 import Ui_UserAccess
from Page2 import Ui_DLSupporter_Input
from Page3 import Ui_Engineer_Output
from Page4 import Ui_ConfirmWindow

#Create the connection object sql
myconn = mysql.connector.connect(host = "192.168.2.195", user = "root", 
    passwd = "ontuquocdat",database = "eewarehouse")

global cur
global sql
global val 
global system_warning 
system_warning = 0
# global result
cur = myconn.cursor()
sql = ("insert into Beckhoff(module, quantity, purpose, IPJnumber, RFQnumber, Position, NoteDLSupporter, NoteSystem) "
    + "values (%s, %s, %s, %s, %s, %s, %s, %s)")

class Page4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.win4 = QMainWindow()
        self.page4 = Ui_ConfirmWindow()
        self.page4.setupUi(self.win4)
        self.win4.setFixedHeight(256)
        self.win4.setFixedWidth(683)
        self.win4.show()
        
        self.page4.Yes_confirm.clicked.connect(self.action_yes_button)
        self.page4.No_confirm.clicked.connect(self.action_no_button)
    
        # self.process_page4()

    # def process_page4(self):
    #     print("Hello")
    #     try:
    #         cur.execute("SELECT * FROM beckhoff")
    #         result = cur.fetchall()

    #         for self.x in result:
    #             #check module co hay ko
    #             if str.upper(self.x[0]) == str.upper(self.page3.Module_TextEdit_Output.toPlainText()):
    #                 print("checkeedd")
                    
    #     except:
    #         myconn.rollback()

    def action_yes_button(self):
        self.win4.close()
    def action_no_button(self):
        self.win4.close()


class Page3 (QMainWindow):
    def __init__(self):
        super().__init__()
        self.win3 = QMainWindow()
        self.page3 = Ui_Engineer_Output()
        self.page3.setupUi(self.win3)
        self.win3.setFixedHeight(305)
        self.win3.setFixedWidth(684)
        self.win3.show()

        #Engineer get Output
        self.page3.Enter_page3.clicked.connect(self.show_page4)
    
    # def display_page4(self):
    #     self.win4 = Page4()

    def show_page4(self):
        #Access to database to get result and display
        try:
            cur.execute("SELECT * FROM beckhoff")
            self.result = cur.fetchall()

            # for self.x in self.result:
            #     # print(x[0])
            #     #check module co hay ko
            #     if str.upper(self.x[0]) == str.upper(self.page3.Module_TextEdit_Output.toPlainText()):
            #         #check quantity du hay ko
            #         if int(self.x[1]) >= int(self.page3.Quantity_SpinBox_Output.text()):
            #             print("OK")
            #             #Check coi số project muốn tìm Project IPJ có trùng với nội dung ở cột Note IPJ ko? Nếu trùng thì cho lấy ra, ko trùng thì sẽ propose ra trong kho
            #             #còn spare bao nhiêu, dự án A B C còn bao nhieu
            #             if int(self.x[3]) == int(self.page3.IPJ_Note_Output.text()):
            #                 print(self.x[5])
            #             else:
            #                 print("Check spare part")
                            
            #         else:
            #             print("This part is out of stock, please order it")

            result_position,get_quantity,spare_quantity,software_proposal = self.main_algorithm()


        except:
            myconn.rollback()
        myconn.close()
        
        #Open page 4 result
        self.win4 = Page4()
        self.win4.page4.Position_TextEdit_Result.setText(result_position)
        self.win4.page4.Get_Quantity_Result.setText(get_quantity)
        self.win4.page4.Spare_TextEdit_Uptodate.setText(spare_quantity)
        self.win4.page4.Database_Proposal_Edit.setText(software_proposal)

        # print(result[0])
        self.win3.close()

    def main_algorithm(self):
        result_position = None
        get_quantity = None
        spare_quantity = None
        software_proposal = None
        for self.x in self.result:
            #check module co hay ko
            module_available = check_module(str.upper(self.x[0]),str.upper(self.page3.Module_TextEdit_Output.toPlainText()))
            if module_available == 1:
                print("Co hang")
                #Check quantity
                quantity_enough,inventory = check_quantity(int(self.x[1]),int(self.page3.Quantity_SpinBox_Output.text()))
                if quantity_enough == 1:
                    print("Du so luong")
                    #Check IPJ number
                    checkIPJnumber = check_IPJ(int(self.x[3]),int(self.page3.IPJ_Note_Output.text()))
                    if checkIPJnumber == 1:
                        print("Trung IPJ, cho phep lay")
                        print("Con ton kho cua du an: ",inventory)
                        break
                    elif checkIPJnumber == 0:
                        # print("Chay lai vong lap, goi y cac IPJ khac con stock")
                        print("IPJ number con hang: ",self.x[3])
                        print("So luong bao nhieu cai: ", self.x[1])
                        
        return result_position,get_quantity,spare_quantity, software_proposal

def check_module(a,b):
    if a == b:
        return 1
    else:
        return 0 
def check_quantity(a,b):
    if a >= b:
        inventory = a - b
        return 1,inventory
    else:
        return 0,0
def check_IPJ(a,b):
    if a == b:
        return 1
    else:
        return 0

class Page2 (QMainWindow):
    def __init__(self):
        super().__init__()
        self.win2 = QMainWindow()
        self.page2 = Ui_DLSupporter_Input()
        self.page2.setupUi(self.win2)
        self.win2.setFixedHeight(320)
        self.win2.setFixedWidth(682)
        self.win2.show()
        
        #Input from DL supporter
        self.page2.Enter_page2.clicked.connect(self.popup_data)
    
    def popup_data(self):
        #save to database
        val = (self.page2.Module_TextEdit.toPlainText(),self.page2.spinBox.text(),self.page2.Purpose_ComboBox.currentText(),self.page2.IPJ_Note.text(),self.page2.RFQ_Note.text(),self.page2.Position_TextEdit.toPlainText(),self.page2.DL_Supporter_Note.toPlainText(),system_warning)
        try:
            cur.execute(sql,val)
            myconn.commit()
        except:
            myconn.rollback()
        # myconn.close()
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Upload database success")
        msg.exec_()

class Page1 (QMainWindow):
    def __init__(self):
        super().__init__()
        # Ui_UserAccess.Enter_page1.clicked.connect(self.show_page2)
        self.win1 = QMainWindow()
        self.page1 = Ui_UserAccess()
        self.page1.setupUi(self.win1)
        self.win1.setFixedHeight(146)
        self.win1.setFixedWidth(381)
        self.win1.show()

    def show_page2(self):
        self.win2 = Page2()
        # self.win2.show()
        #Close window 1
        self.win1.close()
    
    def show_page3(self):
        self.win3 = Page3()
        # self.win3.show()
        #Close window 1
        self.win1.setEnabled(False)
        self.win1.close()

    def check_enter_page1(self):
        if self.page1.Role_listdown.currentText() == "Importer (DL Supporter)":
            self.show_page2()
        elif self.page1.Role_listdown.currentText() == "KHU" or "TUQN" or "NPH" or "TRUT" or "HHP":
            self.show_page3()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Page1()
    

    w.page1.Enter_page1.clicked.connect(w.check_enter_page1)




    sys.exit(app.exec())
