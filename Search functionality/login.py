from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MainWindow(BoxLayout):
        pass

class Myapp(App):
    def build(self):
        return MainWindow()

if __name__ == '__main__':
        Myapp().run()
