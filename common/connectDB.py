import pymysql
from common.get_all_data import *


#获取数据库参数
mysqlconf = get_ini_data("database")
host=mysqlconf["mysql_test"]["host"]
port = int(mysqlconf["mysql_test"]["port"])
username = mysqlconf["mysql_test"]["username"]
password = mysqlconf["mysql_test"]["password"]
basename = mysqlconf["mysql_test"]["basename"]

#获取执行sql
sql_list = get_ini_data("sqlcase")["mysql_test"]["sql"].split("\n")
sql = sql_list[0]
conn = pymysql.connect(host=host,port=port,user=username,password=password,database=basename)
cur = conn.cursor()
result = cur.execute(sql)

