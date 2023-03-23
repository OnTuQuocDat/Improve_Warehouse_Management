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
# from Page1 import Ui_UserAccess
from Page1_update import Ui_UserAccess
from Page2_update import Ui_DLSupporter_Input
from Page3_update import Ui_Engineer_Output
from Page3_1_update import Ui_ConfirmTransferWindow
from Page4_update import Ui_ConfirmWindow
from PageAdmin1 import Ui_MainWindow
from PageAdmin2 import Ui_ConfirmChangePass
from Page1_changepass import Ui_ChangePassword
import datetime
from time import gmtime,strftime,localtime
from pymysql import *
import xlwt
import pandas.io.sql as sql_pandas
import pandas as pd
from checking_case import check_IPJ,check_module,check_purpose,check_quantity
from warning_case import *
from automatic_sendemail import send_email_to_admin


#Create the connection object sql
myconn = mysql.connector.connect(host = "localhost", user = "root", 
    passwd = "ontuquocdat",database = "eewarehouse_update2")

global cur
global sql
global sql_admin
global val 
global val_admin
global system_warning 
system_warning = 0
global list_index
list_index = []
global user_access_evidence


cur = myconn.cursor()
sql = ("insert into warehouse_controller(Year, Month, Day, PartNumber, BeckhoffPart, Quantity, Purpose, POnumber, IPJnumber, RFQnumber, Position, NoteDLSupporter, NoteSystem, ID) "
    + "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

sql_admin = ("insert into useraccount(Initial, DefaultPass, NewPass, UpdateNote, ID, Role) "
    + "values (%s, %s, %s, %s, %s, %s)")

class Page4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.win4 = QMainWindow()
        self.page4 = Ui_ConfirmWindow()
        self.page4.setupUi(self.win4)
        self.win4.setFixedHeight(301)
        self.win4.setFixedWidth(683)
        self.win4.show()
        
        self.page4.Yes_confirm.clicked.connect(self.action_yes_button)
        self.page4.No_confirm.clicked.connect(self.action_no_button)
        self.page4.Back_Button_4.clicked.connect(self.comeback_page3)
        
    def comeback_page3(self):
        self.win3 = Page3_update()
        self.win4.close()

    def action_yes_button(self):
        #Update lại Database
        day = strftime("%Y-%m-%d %H_%M",localtime())
        user = user_access_evidence
        # # projectIPJ = self.win3.page3.IPJ_Note_Output.text() + 'IPJ'
        projectIPJ = global_projectIPJ_page3  ##Refer global variable at def show_page4()
        # print("Project IPJ =  ",projectIPJ)
        quantity = global_quantity_page3 ##Refer global variable at def show_page4()
        note = [day,user,quantity,projectIPJ]
        note = str(note)

        #Read from database
        list_test = []

            
        for i in range (0, len(list_index)):
            try:
                cur.execute("select * from eewarehouse_update2.warehouse_controller")
                notesystem_note = cur.fetchall()
                # print("List index: ",notesystem_note[int(list_index[i])])
                # for x in notesystem_note:
                list_note = notesystem_note[int(list_index[i])]
                # print(list_note[12])
                list_test.append(str(list_note[12]))
                # print("Before: ",list_test)
                # remain_quantity = int(list_note[5]) - int(quantity)

            except:
                myconn.rollback()

            #Append data to Note
            try: 
                # Update Quantity
                sql_afterget = "update eewarehouse_update2.warehouse_controller SET NoteSystem = %s WHERE ID = %s"
                # val_afterget = (int(list_index[i]+1))
                list_test.append(note)
                # print("After: ",list_test)
                # val_afterget = (str(remain_quantity),str(list_test),str(list_index[i] + 1))
                val_afterget = (str(list_test),str(list_index[i] + 1))
                # print(val_afterget)
                cur.execute(sql_afterget,val_afterget)

                myconn.commit()
                # cur.execute("update warehouse_controller set Quantity = '1' where index = ")
                #Update NOTE_SYSTEM
                # sql = "update eewarehouse_update2.warehouse_controller SET NoteSystem = %s WHERE ID = %s"
                # val = (abc)  #List NoteSystem.append
                
            except:
                myconn.rollback()

            # print("list index: ",list_index)
            self.win4.close()
    def action_no_button(self):
        self.win4.close()

class Page3_1_update(QMainWindow):
    def __init__(self):
        super().__init__()
        self.win3_1 = QMainWindow()
        self.page3_1 = Ui_ConfirmTransferWindow()
        self.page3_1.setupUi(self.win3_1)
        self.win3_1.setFixedHeight(202)
        self.win3_1.setFixedWidth(535)
        self.win3_1.show()

        # self.page3_1.pushButton.clicked.connect(self.action_yes_transfer)
        # self.page3_1.pushButton_2.clicked.connect(self.action_cancel_transfer)

    def action_yes_transfer(self):
        self.win3_1.close()
    def action_cancel_transfer(self):
        self.win3_1.close()
    
        

class Page3_update (QMainWindow):
    def __init__(self):
        super().__init__()
        self.win3 = QMainWindow()
        self.page3 = Ui_Engineer_Output()
        self.page3.setupUi(self.win3)
        self.win3.setFixedHeight(301)
        self.win3.setFixedWidth(691)
        self.win3.show()

        #Engineer get Output
        self.page3.Enter_page3_findproduct.clicked.connect(self.show_page4)
        self.page3.Enter_page3_findproduct_spare.clicked.connect(self.show_spare)
        self.page3.Enter_page3_monitordata.clicked.connect(self.export_excel_monitor_project)
        self.page3.Enter_page3_transferpart.clicked.connect(self.transfer_part_to_spare)
        self.page3.Back_Button_3.clicked.connect(self.comeback_page1)
        self.page3.Enter_page3_get_all_part.clicked.connect(self.get_project_part_to_assembly)
    
    def get_project_part_to_assembly(self):
        if self.page3.IPJ_Note_Monitor.text() != 0:
            try:
                cur.execute("select * from eewarehouse_update2.warehouse_controller")
                all_project_part = cur.fetchall()
                for x in all_project_part:
                    if x[8] == self.page3.IPJ_Note_Monitor.text():
                        #check part là spare or project
                        if x[6] == "Project":
                            print("Export all parts of IPJ project for assemble")
                            self.export_excel_monitor_project() #xuất excel ra để monitor vị trí lấy part

                            #Update database quantity
                            day = strftime("%Y-%m-%d %H_%M",localtime())
                            user = user_access_evidence
                            projectIPJ = self.page3.IPJ_Note_Monitor.text() + 'IPJ'
                            note = [day,user,"All", projectIPJ]
                            note = str(note)
                            # print("Note: ",note)
                            
                try:   
                    sql_update = "update eewarehouse_update2.warehouse_controller SET Quantity = '0', NoteSystem = %s WHERE IPJnumber = %s"
                    val_update = (note,self.page3.IPJ_Note_Monitor.text())
                    cur.execute(sql_update,val_update)
                    myconn.commit()
                except:
                    myconn.rollback()

            except:
                myconn.rollback()

    def comeback_page1(self):
        self.win1 = Page1_update()
        self.win3.close()

    def export_excel_monitor_project(self):
        list_PartNumber = []
        # list_BeckhoffPart = []
        list_Quantity = []
        list_POnumber = []
        list_IPJnumber = []
        list_RFQnumber = []
        list_Position = []
        if self.page3.IPJ_Note_Monitor.text() != str(0):
            try:
                cur.execute("SELECT * FROM eewarehouse_update2.warehouse_controller")
                self.monitor_check = cur.fetchall()

                for self.a in self.monitor_check:
                    # print(self.a)
                    #Filter only theo IPJ thôi
                    #So sánh IPJ database and IPJ nhap vao
                    if self.a[8] == self.page3.IPJ_Note_Monitor.text():
                        # print(self.a)
                        list_PartNumber.append(self.a[3])
                        list_Quantity.append(self.a[5])
                        list_POnumber.append(self.a[7])
                        list_IPJnumber.append(self.a[8])
                        list_RFQnumber.append(self.a[9])
                        list_Position.append(self.a[10])

                print("List Part Number: ",list_PartNumber)
                print("List Quantity: ",list_Quantity)
                #dictionary of lists
                dict = {'IPJnumber' : list_IPJnumber, 'RFQ' : list_RFQnumber, 'PartNumber' : list_PartNumber, 'Quantity' : list_Quantity,'POnumber' : list_POnumber, 'Position' : list_Position}

                df = pd.DataFrame(dict)
                # df.to_csv('Demo.csv')
                address = 'C:/Users/Quoc Dat/Downloads/MonitorIPJ'
                df.to_csv(address + "/" + strftime("%Y-%m-%d %H_%M",localtime()) + '_'+ self.a[8] + 'IPJ' + '.csv')

            except:
                myconn.rollback() 
        
    def transfer_part_to_spare(self):
        self.win3_1 = Page3_1_update()
        self.win3_1.page3_1.pushButton.clicked.connect(self.action_yes_transfer)
        self.win3_1.page3_1.pushButton_2.clicked.connect(self.action_cancel_transfer)
    
    def action_yes_transfer(self):
        try:
            sql_transfer = "update warehouse_controller SET Purpose = %s WHERE IPJnumber = %s"
            val_transfer = ("Spare Part",self.page3.IPJ_Transfer_input.text())
            cur.execute(sql_transfer,val_transfer)
            myconn.commit()
            done_transfer_to_spare()
            self.win3_1.win3_1.close()
        except:
            myconn.rollback()
        
    def action_cancel_transfer(self):
        self.win3_1.win3_1.close()
        
    def show_spare(self):
        try:
            cur.execute("select * FROM eewarehouse_update2.warehouse_controller")
            self.check_spare = cur.fetchall()
            if str.upper(self.page3.Module_TextEdit_Output.toPlainText()) != "":
                result_position,get_quantity,spare_quantity,software_proposal = self.spare_algorithm()
        except:
            myconn.rollback()
        #Open page 4 result
        if str.upper(self.page3.Module_TextEdit_Output.toPlainText()) != "":
            self.win4 = Page4()
            self.win4.page4.Position_TextEdit_Result.setText(result_position)
            self.win4.page4.Get_Quantity_Result.setText(get_quantity)
            self.win4.page4.Remain_Quantity_result.setText(spare_quantity)
            self.win4.page4.Database_Proposal_Edit.setText(software_proposal)
            # print(result[0])
            self.win3.close()
    
    def spare_algorithm(self):
        result_position = None
        get_quantity = None
        spare_quantity = None
        software_proposal = None
        list_quantity = []
        list_position = []
        for self.spare in self.check_spare:
            module_available = check_module(str.upper(self.spare[3]),str.upper(self.page3.Module_TextEdit_Output.toPlainText()))
            if module_available == 1:
                purpose_result = check_purpose(self.spare[6])
                if purpose_result == 0:
                    list_quantity.append(int(self.spare[5]))
                    list_position.append(self.spare[10])

        sum_quantity = 0
        for v in list_quantity:
            sum_quantity += v
        Quantity_Spare_need = int(self.page3.Quantity_SpinBox_Output.text())
        if sum_quantity == 0:
            result_position = "No position"
            get_quantity = "Out of stock"
            software_proposal = "Out of stock in Spare. Please order it"
            spare_quantity = None
        elif sum_quantity < Quantity_Spare_need:
            #Give all quantity in spare for you, please order phần thiếu
            result_position = str(list_position)
            get_quantity = str(list_quantity)
            software_proposal = "Please order at least " + str(Quantity_Spare_need-sum_quantity) + " part " + str.upper(self.page3.Module_TextEdit_Output.toPlainText()) + " for stock in Spare."
        elif sum_quantity >= Quantity_Spare_need:
            result_position = None
            get_quantity = None
            software_proposal = None
            spare_quantity = None
            list_position_coding_spare = []
            list_quantity_coding_spare = []

            for i in range(0,len(list_quantity)):
                minus_spare = Quantity_Spare_need - list_quantity[i]
                if minus_spare < 0:
                    stop_index_spare = i
                    break
                else:
                    print("Run FIFO algorithm, minus spare = ",minus_spare)
                    Quantity_Spare_need = minus_spare
                    stop_index_spare = i
            
            if stop_index_spare == 0:
                result_position = str(list_position[0])
                get_quantity = str(self.page3.Quantity_SpinBox_Output.text())
                if sum_quantity == int(self.page3.Quantity_SpinBox_Output.text()):
                    software_proposal = "You can take it in Spare. But out of stock in spare.PLEASE ORDER FOR OTHER USER CAN GET PART"
                else:
                    software_proposal = "You can take it in Spare."
                spare_quantity = None
            else:
                sum_spare = list_quantity[0]
                for k in range(0,stop_index_spare):
                    sum_spare += list_quantity[k+1]
                
                if int(self.page3.Quantity_SpinBox_Output.text()) - sum_spare < 0:
                    last_index_spare = list_quantity[stop_index_spare] + (int(self.page3.Quantity_SpinBox_Output.text()) - sum_spare)

                    for i in range(0,stop_index_spare):
                        list_quantity_coding_spare.append(list_quantity[i])
                        list_position_coding_spare.append(list_position[i])
                    list_quantity_coding_spare.append(last_index_spare)
                    list_position_coding_spare.append(list_position[stop_index_spare])

                    #Output
                    result_position = str(list_position_coding_spare)
                    get_quantity = str(list_quantity_coding_spare)
                    spare_quantity = None
                    software_proposal = None
        return result_position,get_quantity,spare_quantity,software_proposal
    
    def show_page4(self):
        global global_projectIPJ_page3
        global global_quantity_page3
        global_projectIPJ_page3 = self.page3.IPJ_Note_Output.text()
        global_quantity_page3 = self.page3.Quantity_SpinBox_Output.text()
        #Access to database to get result and display
        try:
            cur.execute("SELECT * FROM eewarehouse_update2.warehouse_controller")
            self.result = cur.fetchall()
            if str.upper(self.page3.Module_TextEdit_Output.toPlainText()) != "":
                result_position,get_quantity,spare_quantity,software_proposal = self.main_algorithm()
        except:
            myconn.rollback()
        # myconn.close()
        
        #Open page 4 result
        if str.upper(self.page3.Module_TextEdit_Output.toPlainText()) != "":
            self.win4 = Page4()
            self.win4.page4.Position_TextEdit_Result.setText(result_position)
            self.win4.page4.Get_Quantity_Result.setText(get_quantity)
            self.win4.page4.Remain_Quantity_result.setText(spare_quantity)
            self.win4.page4.Database_Proposal_Edit.setText(software_proposal)

            # print(result[0])
            self.win3.close()

    def main_algorithm(self):
        result_position = None
        get_quantity = None
        spare_quantity = None
        software_proposal = None
        list_quantity = []
        list_position = []
        for self.x in self.result:
            #check module co hay ko
            # print("Index: ",self.result.index(self.x))
            module_available = check_module(str.upper(self.x[3]),str.upper(self.page3.Module_TextEdit_Output.toPlainText()))
            if module_available == 1:
                # print("Co hang")
                #Check project or spare part?
                purpose_result = check_purpose(self.x[6])
                if purpose_result == 1: #check for Project
                    check_IPJnumber = check_IPJ(int(self.x[8]),int(self.page3.IPJ_Note_Output.text()))
                    if check_IPJnumber == 1:
                        #xuat quantity
                        list_quantity.append(int(self.x[5]))
                        list_position.append(self.x[10])
                        # print("Index5: ",self.result.index(self.x[5]))
                        # print("Index10: ",self.result.index(self.x))

                        list_index.append(self.result.index(self.x))
                    else:
                        print("Ko trung IPJ")

                else: #check for Spare Part
                    print("Spare Part - Please find product in spare")


        
        sum_quantity = 0
        for v in list_quantity:
            sum_quantity += v
        print("Quantity con trong kho IPJ: ",sum_quantity)
        Quantity_need = int(self.page3.Quantity_SpinBox_Output.text())
        if sum_quantity == 0:
            print("Software Proposal: Out of stock, please order it")
            result_position = "No position"
            get_quantity = "Out of stock"
            software_proposal = "Out of stock, please order it or you could find in Spare Warehouse."
            spare_quantity = None

        elif sum_quantity < Quantity_need:
            # --> Only give sum quantity in IPJ for you, please order phần còn thiếu
            print("Quantity: ",list_quantity)
            print("Position: ",list_position)
            print("Please order them: ", Quantity_need-sum_quantity)
            result_position = str(list_position)
            get_quantity = str(list_quantity)
            software_proposal = "Please order more " + str(Quantity_need-sum_quantity) + " part " + str.upper(self.page3.Module_TextEdit_Output.toPlainText()) + " or you could find in Spare warehouse."
            spare_quantity = None

        elif sum_quantity >= Quantity_need:
            list_position_coding = []
            list_quantity_coding = []
            # stop_index = 0
            result_position = None
            get_quantity = None
            software_proposal = None
            spare_quantity = None

            for i in range(0,len(list_quantity)):
                minus = Quantity_need - list_quantity[i]
                if minus < 0: 
                    print("Cap quantity need")
                    print("Loop stop at index: ",i)
                    stop_index = i
                    break
                else:
                    print("Run FIFO,minus = ", minus)
                    Quantity_need = minus
                    stop_index = i 

            if stop_index == 0:
                print("Cap đúng só lượng quantity need")
                result_position = str(list_position[0])
                get_quantity = str(self.page3.Quantity_SpinBox_Output.text())
                software_proposal = "Normal. You can take it"
                spare_quantity = None
            else:
                #Tính tổng từ index 0 đến index thứ i
                # for k in range(0,stop_index):
                #     sumX = sumX + list_quantity[k]
                #     print("Sum: ",sumX) 
                sum = list_quantity[0]
                for k in range(0,stop_index):
                    sum += list_quantity[k+1]
                print(sum)


                if int(self.page3.Quantity_SpinBox_Output.text()) - sum > 0:  #Trùng tr hợp trên
                    print("ISSUE problem")
                elif int(self.page3.Quantity_SpinBox_Output.text()) - sum == 0:    #Trùng tr hợp trên
                    print("Lay index position tuong ung voi k index ") #vừa đủ để cấp
                else:
                    #So luong can lay
                    #Lấy full từ 0 đến index (stop_index - 1) + index cuối  với quantity như sau:
                    last_index = list_quantity[stop_index] + (int(self.page3.Quantity_SpinBox_Output.text()) - sum)
                    # print("Last index: ",last_index)
                    
                    for i in range(0,stop_index):
                        list_quantity_coding.append(list_quantity[i])
                        list_position_coding.append(list_position[i])
                    list_quantity_coding.append(last_index)
                    list_position_coding.append(list_position[stop_index])
                    
                    #Output ra interface
                    result_position = str(list_position_coding)
                    get_quantity = str(list_quantity_coding)
                    spare_quantity = None
                    software_proposal = None
                    
        return result_position,get_quantity,spare_quantity, software_proposal



class Page2_update (QMainWindow):
    def __init__(self):
        super().__init__()
        self.win2 = QMainWindow()
        self.page2 = Ui_DLSupporter_Input()
        self.page2.setupUi(self.win2)
        self.win2.setFixedHeight(421)
        self.win2.setFixedWidth(821)
        self.win2.show()
        
        #Input from DL supporter
        # self.page2.Enter_page2.clicked.connect(self.popup_data)
        self.page2.Enter_page2_upload.clicked.connect(self.popup_data)
        self.page2.Enter_All_Spare.clicked.connect(self.export_all_spare)
        self.page2.Enter_Monthly_Inventory.clicked.connect(self.export_monthly_spare)
        self.page2.Back_button_2.clicked.connect(self.comeback_page1)

    def comeback_page1(self):
        self.win1 = Page1_update()
        self.win2.close()

    def popup_data(self):
        #save to database
        today = datetime.datetime.now()
        ID_product = 0 ################################TEMP###########
        val = (today.year,today.month,today.day,self.page2.Module_TextEdit.toPlainText(),self.page2.CheckBeckhoff_ComboBox.currentText(),self.page2.Quantity_input.text(),self.page2.Purpose_ComboBox.currentText(),self.page2.PO_Note.text(),self.page2.IPJ_Note.text(),self.page2.RFQ_Note.text(),self.page2.Position_TextEdit.toPlainText(),self.page2.DL_Supporter_Note.toPlainText(),system_warning,ID_product)
        try:
            cur.execute(sql,val)
            myconn.commit()
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Upload database success")
            msg.exec_()
            #Delete data
            self.page2.Module_TextEdit.clear()
            self.page2.Quantity_input.clear()
            self.page2.PO_Note.clear()
            self.page2.IPJ_Note.clear()
            self.page2.RFQ_Note.clear()
            self.page2.Position_TextEdit.clear()
            self.page2.DL_Supporter_Note.clear()

            
        except:
            myconn.rollback()
        # myconn.close()


    def export_all_spare(self):
        try:
            df = sql_pandas.read_sql('select * from eewarehouse_update2.warehouse_controller',myconn)
            address = 'C:/Users/Quoc Dat/Downloads/FullDatabase'
            # df.to_excel(address + '/'+ w.page1.Role_listdown.currentText() + '_' + 'FullDatabase' + '.xlsx')
            df.to_excel(address + '/' + strftime("%Y-%m-%d %H_%M",localtime()) + '_'+ 'FullDatabase' + '.xlsx')
            #Pop up window
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Export Database Success")
            msg.exec_()
        except:
            myconn.rollback()

    def export_monthly_spare(self):
        try:
            address = 'C:/Users/Quoc Dat/Downloads/MonthlyInventory'
            sql = "select * from eewarehouse_update2.warehouse_controller where Month = %s and Year = %s"
            adr =(self.page2.Month_input.text(), self.page2.Year_input.text(),)
            cur.execute(sql,adr)
            myresult = cur.fetchall()

            if myresult == []:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("No Data Return")
                msg.exec_()  
            else:
                #Khai bao list
                PartNumber = []
                BeckhoffPart = []
                Quantity = []
                Purpose = []
                POnumber = []
                IPJnumber = []
                RFQnumber = []
                Position = []
                NoteDLSupporter = []
                for x in myresult:
                    PartNumber.append(x[3])
                    BeckhoffPart.append(x[4])
                    Quantity.append(x[5])
                    Purpose.append(x[6])
                    POnumber.append(x[7])
                    IPJnumber.append(x[8])
                    RFQnumber.append(x[9])
                    Position.append(x[10])
                    NoteDLSupporter.append(x[11])
                dict = {'PartNumber': PartNumber,'BeckhoffPart': BeckhoffPart,'Quantity': Quantity,'Purpose': Purpose,'POnumber': POnumber,'IPJnumber': IPJnumber,'RFQnumber': RFQnumber,'Position': Position,'NoteDLSupporter': NoteDLSupporter}

                df = pd.DataFrame(dict)
                
                # csv_data = df.to_csv('filename.csv',index=False)
                df.to_excel(address + '/' + strftime("%Y-%m-%d %H_%M",localtime()) + '_'+ 'Month ' + self.page2.Month_input.text() + ' Year ' + self.page2.Year_input.text() + '.xlsx')
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("EXport database success")
                msg.exec_()
            
        except:
            myconn.rollback()

class PageAdmin2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.win_admin2 = QMainWindow()
        self.page_admin2 = Ui_ConfirmChangePass()
        self.page_admin2.setupUi(self.win_admin2)
        self.win_admin2.setFixedHeight(172)
        self.win_admin2.setFixedWidth(519)
        self.win_admin2.show()


class PageAdmin1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.win_admin1 = QMainWindow()
        self.page_admin1 = Ui_MainWindow()
        self.page_admin1.setupUi(self.win_admin1)
        self.win_admin1.setFixedHeight(238)
        self.win_admin1.setFixedWidth(614)
        self.win_admin1.show()
        
#####################################################################################
        self.page_admin1.pushButton_2.clicked.connect(self.create_user)
        self.page_admin1.reset_pass_button.clicked.connect(self.reset_pass)

    def show_confirm_change_pass(self):
        self.win_admin2 = PageAdmin2()

    def reset_pass(self):
        self.show_confirm_change_pass()
        self.win_admin2.page_admin2.YES_RESET.clicked.connect(self.confirm_reset)
        self.win_admin2.page_admin2.NO_RESET.clicked.connect(self.confirm_notreset)

    def confirm_reset(self):
        try:
            # cur.execute("select * from eewarehouse_update2.useraccount")
            # result_reset = cur.fetchall()
            # for x in result_reset:
            #     if x[0] == self.page_admin1.user_input_changepass.text():
            sql_reset = "UPDATE useraccount SET DefaultPass = %s WHERE Initial = %s"
            val_reset = (self.page_admin1.new_pass.text(),self.page_admin1.user_input_changepass.text()) 
            cur.execute(sql_reset,val_reset)
            myconn.commit()
            change_pass_done() 
        except:
            myconn.rollback()
        self.win_admin2.win_admin2.close()

    def confirm_notreset(self):
        not_reset()
        self.win_admin2.win_admin2.close()


    def create_user(self):
        #Find ID_user đang là bao nhiêu
        try:
            cur.execute("select * from eewarehouse_update2.useraccount")
            result_user = cur.fetchall()
            # print(len(result_user))
            if len(result_user) == 0:
                ID_user = "first"
            else:
                for x in result_user:
                    # print (x[0])
                    if x[0] == 0:
                        ID_user = "first"
                    else:
                        if x[0] == self.page_admin1.add_new_user.text():
                            print("No need to create new user")
                            ID_user = "appeared"
                            break
                        else:
                            ####
                            ID_user = len(result_user) + 1
        except:
            myconn.rollback()

        if ID_user == "appeared":
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("User appeared")
            msg.exec_()
        elif ID_user == "first":
            print("First")
            ID_user = 1
            Initial = self.page_admin1.add_new_user.text()
            DefaultPass = self.page_admin1.default_pass.text()
            NewPass = None
            UpdateNote = str(strftime("%Y-%m-%d %H_%M",localtime()))
            ID_create = str(ID_user)
            Role = str(self.page_admin1.comboBox.currentText())
            val_admin = (Initial,DefaultPass,NewPass,UpdateNote,ID_create,Role)

            try:
                cur.execute(sql_admin,val_admin)
                myconn.commit()
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Created New User")
                msg.exec_()           

            except:
                myconn.rollback()

        else:
            # print("Second")
            Initial = self.page_admin1.add_new_user.text()
            DefaultPass = self.page_admin1.default_pass.text()
            NewPass = None
            UpdateNote = str(strftime("%Y-%m-%d %H_%M",localtime()))
            ID_create = str(ID_user)
            Role = str(self.page_admin1.comboBox.currentText())
            val_admin = (Initial,DefaultPass,NewPass,UpdateNote,ID_create,Role)

            try:
                cur.execute(sql_admin,val_admin)
                myconn.commit()
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Created New User")
                msg.exec_()           

            except:
                myconn.rollback()

class Page1_changepass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.win1_changepass = QMainWindow()
        self.page1_changepass = Ui_ChangePassword()
        self.page1_changepass.setupUi(self.win1_changepass)
        self.win1_changepass.setFixedHeight(264)
        self.win1_changepass.setFixedWidth(500)
        self.win1_changepass.show()

        self.page1_changepass.Button_change_pass.clicked.connect(self.change_password)

    def change_password(self):
        trigger = 0
        try:
            cur.execute("select * from eewarehouse_update2.useraccount")
            result_change = cur.fetchall()
            for x in result_change:
                if x[0] == str.upper(self.page1_changepass.user_changepass.text()):
                    if x[1] == self.page1_changepass.old_pass.text():
                        trigger = 1
                        if self.page1_changepass.new_pass.text() == self.page1_changepass.confirm_new_pass.text():
                            try:
                                sql_self_changepass = "update eewarehouse_update2.useraccount SET DefaultPass = %s WHERE Initial = %s and DefaultPass = %s"
                                val_self_changepass = (self.page1_changepass.new_pass.text(),self.page1_changepass.user_changepass.text(),self.page1_changepass.old_pass.text())
                                cur.execute(sql_self_changepass,val_self_changepass)
                                myconn.commit()
                                self_change_pass_done()
                                self.win1_changepass.close()
                            except:
                                myconn.rollback()
                        else:
                            check_new_pass_again()

            if trigger == 0:
                check_your_old_pass_again()
        except:
            myconn.rollback()
        # try:
        #     sql_self_changepass = "update eewarehouse_update2.useraccount SET DefaultPass = %s WHERE Initial = %s and DefaultPass = %s"
        #     val_self_changepass = (self.page1_changepass.new_pass.text(),self.page1_changepass.user_changepass.text(),self.page1_changepass.old_pass.text())
            
        #     cur.execute(sql_self_changepass,val_self_changepass)
        #     myconn.commit()
            
        #     #truy cập lại database check
        # except:
        #     myconn.rollback()

class Page1_update (QMainWindow):
    def __init__(self):
        super().__init__()
        # Ui_UserAccess.Enter_page1.clicked.connect(self.show_page2)
        self.win1 = QMainWindow()
        self.page1 = Ui_UserAccess()
        self.page1.setupUi(self.win1)
        self.win1.setFixedHeight(264)
        self.win1.setFixedWidth(500)
        self.win1.show()

        self.page1.Enter_page1.clicked.connect(self.check_enter_page1)
        self.page1.Enter_page1_changepass.clicked.connect(self.change_password)
        self.page1.Enter_page1_forgotpass.clicked.connect(self.forgot_password)

    def show_page2(self):
        self.win2 = Page2_update()
        # self.win2.show()
        #Close window 1
        self.win1.close()
    
    def show_page3(self):
        self.win3 = Page3_update()
        # self.win3.show()
        #Close window 1
        self.win1.setEnabled(False)
        self.win1.close()
    
    def show_pageAdmin1(self):
        self.win1_admin = PageAdmin1()
        self.win1.close()

    def check_enter_page1(self):
        global user_access_evidence 
        
        if str.upper(self.page1.lineEdit.text()) == "DAQ" and self.page1.Password_input.text() == "admin":
            # if self.page1.Password_input.text() == "admin":
            self.show_pageAdmin1()
        else:
            try:
                cur.execute("select * from eewarehouse_update2.useraccount")
                result_check = cur.fetchall()
                for x in result_check:
                    #check initial
                    if x[0] == str.upper(self.page1.lineEdit.text()):
                        #check password
                        if x[1] == self.page1.Password_input.text():
                            user_access_evidence = str.upper(self.page1.lineEdit.text())
                            #check title
                            if x[5] == "Engineer" or x[5] == "PM" or x[5] == "Purchaser" or x[5] == "Technical Writer":
                                self.show_page3()
                            elif x[5] == "DL Supporter":
                                self.show_page2()
                            else:
                                self.show_page3()
                                # system_warning = 1
                        else:
                            wrong_password()


            except:
                myconn.rollback()

    def change_password(self):
        #User tự change pass
        self.win1_changepass = Page1_changepass() 

    def forgot_password(self):
        #User ask admin cấp lại default password
        send_email_to_admin()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Page1_update()
    


    # print(strftime("%Y-%m",gmtime()))


    sys.exit(app.exec())
