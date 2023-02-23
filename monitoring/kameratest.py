import os
import time
import mysql.connector

time.sleep(1)
    
mydb = mysql.connector.connect(
  host="localhost",
  user="bigfella",
  password="G2023m2!!!",
  database="monitoring"
)


def isitempty(path):
    return os.stat(path).st_size == 0

if isitempty("/home/bigfella/Desktop/v3/monitoring/kameraproces") == 0 and isitempty("/home/bigfella/Desktop/v3/monitoring/emailproces") == 0 :
    mycursor = mydb.cursor()
    mycursor.execute("UPDATE sistem SET status = 1 WHERE aktivnost = 'kameramon'")
    mydb.commit()

else:
    mycursor = mydb.cursor()
    mycursor.execute("UPDATE sistem SET status = 0 WHERE aktivnost = 'kameramon'")
    mydb.commit()

# POKRENUTI CRONJOB svaki minut koji ce da pokrene ps -aux | .... + ovu skriptu koja ce da iscita sadrzaj amialie fajla i na osnovu toga parsuje mysql-u.



