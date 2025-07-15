import pymysql

dataBase = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '12345'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE CRM_db")

print("connected mysql")