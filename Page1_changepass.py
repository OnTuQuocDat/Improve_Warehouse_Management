# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Page1_changepass.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChangePassword(object):
    def setupUi(self, ChangePassword):
        ChangePassword.setObjectName("ChangePassword")
        ChangePassword.resize(500, 264)
        self.centralwidget = QtWidgets.QWidget(ChangePassword)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 210, 47, 41))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(7)
        font.setUnderline(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 220, 81, 20))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(7)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 10, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Role_1 = QtWidgets.QLabel(self.centralwidget)
        self.Role_1.setGeometry(QtCore.QRect(10, 40, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Role_1.setFont(font)
        self.Role_1.setObjectName("Role_1")
        self.user_changepass = QtWidgets.QLineEdit(self.centralwidget)
        self.user_changepass.setGeometry(QtCore.QRect(170, 40, 171, 31))
        self.user_changepass.setObjectName("user_changepass")
        self.old_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.old_pass.setGeometry(QtCore.QRect(170, 90, 171, 31))
        self.old_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.old_pass.setObjectName("old_pass")
        self.Password = QtWidgets.QLabel(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(10, 80, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Password.setFont(font)
        self.Password.setObjectName("Password")
        self.Password_2 = QtWidgets.QLabel(self.centralwidget)
        self.Password_2.setGeometry(QtCore.QRect(10, 130, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Password_2.setFont(font)
        self.Password_2.setObjectName("Password_2")
        self.new_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.new_pass.setGeometry(QtCore.QRect(170, 140, 171, 31))
        self.new_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_pass.setObjectName("new_pass")
        self.confirm_new_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.confirm_new_pass.setGeometry(QtCore.QRect(170, 190, 171, 31))
        self.confirm_new_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_new_pass.setObjectName("confirm_new_pass")
        self.Password_3 = QtWidgets.QLabel(self.centralwidget)
        self.Password_3.setGeometry(QtCore.QRect(10, 180, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Password_3.setFont(font)
        self.Password_3.setObjectName("Password_3")
        self.Button_change_pass = QtWidgets.QPushButton(self.centralwidget)
        self.Button_change_pass.setGeometry(QtCore.QRect(370, 100, 101, 51))
        self.Button_change_pass.setObjectName("Button_change_pass")
        ChangePassword.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ChangePassword)
        self.statusbar.setObjectName("statusbar")
        ChangePassword.setStatusBar(self.statusbar)

        self.retranslateUi(ChangePassword)
        QtCore.QMetaObject.connectSlotsByName(ChangePassword)

    def retranslateUi(self, ChangePassword):
        _translate = QtCore.QCoreApplication.translate
        ChangePassword.setWindowTitle(_translate("ChangePassword", "MainWindow"))
        self.label_3.setText(_translate("ChangePassword", "V1.0"))
        self.label_2.setText(_translate("ChangePassword", "Dev by DAQ"))
        self.label.setText(_translate("ChangePassword", "EE WAREHOUSE CONTROLLER"))
        self.Role_1.setText(_translate("ChangePassword", "User"))
        self.Password.setText(_translate("ChangePassword", "Old Password"))
        self.Password_2.setText(_translate("ChangePassword", "New Password"))
        self.Password_3.setText(_translate("ChangePassword", "Confirm Password"))
        self.Button_change_pass.setText(_translate("ChangePassword", "Change pass"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChangePassword = QtWidgets.QMainWindow()
    ui = Ui_ChangePassword()
    ui.setupUi(ChangePassword)
    ChangePassword.show()
    sys.exit(app.exec_())
