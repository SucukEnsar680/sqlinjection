import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3

adminname = 'davidProf'
adminpwd = 'kannNichtCoden'

@anvil.server.callable
def login(username, password):
  conn = sqlite3.connect(data_files["users.db"])
  cursor = conn.cursor()
  query = f"SELECT username FROM Users WHERE username = '{username}' AND password = '{password}'"
  try:
      cursor = cursor.execute(query)
  except Exception as e:
      return f"Login failed!<br>{query}<br>{e}"

  user = cursor.fetchone()
  login = False 
  accountNo = None
  if user and username == user[0]:
      accountNo = cursor.execute(f"SELECT AccountNo FROM users WHERE username = '{username}'").fetchone()
  if user and username == user[0] and username == adminname:
      query = f"SELECT password FROM Users WHERE username = '{username}' AND password = '{password}'"
      pw = cursor.execute(query).fetchone()
      if pw and password == pw[0] and password == adminpwd:
          return "Congratulations you finished the task!", login
  
  if user:
    login = True
    return accountNo, login
  else:
      return f"Login failed!<br>{query}", login
  