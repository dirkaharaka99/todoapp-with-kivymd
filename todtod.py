import kivy
import kivy
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty
import datetime
from datetime import date
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivy.core.window import Window
Window.size = (350, 600)


class TodoCard(FakeRectangularElevationBehavior, MDFloatLayout):
    pass


class TodoApp(MDApp):

    def build(self):

        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("Main.kv"))
        return screen_manager


if __name__ == "__main__":
    TodoApp().run()
