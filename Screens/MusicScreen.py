import kivy
kivy.require("1.5.1")

from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class MusicScreen(Screen):

    def __init__(self, name=""):
        Screen.__init__(self, name=name)

        self.layout = FloatLayout()

        self.playback = Button(text="Current Playback",
                               pos_hint={'x': 0, 'y': 0},
                               size_hint=(.33, .1))

        self.queue = Button(text="Queue",
                            pos_hint={'x': .33, 'y': 0},
                            size_hint=(.33, .1))

        self.go_back = Button(text="Return",
                              pos_hint={'x': .66, 'y': 0},
                              size_hint=(.34, .1))

        self.go_back.bind(on_release=self.go_to_main)

        self.layout.add_widget(self.go_back)
        self.layout.add_widget(self.queue)
        self.layout.add_widget(self.playback)

        self.add_widget(self.layout)

    def go_to_main(self, value):
        self.parent.current = "Main"
