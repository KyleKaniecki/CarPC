import kivy
kivy.require("1.5.1")

from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label

import datetime
import os


class MainScreen(Screen):

    def __init__(self, name=""):
        Screen.__init__(self, name=name)

        self.layout = FloatLayout()

        self.music = Button(text="Music",
                            size_hint=(.33, .20),
                            pos_hint={'x': 0, 'y': 0},
                            font_size=32)

        self.obd = Button(text="OBD",
                          size_hint=(.33, .20),
                          pos_hint={'x': .33, 'y': 0},
                          font_size=32)

        self.leds = Button(text="LEDs",
                           size_hint=(.34, .20),
                           pos_hint={'x': .66, 'y': 0},
                           font_size=32)

        self.clock = Label(text="TIME",
                           size_hint=(1, .8),
                           pos_hint={'x': 0, 'y': .2},
                           font_size=120)

        self.shutdown = Button(pos_hint={'x': .9, 'y': .9},
                               size_hint=(.1, .1))

        self.music.bind(on_press=self.music_callback)
        self.leds.bind(on_release=self.led_callback)
        self.obd.bind(on_release=self.obd_callback)
        self.shutdown.bind(on_press=self.shutdown_callback)

        self.layout.add_widget(self.music)
        self.layout.add_widget(self.obd)
        self.layout.add_widget(self.leds)
        self.layout.add_widget(self.clock)
        self.layout.add_widget(self.shutdown)

        self.add_widget(self.layout)

        Clock.schedule_interval(self.update_clock, .25)

    def music_callback(self, instance):
        self.parent.current = "Music"

    def led_callback(instance, value):
        instance.parent.current = "LEDs"

    def obd_callback(self, instance):
        self.parent.current = "OBD"
        self.parent.current_screen.start()

    def update_clock(self, value):
        current = datetime.datetime.now()

        time = ""
        if(current.hour > 12):
            time += str(current.hour-12)

        time += ":"

        if(current.minute < 10):
            time += ("0" + str(current.minute))
        else:
            time += str(current.minute)

        time += ":"

        if(current.second < 10):
            time += ("0" + str(current.second))
        else:
            time += str(current.second)

        self.clock.text = time

    def shutdown_callback(self, value):
        os.system("sudo shutdown -h now")
