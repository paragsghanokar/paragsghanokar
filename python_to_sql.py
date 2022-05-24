import mysql.connector
import csv
class MySqlConnection:
    
    
    def create_connection(self):
        MY_DB = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Cmile@123",
        database="emaildb"
        )
        return  MY_DB
        
             
    def import_csv(self,con):
        
        MySqlConnection.mycursor = con.cursor() 
        csvData = csv.reader(open('/home/parag/Documents/practise/username_email.csv'))
        header = next(csvData)
        return csvData
     
         
    def write_csv_to_sql(self,csvData):
        for row in csvData:
            print(row)
            MySqlConnection.mycursor.execute("INSERT INTO emailid(Username, Loginemail, Identifier, Firstname, Lastname) VALUES (%s, %s, %s, %s, %s)",row)
            con.commit()
            print(MySqlConnection.mycursor.rowcount, "record inserted.")      
               
    def close_connection(self):
        MySqlConnection.mycursor.close()
            
d1= MySqlConnection()
con=d1.create_connection()
csvData=d1.import_csv(con)
d1.write_csv_to_sql(csvData)
d1.close_connection()
