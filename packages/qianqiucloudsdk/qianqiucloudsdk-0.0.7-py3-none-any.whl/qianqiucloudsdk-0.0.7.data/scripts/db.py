#!python
# -*- coding: utf-8 -*-
# __author__ = "qianqiusoft"
from DBUtils.PersistentDB import PersistentDB
import pymysql
POOL = PersistentDB(
   creator=pymysql,  # 使用链接数据库的模块
   maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
   setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
   ping=0,
   # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
   closeable=False,
   # 如果为False时， conn.close() 实际上被忽略，供下次使用，再线程关闭时，才会自动关闭链接。如果为True时， conn.close()则关闭链接，那么再次调用pool.connection时就会报错，因为已经真的关闭了连接（pool.steady_connection()可以获取一个新的链接）
   threadlocal=None,  # 本线程独享值得对象，用于保存链接对象，如果链接对象被重置
   host='127.0.0.1',
   port=3306,
   user='zff',
   password='zff123',
   database='zff',
   charset='utf8',
)

def fetchAllUsers():
   conn = POOL.connection(shareable=False)
   cursor = conn.cursor()
   cursor.execute('select * from sys_user')
   result = cursor.fetchall()
   cursor.close()
   conn.close()
   return result