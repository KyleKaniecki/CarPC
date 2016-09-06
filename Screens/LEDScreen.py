import kivy
kivy.require("1.5.1")

from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label


class LEDScreen(Screen):

    def __init__(self, name=""):
        Screen.__init__(self, name=name)

        self.layout = FloatLayout()

        self.color = Label(text="Pick a Color or Animation",
                           pos_hint={'x': 0, 'y': .67},
                           size_hint=(1, .33),
                           font_size=32)

        self.animations = Button(text="Pick Animation",
                                 pos_hint={'x': 0, 'y': .34},
                                 size_hint=(1, .33),
                                 font_size=32)

        self.sliders = Button(text="Custom Color",
                              pos_hint={'x': 0, 'y': 0},
                              size_hint=(.5, .34),
                              font_size=32)

        self.main = Button(text="Return",
                           pos_hint={'x': .5, 'y': 0},
                           size_hint=(.5, .34),
                           font_size=32)

        self.main.bind(on_release=self.go_to_main)
        self.sliders.bind(on_release=self.go_to_sliders)

        self.layout.add_widget(self.color)
        self.layout.add_widget(self.animations)
        self.layout.add_widget(self.sliders)
        self.layout.add_widget(self.main)

        self.add_widget(self.layout)

    def go_to_main(instance, value):
        instance.parent.current = "Main"

    def go_to_anims(instance, value):
        instance.parent.current = "Anims"

    def go_to_sliders(instance, value):
        instance.parent.current = "Sliders"
        instance.parent.current_screen.start()
