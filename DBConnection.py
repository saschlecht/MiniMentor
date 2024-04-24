import mysql.connector
from flask import Flask, Blueprint, request, jsonify, render_template, session

database_bp = Blueprint('database', __name__, static_folder="static", template_folder="templates")

@database_bp.route('/test')
def test():
  return "<h1>test</h1>"

@database_bp.route('/create-account', methods=['POST'])
def create_account():
  passedInfo = request.json.get('content')
  user = passedInfo['username']
  pw = passedInfo['password']

  #TODO check for number, capital letter, >=5 characters in pw

  #connect to database
  conn = mysql.connector.connect(host='localhost', password='rootSQL', user='root', database='minimentordb')
  if conn.is_connected():
    print("Connection established...")
  cur = conn.cursor()

  #check if username is in database
  search_stmt = (
    "SELECT * FROM userdata4 WHERE username = %s"
  )
  cur.execute(search_stmt, (user, ))
  entries = cur.fetchall();
  
  if len(entries) > 0:
    return jsonify({'username': "ERROR CODE", 'password': "Username taken, please try again"})
  
  insert_stmt = (
   "INSERT INTO userdata4 (username, password) "
   "VALUES (%s, %s)"
  )
  cur.execute(insert_stmt, (user, pw))

  conn.commit()
  conn.close()

  session['username'] = user
  session['password'] = pw

  return jsonify({'username': user, 'password': pw})

@database_bp.route('/acct-login', methods=['POST'])
def acct_login():
  #check if account is in database
  passedInfo = request.json.get('content')
  user = passedInfo['username']
  pw = passedInfo['password']

  #connect to database
  conn = mysql.connector.connect(host='localhost', password='rootSQL', user='root', database='minimentordb')
  if conn.is_connected():
    print("Connection established...")
  cur = conn.cursor()

  #check if username is in database
  search_stmt = (
    "SELECT * FROM userdata4 WHERE username = %s"
  )
  cur.execute(search_stmt, (user, ))
  entries = cur.fetchall()
  if len(entries) == 0:
    return jsonify({'username': "ERROR CODE", 'password': "Username doesn't exist, please create account or try again"})

  #check if password matches
  search_stmt2 = (
    "SELECT * FROM userdata4 WHERE username = %s AND password = %s"
  )
  cur.execute(search_stmt2, (user, pw))
  entries2 = cur.fetchall()

  if len(entries2) == 0:
    return jsonify({'username': "ERROR CODE", 'password': "Wrong password, please try again"})
  
  conn.commit()
  conn.close()

  session['username'] = user
  session['password'] = pw

  return jsonify({'username': user, 'password': pw})
  
@database_bp.route('/acct-logout', methods=['POST'])
def acct_logout():
  # connect to database
  conn = mysql.connector.connect(host='localhost', password='rootSQL', user='root', database='minimentordb')
  if conn.is_connected():
    print("Connection established...")
  cur = conn.cursor()

  # find value of user's previous logins
  search_stmt = (
    "SELECT sessions FROM userdata4 WHERE username = %s"
  )
  cur.execute(search_stmt, (session['username'], ))
  entries = cur.fetchall()

  # increment number of logins by 1
  sessionsVal = None
  for entry in entries:
    if entry[0] == None:
      sessionsVal = 1
    else:
      sessionsVal = entry[0] + 1
  update_stmt = (
    "UPDATE userdata4 SET sessions = %s WHERE username=%s"
  )
  cur.execute(update_stmt, (sessionsVal, session['username']))

  # add data collected from session to database here

  session.clear()
  conn.commit()
  conn.close()

  return jsonify({'message': 'Logout successful'})

