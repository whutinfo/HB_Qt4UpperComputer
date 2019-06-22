# -*- coding:utf-8 -*-
import ui_login_face
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import cv2
from conn_mssql import *
from Update_Table import *
from Settings import *


class mainWindow(QMainWindow, ui_login_face.Ui_MainWindow):
	def __init__(self, parent=None):
		# super这个用法是调用父类的构造函数
	    # parent=None表示默认没有父Widget，如果指定父亲Widget，则调用之
		super(mainWindow, self).__init__(parent)

		# 数据库的user_face与users表进行对比更新
		Update_UserFace_Table()

		self.setupUi(self)  # 初始化程序界面
		self.User_SetupUi()  # 自定义的初始化界面，除了通过designer画的ui生成的界面之外，用户通过程序添加的界面控件
		self.slot_init()  # 初始化槽函数


	def User_SetupUi(self):

		# 定义定时器，为了显示摄像头的视频
		self.timer_camera = QTimer()  # 定义定时器，用于控制显示视频的帧率
		self.cap = cv2.VideoCapture()  # 视频流
		self.CAM_NUM = 0  # 为0时表示视频流来自笔记本内置摄像头
		self.open_camera()

		# 显示用户List
		self.database = db_connect()
		sql = 'select * from User_Face'
		querys = self.database.execQuery(sql)

		for row in querys:
			user_name = row.RealName
			only_id = row.OnlyID
			item = QListWidgetItem(user_name)
			# 保存变量Only_id
			item.setData(Qt.UserRole,only_id)
			self.login_user_list.addItem(item)


	'''初始化所有槽函数'''

	def slot_init(self):
		self.get_a_picture_btn.clicked.connect(self.get_a_picture)
		self.timer_camera.timeout.connect(self.show_camera)  # 若定时器结束，则调用show_camera()
		self.close_btn.clicked.connect(self.closeWindow)  # 若该按键被点击，则调用close()，注意这个close是父类QtWidgets.QWidget自带的，会关闭程序

	'''槽函数'''

	def open_camera(self):
		if self.timer_camera.isActive() == False:  # 若定时器未启动
			flag = self.cap.open(self.CAM_NUM)  # 参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频
			if flag == False:  # flag表示open()成不成功
				msg = QMessageBox.warning(self, 'warning', "请检查相机于电脑是否连接正确", buttons=QMessageBox.Ok)
			else:
				self.timer_camera.start(30)  # 定时器开始计时30ms，结果是每过30ms从摄像头中取一帧显示

	def show_camera(self):
		flag, self.image = self.cap.read()  # 从视频流中读取

		show = cv2.resize(self.image, (260, 260))  # 把读到的帧的大小重新设置为 640x480
		show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
		showImage = QImage(show.data, show.shape[1], show.shape[0],
		                   QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
		self.show_camera_label.setPixmap(QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage

	def get_a_picture(self):
		# 对当前选中的用户进行拍照
		only_id = self.login_user_list.currentIndex().data(Qt.UserRole)
		user_name = self.login_user_list.currentIndex().data()
		flag, image = self.cap.read()  # 从视频流中读取
		image_path =VIS_PATH + user_name+'.jpg'
		# 保存成图片存到相应路径
		cv2.imencode('.jpg', image)[1].tofile(image_path)

		cv2.imshow('image',image)
		# 保存照片到数据库
		data = image.tobytes()       #将ndarray数据转成bytes保存到数据库
		sql = "update User_Face set Face_NIR=? where onlyID =? "
		self.database.execNoQuery(sql,[data,only_id])


	def closeWindow(self):
		# 关闭摄像头
		self.timer_camera.stop()  # 关闭定时器
		self.cap.release()  # 释放视频流
		self.show_camera_label.clear()  # 清空视频显示区域
		self.window().close()

