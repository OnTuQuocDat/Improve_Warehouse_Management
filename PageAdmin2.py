# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PageAdmin2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConfirmChangePass(object):
    def setupUi(self, ConfirmChangePass):
        ConfirmChangePass.setObjectName("ConfirmChangePass")
        ConfirmChangePass.resize(519, 172)
        self.centralwidget = QtWidgets.QWidget(ConfirmChangePass)
        self.centralwidget.setObjectName("centralwidget")
        self.Confirm_Project_complete_2 = QtWidgets.QLabel(self.centralwidget)
        self.Confirm_Project_complete_2.setGeometry(QtCore.QRect(60, 30, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Confirm_Project_complete_2.setFont(font)
        self.Confirm_Project_complete_2.setObjectName("Confirm_Project_complete_2")
        self.YES_RESET = QtWidgets.QPushButton(self.centralwidget)
        self.YES_RESET.setGeometry(QtCore.QRect(150, 90, 75, 23))
        self.YES_RESET.setObjectName("YES_RESET")
        self.NO_RESET = QtWidgets.QPushButton(self.centralwidget)
        self.NO_RESET.setGeometry(QtCore.QRect(250, 90, 75, 23))
        self.NO_RESET.setObjectName("NO_RESET")
        ConfirmChangePass.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ConfirmChangePass)
        self.statusbar.setObjectName("statusbar")
        ConfirmChangePass.setStatusBar(self.statusbar)

        self.retranslateUi(ConfirmChangePass)
        QtCore.QMetaObject.connectSlotsByName(ConfirmChangePass)

    def retranslateUi(self, ConfirmChangePass):
        _translate = QtCore.QCoreApplication.translate
        ConfirmChangePass.setWindowTitle(_translate("ConfirmChangePass", "MainWindow"))
        self.Confirm_Project_complete_2.setText(_translate("ConfirmChangePass", "Are you sure to RESET PASSWORD FOR THIS USER?"))
        self.YES_RESET.setText(_translate("ConfirmChangePass", "OK"))
        self.NO_RESET.setText(_translate("ConfirmChangePass", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConfirmChangePass = QtWidgets.QMainWindow()
    ui = Ui_ConfirmChangePass()
    ui.setupUi(ConfirmChangePass)
    ConfirmChangePass.show()
    sys.exit(app.exec_())
