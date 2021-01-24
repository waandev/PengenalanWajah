from Connection.Controller.connection import db
from Connection.Controller.read import ReadUser
from Connection.Controller.insert import InsertUser
from Connection.Controller.delete import DeleteUser
from Connection.Controller.edit import EditUser
from Connection.Controller.get_user import GetUser

def check_connections():
    result = 0;
    try:
        try:
            db
            print("Connection Established")
            result = 1
        except (RuntimeError, TypeError, NameError):
            print('something happened')
    finally:
        return result

def read_user():
    return ReadUser()

def insert_user():
    return InsertUser()

def update_user():
    return EditUser(int(input("Enter Id to update : ")))

def delete_user():
    return DeleteUser(int(input("Enter Id to update : ")))

def get_user(id):
    return GetUser(id);

def CloseDatabase():
    return db.close()
