import mysql.connector
import csv


class CSVRead:
      
      def import_csv(self):
        csv_data = csv.reader(open('/home/parag/Documents/practise/usernamemail.csv'))
        next(csv_data)
        return csv_data


class MySqlExecution:
  
    def create_connection(self):
        MY_DB = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Cmile@123",
        database="emaildb"
        )
        return  MY_DB
        
    def write_csv_to_sql(self, csv_data):    
        myCursor=con.cursor()
        for row in csv_data:
            print(row)
            query_1 = "INSERT INTO emailid(Username, Loginemail, Identifier, Firstname, Lastname) VALUES (%s, %s, %s, %s, %s)"
            myCursor.execute(query_1,row)
            con.commit()
        return myCursor
        
    def fetch_data_from_table(self, myCursor):
        query_2=("SELECT * FROM emailid")       
        myCursor.execute(query_2)
        result = myCursor.fetchall()
        print('Inserted records:\n')
        for info in result:
            print(info)
              
    def close_connection(self):
        myCursor.close()
            
            
dbConnect= MySqlExecution()
rCSV=CSVRead()
con=dbConnect.create_connection()
csv_data=rCSV.import_csv()
myCursor=dbConnect.write_csv_to_sql(csv_data)
dbConnect.fetch_data_from_table(myCursor)
dbConnect.close_connection()    

