import pandas as pd
import numpy as np
from gpiozero import Button,LED
from signal import pause

class ChatGPTVision:
    def connect(self):
        pass

class TrashIqupa:
    def __init__(self):
        self.var_open_close = 0

    def open_trash(self):
        self.var_open_close = 0

    def close_trash(self):
        self.var_open_close = 1

class LedsIqupa:
    def ledSetup(self):
        pass

class Iqupa(ChatGPTVision,TrashIqupa):
    def magnetic_sensor(self, pin=2): #1
        self.button = Button(pin)
        self.button.when_pressed = self.open_trash
        self.button.when_released = self.close_trash

        pause()

    def led_activation(self, pin=17):  #2
        self.led = LED(pin)

    def camera(self):    #3
        pass

    def screen(self):    #4
        pass



