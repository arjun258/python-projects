import mysql.connector as ctor

dbcon = ctor.connect(host = "127.0.0.1", user = "root", passwd = "root", database = "Q18")
cursor = dbcon.cursor()

sql1 = "DELETE FROM category WHERE name= %s "
data1 = ('Stockable',)
cursor.execute(sql1, data1)

dbcon.commit()   


dbcon.close()
