# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Page3.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Engineer_Output(object):
    def setupUi(self, Engineer_Output):
        Engineer_Output.setObjectName("Engineer_Output")
        Engineer_Output.resize(684, 305)
        self.centralwidget = QtWidgets.QWidget(Engineer_Output)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-10, 0, 691, 301))
        self.tabWidget.setObjectName("tabWidget")
        self.FindPart = QtWidgets.QWidget()
        self.FindPart.setObjectName("FindPart")
        self.Module_BH_output = QtWidgets.QLabel(self.FindPart)
        self.Module_BH_output.setGeometry(QtCore.QRect(20, 70, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Module_BH_output.setFont(font)
        self.Module_BH_output.setObjectName("Module_BH_output")
        self.label = QtWidgets.QLabel(self.FindPart)
        self.label.setGeometry(QtCore.QRect(200, 0, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.IPJ_Note_Output = QtWidgets.QSpinBox(self.FindPart)
        self.IPJ_Note_Output.setGeometry(QtCore.QRect(120, 180, 221, 31))
        self.IPJ_Note_Output.setMaximum(999999999)
        self.IPJ_Note_Output.setProperty("value", 0)
        self.IPJ_Note_Output.setObjectName("IPJ_Note_Output")
        self.Quantity_SpinBox_Output = QtWidgets.QSpinBox(self.FindPart)
        self.Quantity_SpinBox_Output.setGeometry(QtCore.QRect(120, 130, 221, 31))
        self.Quantity_SpinBox_Output.setObjectName("Quantity_SpinBox_Output")
        self.Enter_page3_findproduct = QtWidgets.QPushButton(self.FindPart)
        self.Enter_page3_findproduct.setGeometry(QtCore.QRect(440, 90, 131, 41))
        self.Enter_page3_findproduct.setObjectName("Enter_page3_findproduct")
        self.Module_TextEdit_Output = QtWidgets.QTextEdit(self.FindPart)
        self.Module_TextEdit_Output.setGeometry(QtCore.QRect(120, 80, 221, 31))
        self.Module_TextEdit_Output.setObjectName("Module_TextEdit_Output")
        self.Quantity_BH_output = QtWidgets.QLabel(self.FindPart)
        self.Quantity_BH_output.setGeometry(QtCore.QRect(20, 120, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Quantity_BH_output.setFont(font)
        self.Quantity_BH_output.setObjectName("Quantity_BH_output")
        self.Project_IPJ_Output = QtWidgets.QLabel(self.FindPart)
        self.Project_IPJ_Output.setGeometry(QtCore.QRect(20, 170, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Project_IPJ_Output.setFont(font)
        self.Project_IPJ_Output.setObjectName("Project_IPJ_Output")
        self.Question_Label = QtWidgets.QLabel(self.FindPart)
        self.Question_Label.setGeometry(QtCore.QRect(20, 30, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Question_Label.setFont(font)
        self.Question_Label.setObjectName("Question_Label")
        self.Enter_page3_findproduct_spare = QtWidgets.QPushButton(self.FindPart)
        self.Enter_page3_findproduct_spare.setGeometry(QtCore.QRect(440, 170, 131, 41))
        self.Enter_page3_findproduct_spare.setObjectName("Enter_page3_findproduct_spare")
        self.Back_Button_3 = QtWidgets.QPushButton(self.FindPart)
        self.Back_Button_3.setGeometry(QtCore.QRect(20, 0, 101, 31))
        self.Back_Button_3.setObjectName("Back_Button_3")
        self.label_11 = QtWidgets.QLabel(self.FindPart)
        self.label_11.setGeometry(QtCore.QRect(30, 220, 47, 41))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(7)
        font.setUnderline(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.FindPart)
        self.label_12.setGeometry(QtCore.QRect(570, 230, 81, 20))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(7)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.tabWidget.addTab(self.FindPart, "")
        self.MonitorDataProject = QtWidgets.QWidget()
        self.MonitorDataProject.setObjectName("MonitorDataProject")
        self.label_2 = QtWidgets.QLabel(self.MonitorDataProject)
        self.label_2.setGeometry(QtCore.QRect(200, 0, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Project_IPJ_Monitor = QtWidgets.QLabel(self.MonitorDataProject)
        self.Project_IPJ_Monitor.setGeometry(QtCore.QRect(20, 70, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Project_IPJ_Monitor.setFont(font)
        self.Project_IPJ_Monitor.setObjectName("Project_IPJ_Monitor")
        self.IPJ_Note_Monitor = QtWidgets.QSpinBox(self.MonitorDataProject)
        self.IPJ_Note_Monitor.setGeometry(QtCore.QRect(180, 80, 221, 31))
        self.IPJ_Note_Monitor.setMaximum(999999999)
        self.IPJ_Note_Monitor.setObjectName("IPJ_Note_Monitor")
        self.Enter_page3_monitordata = QtWidgets.QPushButton(self.MonitorDataProject)
        self.Enter_page3_monitordata.setGeometry(QtCore.QRect(450, 70, 131, 41))
        self.Enter_page3_monitordata.setObjectName("Enter_page3_monitordata")
        self.Enter_page3_get_all_part = QtWidgets.QPushButton(self.MonitorDataProject)
        self.Enter_page3_get_all_part.setGeometry(QtCore.QRect(210, 180, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Enter_page3_get_all_part.setFont(font)
        self.Enter_page3_get_all_part.setObjectName("Enter_page3_get_all_part")
        self.label_13 = QtWidgets.QLabel(self.MonitorDataProject)
        self.label_13.setGeometry(QtCore.QRect(570, 230, 81, 20))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(7)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.MonitorDataProject)
        self.label_14.setGeometry(QtCore.QRect(30, 220, 47, 41))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(7)
        font.setUnderline(True)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.tabWidget.addTab(self.MonitorDataProject, "")
        self.TransferParttoSpare = QtWidgets.QWidget()
        self.TransferParttoSpare.setObjectName("TransferParttoSpare")
        self.label_4 = QtWidgets.QLabel(self.TransferParttoSpare)
        self.label_4.setGeometry(QtCore.QRect(200, 0, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.IPJ_Transfer = QtWidgets.QLabel(self.TransferParttoSpare)
        self.IPJ_Transfer.setGeometry(QtCore.QRect(20, 90, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.IPJ_Transfer.setFont(font)
        self.IPJ_Transfer.setObjectName("IPJ_Transfer")
        self.IPJ_Transfer_input = QtWidgets.QSpinBox(self.TransferParttoSpare)
        self.IPJ_Transfer_input.setGeometry(QtCore.QRect(169, 100, 221, 31))
        self.IPJ_Transfer_input.setMaximum(999999999)
        self.IPJ_Transfer_input.setObjectName("IPJ_Transfer_input")
        self.Enter_page3_transferpart = QtWidgets.QPushButton(self.TransferParttoSpare)
        self.Enter_page3_transferpart.setGeometry(QtCore.QRect(490, 90, 151, 41))
        self.Enter_page3_transferpart.setObjectName("Enter_page3_transferpart")
        self.label_15 = QtWidgets.QLabel(self.TransferParttoSpare)
        self.label_15.setGeometry(QtCore.QRect(30, 220, 47, 41))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(7)
        font.setUnderline(True)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.TransferParttoSpare)
        self.label_16.setGeometry(QtCore.QRect(570, 230, 81, 20))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(7)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.tabWidget.addTab(self.TransferParttoSpare, "")
        Engineer_Output.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Engineer_Output)
        self.statusbar.setObjectName("statusbar")
        Engineer_Output.setStatusBar(self.statusbar)

        self.retranslateUi(Engineer_Output)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Engineer_Output)

    def retranslateUi(self, Engineer_Output):
        _translate = QtCore.QCoreApplication.translate
        Engineer_Output.setWindowTitle(_translate("Engineer_Output", "Engineer_Output"))
        self.Module_BH_output.setText(_translate("Engineer_Output", "Module"))
        self.label.setText(_translate("Engineer_Output", "EE WAREHOUSE CONTROLLER"))
        self.Enter_page3_findproduct.setText(_translate("Engineer_Output", "Find Product"))
        self.Quantity_BH_output.setText(_translate("Engineer_Output", "Quantity"))
        self.Project_IPJ_Output.setText(_translate("Engineer_Output", "Project IPJ"))
        self.Question_Label.setText(_translate("Engineer_Output", "What do you want to find ?"))
        self.Enter_page3_findproduct_spare.setText(_translate("Engineer_Output", "Find Product Spare"))
        self.Back_Button_3.setText(_translate("Engineer_Output", "BACK"))
        self.label_11.setText(_translate("Engineer_Output", "V1.0"))
        self.label_12.setText(_translate("Engineer_Output", "Dev by DAQ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.FindPart), _translate("Engineer_Output", "Find Part"))
        self.label_2.setText(_translate("Engineer_Output", "EE WAREHOUSE CONTROLLER"))
        self.Project_IPJ_Monitor.setText(_translate("Engineer_Output", "IPJ Number"))
        self.Enter_page3_monitordata.setText(_translate("Engineer_Output", "Export Data"))
        self.Enter_page3_get_all_part.setText(_translate("Engineer_Output", "Get All Parts to assemble"))
        self.label_13.setText(_translate("Engineer_Output", "Dev by DAQ"))
        self.label_14.setText(_translate("Engineer_Output", "V1.0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MonitorDataProject), _translate("Engineer_Output", "Monitor Data Project and Ready for assembly"))
        self.label_4.setText(_translate("Engineer_Output", "EE WAREHOUSE CONTROLLER"))
        self.IPJ_Transfer.setText(_translate("Engineer_Output", "IPJ Number"))
        self.Enter_page3_transferpart.setText(_translate("Engineer_Output", "Transfer Part to Spare"))
        self.label_15.setText(_translate("Engineer_Output", "V1.0"))
        self.label_16.setText(_translate("Engineer_Output", "Dev by DAQ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TransferParttoSpare), _translate("Engineer_Output", "Transfer Part to Spare"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Engineer_Output = QtWidgets.QMainWindow()
    ui = Ui_Engineer_Output()
    ui.setupUi(Engineer_Output)
    Engineer_Output.show()
    sys.exit(app.exec_())
