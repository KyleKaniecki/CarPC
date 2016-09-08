import kivy
kivy.require("1.5.1")

from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.slider import Slider
from kivy.uix.label import Label


class SliderScreen(Screen):

    def __init__(self, name="", custom_manager=None):
        Screen.__init__(self, name=name)

        self.layout = FloatLayout()

        self.led_manager = custom_manager

        self.labels = [Label(text="Red Color: ",
                             pos_hint={'x': 0, 'y': .45},
                             size_hint=(1, .05),
                             font_size=32),
                       Label(text="Green Color: ",
                             pos_hint={'x': 0, 'y': .70},
                             size_hint=(1, .05),
                             font_size=32),
                       Label(text="Blue Color: ",
                             pos_hint={'x': 0, 'y': .95},
                             size_hint=(1, .05),
                             font_size=32)
                       ]

        self.sliders = [Slider(min=0,
                               max=255,
                               value=self.led_manager.current_color[1],
                               pos_hint={'x': 0, 'y': .75},
                               size_hint=(1, .20)),
                        Slider(min=0,
                               max=255,
                               value=self.led_manager.current_color[1],
                               pos_hint={'x': 0, 'y': .5},
                               size_hint=(1, .20)),
                        Slider(min=0,
                               max=255,
                               value=self.led_manager.current_color[1],
                               pos_hint={'x': 0, 'y': .25},
                               size_hint=(1, .20))
                        ]

        self.save_changes = Button(text="Save Changes", pos_hint={'x': 0, 'y': 0}, size_hint=(1, .25), font_size=32)
        self.save_changes.bind(on_release=self.save)

        for i in range(3):
            self.layout.add_widget(self.sliders[i])
            self.layout.add_widget(self.labels[i])

        self.layout.add_widget(self.save_changes)

        self.add_widget(self.layout)

    def start(self):
        Clock.schedule_interval(self.update, .5)

    def update(self, value):
        self.led_manager.setColor(
            (int(self.sliders[0].value), int(self.sliders[1].value), int(self.sliders[2].value)))

        for i in range(3):
            self.labels[i].text = (self.labels[i].text[:len(self.labels[i].text) - len(str(int(self.sliders[i].value)))] + "%d") % self.sliders[i].value

    def save(self, value):

        Clock.unschedule(self.update)

        self.parent.current = "LEDs"
