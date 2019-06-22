# -*- coding:utf-8 -*-

from conn_mssql import *

def Update_UserFace_Table():
	database = db_connect()

	sql = 'select OnlyID,UserID,RealName from Users'
	user_querys = database.execQuery(sql)

	sql = 'select OnlyID,UserID,RealName from User_Face'
	userface_querys = database.execQuery(sql)
	exist_flag = 0      # 根据onlyid判断是否存在该用户,存在为1，不存在为0

	# 首先在user_face表中删除旧表users中没有的用户
	delete_sql = 'delete from User_Face where OnlyID not in (select OnlyID from Users)'
	database.execNoQuery(delete_sql)

	# 旧表有新表没有的则插入，新表与旧表OnlyID一样，其他不一样的则更新
	for user_row in user_querys:

		# 旧表的一行比较完之后flag清空
		exist_flag = 0
		for user_face_row in userface_querys:
			# 比较onlyid
			if user_face_row.OnlyID != user_row.OnlyID :
				continue

			# 如果相等则表示存在，比较UserID，RealName是否一致，一致则不作更改，不一致则Update
			else:
				exist_flag = 1
				if user_face_row.UserID != user_row.UserID  or	 user_face_row.RealName != user_row.RealName :
					update_sql = 'update User_Face set UserID=?,RealName= ? where OnlyID =? '
					# 更新OnlyID，RealName
					database.execNoQuery(update_sql,[user_row.UserID, user_row.RealName, user_face_row.OnlyID])

				break

		# 整个新表遍历完都没有旧表的onlyid，则插入
		if exist_flag == 0:
			# 不存在该用户，插入数据
			insert_sql = 'insert into User_Face (OnlyID,UserID,RealName) Values (?,?,?)'
			database.execNoQuery(insert_sql,[user_row.OnlyID, user_row.UserID, user_row.RealName])