import pymysql
connect = pymysql.Connect(
    host='账号',
    port = 3306,
    user = 'root',
    password = '密码',
    db='数据库',
    #charset = 'utf8'
)
cursor = connect.cursor()
#sql = 'insert into dataTest1 values("i m one","i m two")'
#cursor.execute(sql)
sql = "select id from user where mac = '914-87-e0-67-8d-01'"
cursor.execute(sql)
connect.commit()
a = cursor.fetchall()
if len(a)==0:
    print(a)
cursor.close()
connect.close()
