from ._anvil_designer import login_PageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class login_Page(login_PageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
   
    # Any code you write here will run before the form opens.
    self.url = anvil.js.window.location.href
    self.accNo = anvil.server.call('get_accountNumber_from_query', self.url)
    if (self.accNo == None):
      self.rich_text_1.content = "Login Successful but AccountNo was not passed."
    else:
      
      self.username = anvil.server.call('get_username_from_id', self.accNo)
      self.rich_text_1.content = f"Welcome {self.username}. Your balance is {anvil.server.call('get_balance',self.accNo)}."
