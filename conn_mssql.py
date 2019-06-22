# -*- coding:utf-8 -*-
import pyodbc
from PIL import Image
import io
import cv2
import numpy

from Settings import DATABASES

"""
连接数据库sql server的公共类
"""
class db_connect(object):

	def __init__(self):
		db_settings = DATABASES['default']

		self.driver = db_settings['OPTIONS']['driver']

		self.host = db_settings['HOST']

		self.database = db_settings['NAME']

		self.user = db_settings['USER']

		self.pwd = db_settings['PASSWORD']

	def __GetConnect(self):
		''''' Connect to the DB '''
		if not self.database:
			raise (NameError, "no setting db info")
		self.conn = pyodbc.connect(DRIVER=self.driver, SERVER=self.host, DATABASE=self.database,
		                           UID=self.user, PWD=self.pwd, charset="UTF-8")
		cur = self.conn.cursor()  # 后面对数据库执行的sql语句将使用游标指针来操作
		if not self.conn:
			raise (NameError, "connected failed!")
		else:
			return cur

	# 主要用来查询
	def execQuery(self, sql):
		''''' Perform one Sql statement '''
		cur = self.__GetConnect()
		cur.execute(sql)  # 通过指针来执行sql指令
		rows = cur.fetchall()  # 一次获取所有内容  获取的是所有Row的list，迭代循环时获取的就是Row.Row这个类，类似于一个元组，但是他们也可以通过字段名进行访问。
		cur.close()  # 游标指标关闭
		self.conn.close()  # 关闭数据库连接
		return rows

	# 增删改 都需要commit提交，并且无需返回
	"""
	ODBC支持在SQL语句中使用一个问号来作为参数。你可以在SQL语句后面加上值，用来传递给SQL语句中的问号。
	"""
	def execNoQuery(self,sql, args_list=[]):
		''''' Person one Sql statement like write data, or create table, database and so on'''
		cur = self.__GetConnect()
		if args_list != []:#  带参数执行语句
			cur.execute(sql, args_list)
		else:
			cur.execute(sql)
		self.conn.commit()  # 连接句柄来提交
		cur.close()
		self.conn.close()

if __name__ == "__main__":
	database = db_connect()
	# 插入图片image格式的语句
	# insert into Table_1 (image) Select * from OPENROWSET(BULK 'E:\python_project\人脸识别模块\temp\张三.jpg', SINGLE_BLOB) as image

	# 保存图片到数据库
	insert_sql = "insert into User_Face (Face_VIS) values (?)"
	path = '0.jpg'
	with open(path,'rb') as fp:
		data= fp.read()    #bytes
		database.execNoQuery(insert_sql,[data])

	# 从数据库读
	sql = 'select Face_VIS from User_Face'
	rows = database.execQuery(sql)
	i= 0
	for row in rows:
		i = i+1
		data = row.Face_VIS
		path = str(i) + ".jpg"
		with open(path,'wb') as fp:
			fp.write(data)



