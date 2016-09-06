from bibliopixel.drivers.LPD8806 import *
from bibliopixel import led
from bibliopixel import animation
from bibliopixel import colors

import time
import random
import colorsys

class stack(animation.BaseStripAnim):
    def __init__(self,led,start=0,end=-1):
        super(stack,self).__init__(led,start,end)
        self.current = 0
        self.stop = 160
        self.color = (255,0,0)

    def step(self, amt=1):
        if self.current >= self.stop:
            self.current = 0
            self.stop -= 5
            self._step += amt
            self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            
        for i in range(self.current, self.current-5,-1):
            self._led.set(i,self.color)
        for i in range(self.current-5, self.current-10, -1):
            self._led.set(i,(0,0,0))
        self.current += 5

        if(self.stop <= 0):
            self.current = 0
            self.stop = 160
            self.clear()

    def clear():
        self._led.fill((0,0,0))
        self._led.update()
