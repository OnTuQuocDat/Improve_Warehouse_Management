
from PyQt5 import QtWidgets


def wrong_password():
    msg = QtWidgets.QMessageBox()
    #icon Critical,Warning,Information,Question
    msg.setIcon(QtWidgets.QMessageBox.Warning)
    msg.setText("Wrong Password")
    msg.exec_()    

def wrong_initial():
    msg = QtWidgets.QMessageBox()
    #icon Critical,Warning,Information,Question
    msg.setIcon(QtWidgets.QMessageBox.Warning)
    msg.setText("Wrong Initial")
    msg.exec_() 

def miss_account():
    msg = QtWidgets.QMessageBox()
    #icon Critical,Warning,Information,Question
    msg.setIcon(QtWidgets.QMessageBox.Warning)
    msg.setText("New User. Contact DAQ to create your account")
    msg.exec_()     

def not_reset():
    msg = QtWidgets.QMessageBox()
    #icon Critical,Warning,Information,Question
    msg.setIcon(QtWidgets.QMessageBox.Critical)
    msg.setText("Not Reset User Password")
    msg.exec_() 


def change_pass_done():
    msg = QtWidgets.QMessageBox()
    #icon Critical,Warning,Information,Question
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setText("Done.Reset User Password")
    msg.exec_() 
   

def self_change_pass_done():
    msg = QtWidgets.QMessageBox()
    #icon Critical,Warning,Information,Question
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setText("Done. Your password is changed")
    msg.exec_() 

def check_new_pass_again():
    msg = QtWidgets.QMessageBox()
    #icon Critical,Warning,Information,Question
    msg.setIcon(QtWidgets.QMessageBox.Warning)
    msg.setText("Please confirm your new password again")
    msg.exec_()   

def check_your_old_pass_again():
    msg = QtWidgets.QMessageBox()
    #icon Critical,Warning,Information,Question
    msg.setIcon(QtWidgets.QMessageBox.Warning)
    msg.setText("Please check your old password again")
    msg.exec_() 

def done_transfer_to_spare():
    msg = QtWidgets.QMessageBox()
    #icon Critical,Warning,Information,Question
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setText("Transferred all part of this IPJ task to Spare")
    msg.exec_()       