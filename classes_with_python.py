import mysql.connector
import csv


class CsvRead:
      
      
      def import_csv(self,con):
        csvData = csv.reader(open('/home/parag/Documents/practise/usernamemail.csv'))
        next(csvData)
        return csvData


class MySqlConnection:

        
    def create_connection(self):
        MY_DB = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Cmile@123",
        database="emaildb"
        )
        return  MY_DB
        

    def write_csv_to_sql(self,csvData):
        CsvRead.myCursor=con.cursor()
        for row in csvData:
            print(row)
            CsvRead.myCursor.execute("INSERT INTO emailid(Username, Loginemail, Identifier, Firstname, Lastname) VALUES (%s, %s, %s, %s, %s)",row)
            con.commit()
            
        CsvRead.myCursor.execute("SELECT * FROM emailid")
        databaseResult = CsvRead.myCursor.fetchall()
        print('Inserted records:\n')
        for x in databaseResult:
            print(x)
    
                
    def close_connection(self):
        CsvRead.myCursor.close()
            
            
dbConnect= MySqlConnection()
rCsv=CsvRead()
con=dbConnect.create_connection()
csvData=rCsv.import_csv(con)
dbConnect.write_csv_to_sql(csvData)
dbConnect.close_connection()

