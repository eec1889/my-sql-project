import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="ec")

mycursor = mydb.cursor()

mycursor.execute("select * from student")
result = mycursor.fetchall()

print("#############################")
for i in result:
    print(f"Name: {i[0]}")
    print(f"College: {i[1]}")
    print("#############################")
    print()