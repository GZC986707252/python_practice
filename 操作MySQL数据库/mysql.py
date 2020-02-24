import pymysql     #导入模块

#建立数据库连接
db = pymysql.connect('localhost','root','root','mydb')
#通过cursor()方法获取游标对象
cursor = db.cursor()

#通过execute()方法执行sql语句
cursor.execute('select version()')
#通过fetchone()方法获取单条结果
version = cursor.fetchone()
print('Database version: %s'%version)

cursor.execute("select * from admin_info")
#通过fetchall()方法获取全部结果
data = cursor.fetchall()
for item in data:
    print('name: %s\npassword: %s\n'%item)
#print(data)

#关闭数据库连接
db.close()
