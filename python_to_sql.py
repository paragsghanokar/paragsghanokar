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
        
             
    def import_csv(self,conn):
        
        MySqlConnection.myCursor = conn.cursor() 
        csvData = csv.reader(open('/home/parag/Documents/practise/username_email.csv'))
        header = next(csvData)
        return csvData
     
         
    def write_csv_to_sql(self,csvData):
        for row in csvData:
            print(row)
            MySqlConnection.myCursor.execute("INSERT INTO emailid(Username, Loginemail, Identifier, Firstname, Lastname) VALUES (%s, %s, %s, %s, %s)",row)
            conn.commit()
        MySqlConnection.myCursor.execute("SELECT * FROM emailid")
        database_result = MySqlConnection.myCursor.fetchall()
        print('Inserted records:\n')
        for x in database_result:
            print(x)            
               
                
    def close_connection(self):
        MySqlConnection.myCursor.close()
            
dbConnect= MySqlConnection()
conn=dbConnect.create_connection()
csvData=dbConnect.import_csv(conn)
dbConnect.write_csv_to_sql(csvData)
dbConnect.close_connection()
