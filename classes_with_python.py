import mysql.connector
import csv


class CSVRead:
      
      def import_csv(self):
        csv_data = csv.reader(open('/home/parag/Documents/practise/usernamemail.csv'))
        next(csv_data)
        return csv_data


class MySqlExecution:
  
    def create_connection(self):
        LOCAL_DB = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Cmile@123",
        database="emaildb"
        )
        return  LOCAL_DB
        
    def write_csv_to_sql(self, csv_data):    
        my_cursor=con.cursor()
        for row in csv_data:
            print(row)
            query_1 = "INSERT INTO emailid(Username, Loginemail, Identifier, Firstname, Lastname) VALUES (%s, %s, %s, %s, %s)"
            my_cursor.execute(query_1,row)
            con.commit()
        return myCursor
        
    def fetch_data_from_table(self, my_cursor):
        query_2=("SELECT * FROM emailid")       
        my_cursor.execute(query_2)
        result = my_cursor.fetchall()
        print('Inserted records:\n')
        for info in result:
            print(info)
              
    def close_connection(self):
        myCursor.close()
            
            
dbConnect= MySqlExecution()
rCSV=CSVRead()
con=dbConnect.create_connection()
csv_data=rCSV.import_csv()
my_cursor=dbConnect.write_csv_to_sql(csv_data)
dbConnect.fetch_data_from_table(my_cursor)
dbConnect.close_connection()    

