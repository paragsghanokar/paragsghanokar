import mysql.connector
import csv
class MySqlConnection:
    
    
    def create_connection(self):
        MYDB = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Cmile@123",
        database="emaildb"
        )
        
             
    def import_csv(self):  
        myCursor = MYDB.cursor() 
        csv_Data = csv.reader(open('/home/parag/Documents/practise/username_email.csv'))
        header = next(csv_Data)
     
        
       
    def write_csv(self):
        for row in csv_Data:
            print(row)
            myCursor.execute("INSERT INTO emailid(Username, Loginemail, Identifier, Firstname, Lastname) VALUES     (%s, %s, %s, %s, %s)",row)
    
            MYDB.commit()
                
               
    def close_connection(self):
        myCursor.close()
            
d1= MySqlConnection()
d1.create_connection()
d1.import_csv()
d1.write_csv()
d1.close_connection()       