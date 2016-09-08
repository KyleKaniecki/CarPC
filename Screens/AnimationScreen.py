import kivy
kivy.require("1.5.1")

from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class AnimationScreen(Screen):

    def __init__(self, name="", custom_manager=None):
        Screen.__init__(self, name=name)

        self.layout = FloatLayout()

        self.led_manager = custom_manager

        self.anim1 = Button(text="Glow",
                            size_hint=(.5, .33),
                            pos_hint={'x': 0, 'y': .67},
                            font_size=32)

        self.anim2 = Button(text="Glimmer",
                            size_hint=(.5, .33),
                            pos_hint={'x': .5, 'y': .67},
                            font_size=32)

        self.anim3 = Button(text="Alternation",
                            size_hint=(.5, .33),
                            pos_hint={'x': 0, 'y': .34},
                            font_size=32)

        self.anim4 = Button(text="Bouncing Lazer",
                            size_hint=(.5, .33),
                            pos_hint={'x': .5, 'y': .34},
                            font_size=32)

        self.return_button = Button(text="Return",
                                    size_hint=(1, .34),
                                    pos_hint={'x': 0, 'y': 0},
                                    font_size=32)

        self.return_button.bind(on_press=self.go_back)

        self.anim1.bind(on_press=self.animation_callback)
        self.anim2.bind(on_press=self.animation_callback)
        self.anim3.bind(on_press=self.animation_callback)
        self.anim4.bind(on_press=self.animation_callback)

        self.layout.add_widget(self.anim1)
        self.layout.add_widget(self.anim2)
        self.layout.add_widget(self.anim3)
        self.layout.add_widget(self.anim4)
        self.layout.add_widget(self.return_button)

        self.add_widget(self.layout)

    def animation_callback(self, value):

        self.led_manager.setAnimation(value.text)

    def go_back(self, value):
        self.parent.current = "LEDs"
