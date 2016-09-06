from bibliopixel.drivers.LPD8806 import *
from bibliopixel import led
from bibliopixel import animation
from bibliopixel import colors

import random


class alternation(animation.BaseStripAnim):
    def __init__(self,led,start=0,end=-1):
        super(alternation,self).__init__(led,start,end)
        self.odds = True
        
    def step(self, amt= 1):
        
        self.clear()
        if(self.odds == True):
            for i in range(0,160,2):
                self._led.set(i,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            self.odds = False
        else:
            for i in range(1,160,2):
                self._led.set(i,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            self.odds = True
        self._step += amt

    def clear():
        self._led.fill((0,0,0))
        self._led.update()
        