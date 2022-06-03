import mysql.connector
import csv


class CSVRead:
      
      def import_csv(self):
        csv_data = csv.reader(open('/home/parag/Documents/practise/usernamemail.csv'))
        next(csv_data)
        return csv_data


class SqlExecution:
  
    def create_connection(self):
        CONST_DB = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Cmile@123",
        database="emaildb"
        )
        return  CONST_DB
        
    def write_csv_to_sql(self, csv_data):    
        db_cursor=con.cursor()
        for row in csv_data:
            print(row)
            first_query = "INSERT INTO emailid(Username, Loginemail, Identifier, Firstname, Lastname) VALUES (%s, %s, %s, %s, %s)"
            db_cursor.execute(first_query,row)
            con.commit()
        return db_cursor
        
    def display_data(self, db_cursor):
        second_query=("SELECT * FROM emailid")       
        db_cursor.execute(second_query)
        result = db_cursor.fetchall()
        print('Inserted records:\n')
        for info in result:
            print(info)
              
    def close_connection(self):
        db_cursor.close()
            
            
db_connect= SqlExecution()
r_csv=CSVRead()
con=db_connect.create_connection()
csv_data=r_csv.import_csv()
db_cursor=db_connect.write_csv_to_sql(csv_data)
db_connect.display_data(db_cursor)
db_connect.close_connection()     
