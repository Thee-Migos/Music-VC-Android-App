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
        
        #vanilla backend methods aren't required to take in self as a parmeter
        def init_system(prefix_dir):
                #creates a new directory /prefix_dir/Master
                #prefix_dir is a string containing the root directory for all our repos

                pass

        def set_folder_as_default():
                pass

        def upload_to_server(self):
                #uploads current default local repo
                #somewhere in else the backend we'll have to keep track
                #of all our local repos, the repo/folder thats currently set
                #qs default will be the one which is uploaded 

                print("Uploading to Server...")

        def search(self):
                pass
      
 
 


class Ex1App(App):                
        def build(self):
                return Ex1()

if __name__ == '__main__':
        Ex1App().run()
