from Animations import alternation, bouncing_lazer, glimmer, glow

from bibliopixel.drivers.LPD8806 import *
from bibliopixel import led


class LEDManager():

    def __init__(self):

        self._driver = DriverLPD8806(
            160, c_order=ChannelOrder.RGB, use_py_spi=True, dev="/dev/spidev0.0", SPISpeed=2)
        self._leds = led.LEDStrip(self._driver, threadedUpdate=True)

        self.current_anim = None
        self.current_color = (0, 0, 0)

        self.animations = {
            'Glow': glow.glow(led=self._leds),
            'Glimmer': glimmer.glimmer(led=self._leds),
            'Alternation': alternation.alternation(led=self._leds),
            'Bouncing Lazer': bouncing_lazer.bouncing_lazer(led=self._leds)
        }

    def setAnimation(self, animation):
        if(self.current_anim):
            self.current_anim.stopThread()

        self.clear()

        self.current_color = None
        self.current_anim = self.animations[animation]
        self.current_anim.run(threaded=True, fps=30)

    def setColor(self, color):
        if(self.current_anim):
            self.current_anim.stopThread()

        self.clear()
        self.current_anim = None
        self.current_color = color

        self._leds.fill(color)
        self._leds.update()

    def clear(self):
        self._leds.fill((0, 0, 0))
        self._leds.update()
