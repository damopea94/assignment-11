import mysql.connector
connection=mysql.connector.connect("localhost","root","python3020","pydb")#established connection between your database
cursor=connection.cursor()#cursor() method create a cursor object
cursor.execute("create table tstudent(stuid INT,stuname varchar(255),major varchar(255),stuyear INT,tuition INT )")#Execute SQL Query to create a table into your database
print("table tstudent created")
connection.close()#Connection Close
