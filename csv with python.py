import mysql.connector
import csv
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Cmile@123",
  database="emaildb"
)
mycursor = mydb.cursor()
csv_data = csv.reader(open('/home/parag/Documents/practise/username_email.csv'))
header = next(csv_data)

for row in csv_data:
    print(row)
    mycursor.execute("INSERT INTO emailid(Username, Loginemail, Identifier, Firstname, Lastname) VALUES (%s, %s, %s, %s, %s)",row)
    
mydb.commit()
mycursor.close()
