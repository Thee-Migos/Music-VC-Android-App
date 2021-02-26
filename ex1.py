import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup

class CommitPopup(Popup):
    pass

class Ex1(BoxLayout):
        searchedTextObjProp = ObjectProperty(None)

        def btn(self):
                print("The searched word is :" + self.searchedTextObjProp.text)
        
        def select(self ,*args):
                try:
                        self.label.text = args[1][0]
                except: 
                        pass

        # For Switch
        def switch_on(self, instance, value):
                if value is True:
                        print("Switch On")
                else:
                        print("Switch Off")

        def open_popup(self):
                the_popup = CommitPopup()
                the_popup.open()
 
 


class Ex1App(App):                
        def build(self):
                return Ex1()

if __name__ == '__main__':
        Ex1App().run()
