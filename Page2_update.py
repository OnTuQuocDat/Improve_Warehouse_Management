# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Page2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DLSupporter_Input(object):
    def setupUi(self, DLSupporter_Input):
        DLSupporter_Input.setObjectName("DLSupporter_Input")
        DLSupporter_Input.resize(817, 443)
        self.centralwidget = QtWidgets.QWidget(DLSupporter_Input)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 821, 421))
        self.tabWidget.setObjectName("tabWidget")
        self.InputPO = QtWidgets.QWidget()
        self.InputPO.setObjectName("InputPO")
        self.Quantity_BH = QtWidgets.QLabel(self.InputPO)
        self.Quantity_BH.setGeometry(QtCore.QRect(10, 170, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Quantity_BH.setFont(font)
        self.Quantity_BH.setObjectName("Quantity_BH")
        self.Position_BH = QtWidgets.QLabel(self.InputPO)
        self.Position_BH.setGeometry(QtCore.QRect(410, 170, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Position_BH.setFont(font)
        self.Position_BH.setObjectName("Position_BH")
        self.PO_Note = QtWidgets.QSpinBox(self.InputPO)
        self.PO_Note.setGeometry(QtCore.QRect(180, 300, 221, 31))
        self.PO_Note.setMaximum(999999999)
        self.PO_Note.setObjectName("PO_Note")
        self.IPJ_Note = QtWidgets.QSpinBox(self.InputPO)
        self.IPJ_Note.setGeometry(QtCore.QRect(540, 120, 221, 31))
        self.IPJ_Note.setMaximum(999999999)
        self.IPJ_Note.setObjectName("IPJ_Note")
        self.Enter_page2_upload = QtWidgets.QPushButton(self.InputPO)
        self.Enter_page2_upload.setGeometry(QtCore.QRect(580, 290, 131, 41))
        self.Enter_page2_upload.setObjectName("Enter_page2_upload")
        self.Module_TextEdit = QtWidgets.QTextEdit(self.InputPO)
        self.Module_TextEdit.setGeometry(QtCore.QRect(180, 60, 221, 31))
        self.Module_TextEdit.setObjectName("Module_TextEdit")
        self.PO_BH = QtWidgets.QLabel(self.InputPO)
        self.PO_BH.setGeometry(QtCore.QRect(10, 290, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PO_BH.setFont(font)
        self.PO_BH.setObjectName("PO_BH")
        self.RFQ_BH = QtWidgets.QLabel(self.InputPO)
        self.RFQ_BH.setGeometry(QtCore.QRect(420, 50, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RFQ_BH.setFont(font)
        self.RFQ_BH.setObjectName("RFQ_BH")
        self.IPJ_BH = QtWidgets.QLabel(self.InputPO)
        self.IPJ_BH.setEnabled(True)
        self.IPJ_BH.setGeometry(QtCore.QRect(420, 110, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.IPJ_BH.setFont(font)
        self.IPJ_BH.setObjectName("IPJ_BH")
        self.Purpose_BH = QtWidgets.QLabel(self.InputPO)
        self.Purpose_BH.setGeometry(QtCore.QRect(10, 230, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Purpose_BH.setFont(font)
        self.Purpose_BH.setObjectName("Purpose_BH")
        self.RFQ_Note = QtWidgets.QSpinBox(self.InputPO)
        self.RFQ_Note.setGeometry(QtCore.QRect(540, 60, 221, 31))
        self.RFQ_Note.setMaximum(999999999)
        self.RFQ_Note.setObjectName("RFQ_Note")
        self.Yournote_text = QtWidgets.QLabel(self.InputPO)
        self.Yournote_text.setGeometry(QtCore.QRect(410, 230, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Yournote_text.setFont(font)
        self.Yournote_text.setObjectName("Yournote_text")
        self.Position_TextEdit = QtWidgets.QTextEdit(self.InputPO)
        self.Position_TextEdit.setGeometry(QtCore.QRect(540, 180, 221, 31))
        self.Position_TextEdit.setObjectName("Position_TextEdit")
        self.label = QtWidgets.QLabel(self.InputPO)
        self.label.setGeometry(QtCore.QRect(280, 10, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.DL_Supporter_Note = QtWidgets.QTextEdit(self.InputPO)
        self.DL_Supporter_Note.setGeometry(QtCore.QRect(540, 240, 221, 31))
        self.DL_Supporter_Note.setObjectName("DL_Supporter_Note")
        self.Quantity_input = QtWidgets.QSpinBox(self.InputPO)
        self.Quantity_input.setGeometry(QtCore.QRect(180, 180, 221, 31))
        self.Quantity_input.setObjectName("Quantity_input")
        self.Purpose_ComboBox = QtWidgets.QComboBox(self.InputPO)
        self.Purpose_ComboBox.setGeometry(QtCore.QRect(180, 240, 221, 31))
        self.Purpose_ComboBox.setEditable(False)
        self.Purpose_ComboBox.setObjectName("Purpose_ComboBox")
        self.Purpose_ComboBox.addItem("")
        self.Purpose_ComboBox.addItem("")
        self.Module_BH = QtWidgets.QLabel(self.InputPO)
        self.Module_BH.setGeometry(QtCore.QRect(10, 50, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Module_BH.setFont(font)
        self.Module_BH.setObjectName("Module_BH")
        self.CheckBeckhoff_BH = QtWidgets.QLabel(self.InputPO)
        self.CheckBeckhoff_BH.setGeometry(QtCore.QRect(10, 110, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CheckBeckhoff_BH.setFont(font)
        self.CheckBeckhoff_BH.setObjectName("CheckBeckhoff_BH")
        self.CheckBeckhoff_ComboBox = QtWidgets.QComboBox(self.InputPO)
        self.CheckBeckhoff_ComboBox.setGeometry(QtCore.QRect(180, 120, 221, 31))
        self.CheckBeckhoff_ComboBox.setEditable(False)
        self.CheckBeckhoff_ComboBox.setObjectName("CheckBeckhoff_ComboBox")
        self.CheckBeckhoff_ComboBox.addItem("")
        self.CheckBeckhoff_ComboBox.addItem("")
        self.Back_button_2 = QtWidgets.QPushButton(self.InputPO)
        self.Back_button_2.setGeometry(QtCore.QRect(20, 10, 101, 31))
        self.Back_button_2.setObjectName("Back_button_2")
        self.label_9 = QtWidgets.QLabel(self.InputPO)
        self.label_9.setGeometry(QtCore.QRect(30, 340, 47, 41))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(7)
        font.setUnderline(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.InputPO)
        self.label_10.setGeometry(QtCore.QRect(740, 350, 81, 20))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(7)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.InputPO, "")
        self.ManageInventory = QtWidgets.QWidget()
        self.ManageInventory.setObjectName("ManageInventory")
        self.label_2 = QtWidgets.QLabel(self.ManageInventory)
        self.label_2.setGeometry(QtCore.QRect(270, 10, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Enter_All_Spare = QtWidgets.QPushButton(self.ManageInventory)
        self.Enter_All_Spare.setGeometry(QtCore.QRect(260, 60, 281, 51))
        self.Enter_All_Spare.setObjectName("Enter_All_Spare")
        self.Enter_Monthly_Inventory = QtWidgets.QPushButton(self.ManageInventory)
        self.Enter_Monthly_Inventory.setGeometry(QtCore.QRect(440, 160, 321, 41))
        self.Enter_Monthly_Inventory.setObjectName("Enter_Monthly_Inventory")
        self.Month_input = QtWidgets.QSpinBox(self.ManageInventory)
        self.Month_input.setGeometry(QtCore.QRect(100, 160, 91, 31))
        self.Month_input.setMaximum(999999999)
        self.Month_input.setObjectName("Month_input")
        self.Year_input = QtWidgets.QSpinBox(self.ManageInventory)
        self.Year_input.setGeometry(QtCore.QRect(270, 160, 91, 31))
        self.Year_input.setMaximum(999999999)
        self.Year_input.setObjectName("Year_input")
        self.label_3 = QtWidgets.QLabel(self.ManageInventory)
        self.label_3.setGeometry(QtCore.QRect(50, 160, 51, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.ManageInventory)
        self.label_4.setGeometry(QtCore.QRect(230, 160, 41, 31))
        self.label_4.setObjectName("label_4")
        self.label_11 = QtWidgets.QLabel(self.ManageInventory)
        self.label_11.setGeometry(QtCore.QRect(30, 340, 47, 41))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(7)
        font.setUnderline(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.ManageInventory)
        self.label_12.setGeometry(QtCore.QRect(740, 350, 81, 20))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(7)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.tabWidget.addTab(self.ManageInventory, "")
        DLSupporter_Input.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DLSupporter_Input)
        self.statusbar.setObjectName("statusbar")
        DLSupporter_Input.setStatusBar(self.statusbar)

        self.retranslateUi(DLSupporter_Input)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DLSupporter_Input)

    def retranslateUi(self, DLSupporter_Input):
        _translate = QtCore.QCoreApplication.translate
        DLSupporter_Input.setWindowTitle(_translate("DLSupporter_Input", "DLSupporter_Input"))
        self.Quantity_BH.setText(_translate("DLSupporter_Input", "Quantity"))
        self.Position_BH.setText(_translate("DLSupporter_Input", "Position Saving"))
        self.Enter_page2_upload.setText(_translate("DLSupporter_Input", "Upload to Database"))
        self.PO_BH.setText(_translate("DLSupporter_Input", "PO number"))
        self.RFQ_BH.setText(_translate("DLSupporter_Input", "RFQ number"))
        self.IPJ_BH.setText(_translate("DLSupporter_Input", "Project IPJ"))
        self.Purpose_BH.setText(_translate("DLSupporter_Input", "Purpose"))
        self.Yournote_text.setText(_translate("DLSupporter_Input", "Your note"))
        self.label.setText(_translate("DLSupporter_Input", "EE WAREHOUSE CONTROLLER"))
        self.Purpose_ComboBox.setItemText(0, _translate("DLSupporter_Input", "Spare Part"))
        self.Purpose_ComboBox.setItemText(1, _translate("DLSupporter_Input", "Project"))
        self.Module_BH.setText(_translate("DLSupporter_Input", "Part Number/Module"))
        self.CheckBeckhoff_BH.setText(_translate("DLSupporter_Input", "Beckhoff Part?"))
        self.CheckBeckhoff_ComboBox.setItemText(0, _translate("DLSupporter_Input", "Beckhoff Part"))
        self.CheckBeckhoff_ComboBox.setItemText(1, _translate("DLSupporter_Input", "Other"))
        self.Back_button_2.setText(_translate("DLSupporter_Input", "BACK"))
        self.label_9.setText(_translate("DLSupporter_Input", "V1.0"))
        self.label_10.setText(_translate("DLSupporter_Input", "Dev by DAQ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.InputPO), _translate("DLSupporter_Input", "Input PO"))
        self.label_2.setText(_translate("DLSupporter_Input", "EE WAREHOUSE CONTROLLER"))
        self.Enter_All_Spare.setText(_translate("DLSupporter_Input", "Export All Spare in Warehouse"))
        self.Enter_Monthly_Inventory.setText(_translate("DLSupporter_Input", "Export All Parts pushed into Warehouse in this time"))
        self.label_3.setText(_translate("DLSupporter_Input", "Month"))
        self.label_4.setText(_translate("DLSupporter_Input", "Year"))
        self.label_11.setText(_translate("DLSupporter_Input", "V1.0"))
        self.label_12.setText(_translate("DLSupporter_Input", "Dev by DAQ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ManageInventory), _translate("DLSupporter_Input", "Manage Inventory"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DLSupporter_Input = QtWidgets.QMainWindow()
    ui = Ui_DLSupporter_Input()
    ui.setupUi(DLSupporter_Input)
    DLSupporter_Input.show()
    sys.exit(app.exec_())
