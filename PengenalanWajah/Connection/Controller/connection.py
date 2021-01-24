import pymysql as database

#Connections
#https://www.simplifiedpython.net/python-mysql-tutorial/

db = database.connect(
    host="localhost",
    user="root",
    password="",
    db="face_reg"
)
