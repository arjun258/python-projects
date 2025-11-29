import mysql.connector as mysql
def delete():
    myconn = mysql.connect(host = "127.0.0.1", user = "root ", password = "root", database = "emp")
    mycursor = myconn.cursor()
    mycursor.execute("DELETE FROM employee WHERE E_code = 'E101'")
    myconn.commit()
    print("Deleted successfully")
delete()