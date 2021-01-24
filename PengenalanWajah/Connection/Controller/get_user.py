from Connection.Controller.connection import db

def GetUser(id):
    sql="select * from user where id=%s"
    name = ''
    age = ''
    gender = ''
    desc = ''
    try:
        with db.cursor() as cursor:
            try:
                cursor.execute(sql,(id,))
                result = cursor.fetchone()
                name = result[1]
                age = str(result[2])
                gender = result[3]
                desc = result[4]
            except:
                print("error")
        db.commit()
    finally:
        # print(name+age+gender+desc)
        return name,age,gender,desc

# GetUser(1)
