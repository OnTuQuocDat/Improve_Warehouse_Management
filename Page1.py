# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Page1.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserAccess(object):
    def setupUi(self, UserAccess):
        UserAccess.setObjectName("UserAccess")
        UserAccess.resize(500, 264)
        UserAccess.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(UserAccess)
        self.centralwidget.setObjectName("centralwidget")
        self.Role_1 = QtWidgets.QLabel(self.centralwidget)
        self.Role_1.setGeometry(QtCore.QRect(10, 60, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Role_1.setFont(font)
        self.Role_1.setObjectName("Role_1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 10, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Enter_page1 = QtWidgets.QPushButton(self.centralwidget)
        self.Enter_page1.setGeometry(QtCore.QRect(340, 80, 81, 51))
        self.Enter_page1.setObjectName("Enter_page1")
        self.Password = QtWidgets.QLabel(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(10, 120, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Password.setFont(font)
        self.Password.setObjectName("Password")
        self.Password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Password_input.setGeometry(QtCore.QRect(100, 130, 171, 31))
        self.Password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password_input.setObjectName("Password_input")
        self.Enter_page1_forgotpass = QtWidgets.QPushButton(self.centralwidget)
        self.Enter_page1_forgotpass.setGeometry(QtCore.QRect(70, 180, 111, 23))
        self.Enter_page1_forgotpass.setObjectName("Enter_page1_forgotpass")
        self.Enter_page1_changepass = QtWidgets.QPushButton(self.centralwidget)
        self.Enter_page1_changepass.setGeometry(QtCore.QRect(280, 180, 111, 23))
        self.Enter_page1_changepass.setObjectName("Enter_page1_changepass")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 60, 171, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 220, 81, 20))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(7)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 210, 47, 41))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(7)
        font.setUnderline(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        UserAccess.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(UserAccess)
        self.statusbar.setObjectName("statusbar")
        UserAccess.setStatusBar(self.statusbar)

        self.retranslateUi(UserAccess)
        QtCore.QMetaObject.connectSlotsByName(UserAccess)

    def retranslateUi(self, UserAccess):
        _translate = QtCore.QCoreApplication.translate
        UserAccess.setWindowTitle(_translate("UserAccess", "UserAccess"))
        self.Role_1.setText(_translate("UserAccess", "User"))
        self.label.setText(_translate("UserAccess", "EE WAREHOUSE CONTROLLER"))
        self.Enter_page1.setText(_translate("UserAccess", "Enter"))
        self.Password.setText(_translate("UserAccess", "Password"))
        self.Enter_page1_forgotpass.setText(_translate("UserAccess", "Forgot pass"))
        self.Enter_page1_changepass.setText(_translate("UserAccess", "Change pass"))
        self.label_2.setText(_translate("UserAccess", "Dev by DAQ"))
        self.label_3.setText(_translate("UserAccess", "V1.0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UserAccess = QtWidgets.QMainWindow()
    ui = Ui_UserAccess()
    ui.setupUi(UserAccess)
    UserAccess.show()
    sys.exit(app.exec_())