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
  conn = sqlite3.connect(data_files["users1.db"])
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

@anvil.server.callable
def get_accNo(username, password):
  conn = sqlite3.connect(data_files["users1.db"])
  cursor = conn.cursor()
  cursor.execute(f"SELECT AccountNo FROM Users WHERE username = '{username}' AND password = '{password}'")
  result = cursor.fetchone()
  if (result):
    return result[0]
  else:
    return None
  
    
@anvil.server.callable
def get_accountNumber_from_query(url):
    query_string = url.split('?')[-1] if '?' in url else ''
    if query_string:
      query_params = urllib.parse.parse_qs(query_string)
      if "AccountNo" in query_params:
        return query_params["AccountNo"][0]
    return None

@anvil.server.callable
def get_username_from_id(id):
  con = sqlite3.connect(data_files["users1.db"])
  cursor = con.cursor()
  query = "SELECT username FROM Users WHERE AccountNo = ?"
  res = list(cursor.execute(query, (id,)))
  return res[0][0]