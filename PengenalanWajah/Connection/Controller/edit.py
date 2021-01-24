from Connection.Controller.connection import db

def EditUser(id):
    sql = "update user set `name`=%s, `description`=%s, `age`=%s, `gender`=%s where id=%s"
    name = input('Insert Your Name : ')
    age = int(input('Insert Your Age : '))
    gender = input('Insert Your Gender : ')
    desc = input('Insert Your Description : ')
    try:
        with db.cursor() as cursor:
            try:
                cursor.execute(sql,(name,desc,age,gender,id))
                print('Succesfully Updated')
            except:
                print('Oops! Something Went Wrong.... *is it your face?*')
            db.commit()
    finally:
        print('')

# EditUser(int(input('Input Id : ')))
