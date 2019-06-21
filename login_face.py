# -*- coding:utf-8 -*-
import ui_login_face
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *



class mainWindow(QMainWindow, ui_login_face.Ui_MainWindow):
	def __init__(self, parent=None):
		# super这个用法是调用父类的构造函数
	    # parent=None表示默认没有父Widget，如果指定父亲Widget，则调用之
		super(mainWindow, self).__init__(parent)
		self.setupUi(self)
		self.get_a_picture_btn.clicked.connect(self.get_a_picture)

	def get_a_picture(self):
		# 对当前选中的用户进行拍照
		ret = self.login_user_list.currentIndex().data()
		print(ret)

