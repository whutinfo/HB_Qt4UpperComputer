# -*- coding:utf-8 -*-

"""
mssql配置项
"""
DATABASES = {
    'default': {

        'ENGINE': 'sql_server.pyodbc',
	    'NAME': 'TestDB',
        #'NAME':'HB_NetSafetyDB',    #数据库的名字
        'HOST':'localhost',     #数据库的IP地址,
        'PORT': '1433',		#数据库的端口
        'USER': 'sa',  # 登录数据库的用户名
        'PASSWORD': '123',  # 登录数据库的密码
        'OPTIONS': {
            'driver': 'SQL Server Native Client 11.0',  # 注意，不行就试试11.0
        },
    }
}

# 可见光人脸图片路径
VIS_PATH = '可见光人脸图片/'