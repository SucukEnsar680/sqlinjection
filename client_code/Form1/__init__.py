from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    

  def button_1_click(self, **event_args):
    username = self.username.text
    password = self.password.text

    ergebnis, login = anvil.server.call('login', username, password)
    accNo = anvil.server.call('get_accNo', username, password)
    print(ergebnis)
    
    
    
    if login:
        if accNo != None:
          
          print("Hallo")
          print(anvil.js.window.location.href)
          anvil.js.window.location.href = anvil.js.window.location.href + "?AccountNo=" + str(accNo[0])
        open_form('login_Page')
    
      
