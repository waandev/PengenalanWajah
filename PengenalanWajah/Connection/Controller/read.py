from Connection.Controller.connection import db

def ReadUser():
    try:
        with db.cursor() as cursor:
            sql = "Select * from User"
            try:
                cursor.execute(sql)
                result = cursor.fetchall()
                print("Id\t Name\t\tAge\tGender\tDescription")
                print("========================================================================================================")
                for row in result:
                    print(str(row[0])+"\t"+row[1]+"\t"+str(row[2])+"\t"+row[3]+"\t"+row[4])
            except:
                print("Oops!!! Something Wrong")
        db.commit()
    finally:
        print("")

# ReadUser()
