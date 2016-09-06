from bibliopixel.drivers.LPD8806 import *
from bibliopixel import led
from bibliopixel import animation
from bibliopixel import colors

import time
import random
import colorsys

class multiple_lazers(animation.BaseStripAnim):
    
    def __init__(self, led,start=0, end=-1):
        super(multiple_lazers,self).__init__(led,start,end)
        self._colors = []
        self.counter = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160]
        

    def step(self, amt=1):
        self.clear()
        for i in range(0, len(self.counter)):
            color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            for j in range(0,5):
                self._led.set(self.counter[i]-j,color)
            if(self.counter[i] >= 160):
                self.counter[i] = 0
            else:
                self.counter[i]+=1
        self._step += amt

    def clear():
        self._led.fill((0,0,0))
        self._led.update()