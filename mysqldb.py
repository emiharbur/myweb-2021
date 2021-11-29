#适用于pyspider连接mysql
#适用于python3

import pymysql
from datetime import date, datetime, timedelta

class SQL:
    username = 'root'
    password = 'root'
    database = 'test'
    host = 'localhost'
    connection = ''
    connectstat = True
    placeholder = '%s'
#基础声明，username、password 为mysql的用户名和密码，database为需要连接的数据库的名字，host为数据库的ip和端口
#connectstat为数据库连接状态
