from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import re


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    

  def button_1_click(self, **event_args):
    if self.radio_button_1.selected:
      if re.search(r"[#@!-'']", self.username.text) or re.search(r"[#@!-'']", self.password.text):
        alert("Keine SonderZeichen!")
      else:
        username = self.username.text
        password = self.password.text

    else:
      username = self.username.text
      password = self.password.text

    ergebnis, login = anvil.server.call('login', username, password)
    accNo = anvil.server.call('get_accNo', username, password)
    print(ergebnis)
    
    
    
    if login:
        if accNo != None:
          
          print("Hallo")

        open_form('login_Page')

  
    
    
      
