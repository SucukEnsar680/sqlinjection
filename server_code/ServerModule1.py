import anvil.server
import sqlite3
def init_db():
  adminname = 'davidProf'
  adminpwd = 'kannNichtCoden'
  accountNumbers = [4509693768556941, 4509693768521313, 69826208285551123123]
  
  db = data_files["datenbank.db"]
  cursor = db.cursor()
  cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                          AccountNo INTEGER,
                          username TEXT,
                          password TEXT
                        )''')
  cursor.execute('''CREATE TABLE IF NOT EXISTS Balances (
                              AccountNo INTEGER,
                              balance INTEGER
                            )''')
  # Insert sample data
  cursor.execute(f"INSERT INTO Users (AccountNo, username, password) VALUES ({accountNumbers[0]}, '{adminname}', '{adminpwd}')")
  cursor.execute(f"INSERT INTO Users (AccountNo, username, password) VALUES ({accountNumbers[1]}, 'frodo', 'DerEineRing')")
  cursor.execute(f"INSERT INTO Users (AccountNo, username, password) VALUES ({accountNumbers[2]}, 'glorfindel', 'Unsterblicher')")
  
  cursor.execute(f"INSERT INTO Balances (AccountNo, balance) VALUES ({accountNumbers[0]}, 5000)")
  cursor.execute(f"INSERT INTO Balances (AccountNo, balance) VALUES ({accountNumbers[1]}, 1500)")
  cursor.execute(f"INSERT INTO Balances (AccountNo, balance) VALUES ({accountNumbers[2]}, 7500)")
  db.commit()
