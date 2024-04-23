import mysql.connector
import hashlib
from flask import Flask, Blueprint, request, jsonify, render_template

database_bp = Blueprint('database', __name__, static_folder="static", template_folder="templates")

@database_bp.route('/test')
def test():
  return "<h1>test</h1>"

@database_bp.route('/create-account', methods=['POST'])
def create_account():
  passedInfo = request.json.get('content')
  user = passedInfo['username']
  pw = passedInfo['password']

  #connect to database
  #conn = mysql.connector.connect(host='localhost', password='rootSQL', user='root', database='minimentordb')
  #if conn.is_connected():
  #  print("Connection established...")
  #cur = conn.cursor()

  #TODO check if username is in database
  #TODO check for number, capital letter, >=5 characters in pw

  #pw = hashlib.sha256(pw.encode()).hexdigest()  #encode password

  #insert_stmt = (
  #  "INSERT INTO userdata4 (username, password) "
  #  "VALUES (%s, %s)"
  #)
  #cur.execute(insert_stmt, (user, pw))

  #conn.commit()

  return jsonify({'username': user, 'password': pw})
