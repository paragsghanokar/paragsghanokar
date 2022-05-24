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
        
        
class ReadCsv:   
    
              
    def import_csv(self,conn):
        ReadCsv.myCursor = conn.cursor() 
        csvData = csv.reader(open('/home/parag/Documents/practise/username_email.csv'))
        header = next(csvData)
        return csvData
     
         
    def write_csv_to_sql(self,csvData):
        for row in csvData:
            print(row)
            ReadCsv.myCursor.execute("INSERT INTO emailid(Username, Loginemail, Identifier, Firstname, Lastname) VALUES (%s, %s, %s, %s, %s)",row)
            conn.commit()
        ReadCsv.myCursor.execute("SELECT * FROM emailid")
        database_result = ReadCsv.myCursor.fetchall()
        print('Inserted records:\n')
        for x in database_result:
            print(x)            
               
               
    def close_connection(self):
        ReadCsv.myCursor.close()
            
dbConnect= MySqlConnection()
rCsv=ReadCsv()
conn=dbConnect.create_connection()
csvData=rCsv.import_csv(conn)
rCsv.write_csv_to_sql(csvData)
rCsv.close_connection()

