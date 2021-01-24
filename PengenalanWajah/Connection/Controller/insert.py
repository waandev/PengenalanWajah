from Connection.Controller.connection import db

def InsertUser():
    name = input('Enter Your Name: ')
    age = int(input('Enter Your Age: '))
    gender = input('Enter Your Gender: ')
    desc = input('Enter Your Personal Description : ')
    sql = "Insert Into user (`name`,`age`,`gender`,`Description`) values (%s, %s, %s, %s)"
    try:
        with db.cursor() as cursor:
            try:
                cursor.execute(sql, (name,age,gender,desc))
                print("User Inserted")
            except:
                print("Oops! Something Wrong")
            db.commit()
    finally:
        print('')


# InsertItem();
