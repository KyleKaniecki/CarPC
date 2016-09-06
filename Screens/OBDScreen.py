import kivy
kivy.require("1.5.1")

from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label


class OBDScreen(Screen):

    def __init__(self, name="", custom_manager=None):
        Screen.__init__(self, name=name)

        self.current_page = 1

        self.obd_manager = custom_manager

        self.layout = FloatLayout()

        self.values = [Label(text="OBD", size_hint=(.5, .30), pos_hint={'x': 0, 'y': .6}, font_size=32),

                       Label(text="OBD2", size_hint=(.5, .30),
                             pos_hint={'x': .5, 'y': .6}, font_size=32),

                       Label(text="OBD3", size_hint=(.5, .30),
                             pos_hint={'x': 0, 'y': .20}, font_size=32),

                       Label(text="OBD4", size_hint=(.5, .30),
                             pos_hint={'x': .5, 'y': .20}, font_size=32)
                       ]

        self.types = [Label(text="FILLER",
                            size_hint=(.5, .1),
                            pos_hint={'x': 0, 'y': .9},
                            font_size=32),

                      Label(text="FILLER",
                            size_hint=(.5, .1),
                            pos_hint={'x': .5, 'y': .9},
                            font_size=32),

                      Label(text="FILLER",
                            size_hint=(.5, .1),
                            pos_hint={'x': 0, 'y': .5},
                            font_size=32),

                      Label(text="FILLER",
                            size_hint=(.5, .1),
                            pos_hint={'x': .5, 'y': .5},
                            font_size=32)
                      ]

        self.change = Button(
            text="Change OBD", size_hint=(.5, .20), pos_hint={'x': 0, 'y': 0}, font_size=32)
        self.main = Button(
            text="Return", size_hint=(.5, .20), pos_hint={'x': .5, 'y': 0}, font_size=32)

        self.change.bind(on_press=self.switch_commands)
        self.main.bind(on_release=self.go_to_parent)

        for i in range(4):
            self.layout.add_widget(self.values[i])
            self.layout.add_widget(self.types[i])

        self.layout.add_widget(self.change)
        self.layout.add_widget(self.main)

        self.add_widget(self.layout)

    def start(self):
        Clock.schedule_interval(self.update_values, .25)

    def stop(self):
        Clock.unschedule(self.update_values)

    def update_values(self, dt):
        responses = self.obd_manager.queryAdapter(table=self.current_page)
        counter = 0

        for key, value in responses.iteritems():
            self.types[counter].text = key
            self.values[counter].text = value
            counter += 1

    def switch_commands(self, value):

        self.current_page += 1

        if(self.current_page > 3):
            self.current_page = 1

    def go_to_parent(self, instance):
        self.stop()
        self.parent.current = "Main"
