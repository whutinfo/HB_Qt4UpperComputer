# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_face.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.login_user_list = QtWidgets.QListWidget(self.centralwidget)
        self.login_user_list.setGeometry(QtCore.QRect(60, 150, 271, 271))
        self.login_user_list.setObjectName("login_user_list")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 124, 81, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 124, 81, 21))
        self.label_2.setObjectName("label_2")
        self.get_a_picture_btn = QtWidgets.QPushButton(self.centralwidget)
        self.get_a_picture_btn.setGeometry(QtCore.QRect(230, 470, 93, 28))
        self.get_a_picture_btn.setObjectName("get_a_picture_btn")
        self.close_btn = QtWidgets.QPushButton(self.centralwidget)
        self.close_btn.setGeometry(QtCore.QRect(400, 470, 93, 28))
        self.close_btn.setObjectName("close_btn")
        self.show_camera_label = QtWidgets.QLabel(self.centralwidget)
        self.show_camera_label.setGeometry(QtCore.QRect(400, 150, 281, 271))
        self.show_camera_label.setText("")
        self.show_camera_label.setObjectName("show_camera_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "登记用户"))
        self.label_2.setText(_translate("MainWindow", "人脸图片"))
        self.get_a_picture_btn.setText(_translate("MainWindow", "拍照"))
        self.close_btn.setText(_translate("MainWindow", "关闭"))

