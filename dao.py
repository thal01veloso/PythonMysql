import mysql.connector
host = 'localdb'
user = 'user01'
passwd='1234'
db = 'BASE01'
cnx = mysql.connector.connect(user='user01', password='1234',
                              host='localhost',
                              database='BASE01')
cursor = cnx.cursor()

query = 'CREATE TABLE IF NOT EXISTS alunos(ID INT null);'
cursor.execute(query)
cnx.close()
