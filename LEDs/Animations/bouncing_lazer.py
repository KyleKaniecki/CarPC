from bibliopixel.drivers.LPD8806 import *

from bibliopixel import animation
from bibliopixel import colors

import random

class bouncing_lazer(animation.BaseStripAnim):
    
    def __init__(self, led, start=0, end=-1):
        super(bouncing_lazer,self).__init__(led,start,end)
        self._colors = [colors.Red,colors.Teal, colors.DarkCyan, colors.Violet, colors.Amethyst, colors.GreenYellow]

    def step(self, amt=1):
        self.led.fill((0,0,0))
        for i in range(self._step,self._step+5):
                if i >= 160:
                    self._step = 0
                    self._led.set(i-159,self._colors[random.randint(0,5)])
                else:
                    self._led.set(i,self._colors[random.randint(0,5)])
        self._step += amt