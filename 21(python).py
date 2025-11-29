import mysql.connector as mysql
def sql_data():
    con1 = mysql.connect(host = "127.0.0.1", user = "root", password = "root", database = "Q18")
    mycursor = con1.cursor()
    print("Students with marks greater than 75 are:")
    mycursor.execute("select Name from student where marks>75")
    data = mycursor.fetchall()

    for i in data:
        print(i)
    print()
sql_data()