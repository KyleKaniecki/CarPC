
from bibliopixel.drivers.LPD8806 import *
from bibliopixel import led
from bibliopixel import animation
from bibliopixel import colors

import time
import random
import colorsys


class glimmer(animation.BaseStripAnim):
    def __init__(self,led,start=0,end=-1):
        super(glimmer,self).__init__(led,start,end)
        
    def step(self, amt=1):
        for i in range(0,160):
            temp = self._led.get(i)
            if(temp[0]-10 < 0):
                self._led.set(i,(0,0,0))
            else:
                self._led.set(i,(temp[0]-10,temp[1]-10,temp[2]-10))
        for i in range(0,5):
            self._led.set(random.randint(0,160),(175,175,175))

        self._step += amt
