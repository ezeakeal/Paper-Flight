from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, WipeTransition

import interface.menus as menus
import interface.game as game

class paperApp(App):
  def build(self):
    root = ScreenManager(transition=WipeTransition())
    
    MainMenu     = menus.main.Menu(name="mainmenu")
    SettingsMenu = menus.settings.SettingsMenu(name="settings")
    GameMenu     = menus.game.GameMenu(name="game")

    root.add_widget(MainMenu)
    root.add_widget(SettingsMenu)
    root.add_widget(GameMenu)

    return root
