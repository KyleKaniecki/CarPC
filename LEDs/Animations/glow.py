from bibliopixel.drivers.LPD8806 import *
from bibliopixel import led
from bibliopixel import animation
from bibliopixel import colors

import time
import random
import colorsys

class glow(animation.BaseStripAnim):
    def __init__(self,led,start=0,end=-1,red=0,blue=0,green=175):
        super(glow,self).__init__(led,start,end)
        self.time = 0
        self.hue = colorsys.rgb_to_hsv(blue,red,green)[0]
        self.subtract = False
        self.rgbcolor = colorsys.hsv_to_rgb(self.hue,1,(int(self.time)%100)*.01)

    def step(self, amt=1):
        self._led.fill((20+int(self.rgbcolor[0]*(255-20)),int(self.rgbcolor[1]*255),int(self.rgbcolor[2]*255)))
        self.rgbcolor = colorsys.hsv_to_rgb(self.hue,1,(self.time%100)*.01)

        if self.subtract:
            self.time -= 1
            if self.time <= 0:
                self.subtract = False
        else:
            self.time += 1
            if self.time >= 99:
                self.subtract = True
        
        self._step += amt
