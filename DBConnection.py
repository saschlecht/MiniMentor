import mysql.connector
import hashlib

#connect to database
conn = mysql.connector.connect(host='localhost', password='rootSQL', user='root', database='minimentordb')
if conn.is_connected():
	print("Connection established...")
cur = conn.cursor()

#take user input - will be from SignUp.html
user = input("Enter username: ")
pw = input("Enter password: ")

#TODO check if username is in database
#TODO check for number, capital letter, >=5 characters in pw

pw = hashlib.sha256(pw.encode()).hexdigest()	#encode password

insert_stmt = (
  "INSERT INTO userdata4 (username, password) "
  "VALUES (%s, %s)"
)
cur.execute(insert_stmt, (user, pw))

conn.commit()
