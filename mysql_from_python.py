import os
import pymysql

#Get username from Clould( workspace)
# (modify this variable if running on another envirmoent)

username = os.getenv("C9_USER")

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

                             
try:
    #Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * from Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection, reagrdless of whether the above was successful
    connection.close()