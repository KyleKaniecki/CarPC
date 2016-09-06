#!/usr/bin/python

# ---------------------KIVY IMPORTS---------------------------------
import kivy
kivy.require("1.5.1")
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager


# -----------------------OTHER IMPORTS--------------------------------
from OBD.OBDManager import OBDManager
from LEDs.LEDManager import LEDManager
from Screens import MusicScreen, MainScreen, OBDScreen, SliderScreen, LEDScreen, AnimationScreen
import os


class TestApp(App):

    def build(self):

        # os.system("sudo rfcomm bind 00:1D:A5:00:04:A9")

        # Build and initialize managers that handle logic
        sm = ScreenManager()
        obdmanager = OBDManager()
        ledmanager = LEDManager()

        # Build the screens that will display the info
        music = MusicScreen.MusicScreen(name="Music")
        main = MainScreen.MainScreen(name="Main")
        obd = OBDScreen.OBDScreen(name="OBD", custom_manager=obdmanager)
        sliders = SliderScreen.SliderScreen(name="Sliders", custom_manager=ledmanager)
        leds = LEDScreen.LEDScreen(name="LEDs")
        anims = AnimationScreen.AnimationScreen(
            name="Anims", custom_manager=ledmanager)

        # Add the screens to the ScreenManager so it can manage them
        sm.add_widget(music)
        sm.add_widget(main)
        sm.add_widget(obd)
        sm.add_widget(sliders)
        sm.add_widget(leds)
        sm.add_widget(anims)

        # Set the current screen to the main screen
        sm.current = "Main"
        return sm

if __name__ == "__main__":
    app = TestApp()
    try:
        app.run()
    except (Exception, StandardError) as e:
        import traceback
        errorlog = open("/home/pi/CarPC/errors.txt", "a+")
        errorrrrrr = traceback.format_exc()
        errorlog.write(errorrrrrr + '\n')
        print errorrrrrr
