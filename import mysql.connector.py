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
        
      
class CSVReadWrite: 
      
    def import_csv(self): 
        csv_data = csv.reader(open('/home/parag/Documents/practise/usernamemail.csv'))
        next(csv_data)
        return csv_data
    
    def write_csv_to_sql(self, csv_data, con):
        CSVReadWrite.my_cursor = con.cursor()
        for row in csv_data:
            print(row)
            CSVReadWrite.my_cursor.execute(("INSERT INTO emailid(Username, Loginemail, Identifier, Firstname, Lastname) VALUES (%s, %s, %s, %s, %s"),row)
            con.commit()       
            
    def fetch_data_after_inserting():       
        CSVReadWrite.my_cursor.execute("SELECT * FROM emailid")
        result = CSVReadWrite.my_cursor.fetchall()
        print('Inserted records:\n')
        for info in result:
            print(info)
                             
    def close_connection(self):
        CSVReadWrite.my_cursor.close()
            
            
dbConnect= MySqlConnection()
rCsv=CSVReadWrite()
con=dbConnect.create_connection()
csv_data=rCsv.import_csv()
rCsv.write_csv_to_sql(csv_data)
rCsv.close_connection()                         