from kivy.app import App
from kivy.uix.button import Button

class mainmenu(App):
  def menu_build(self):
    return Button(text='Play')

  def build(self):
    return menu_build()