#!/usr/bin/python
#encoding:utf-8

import Adafruit_DHT
from time import sleep
import math

class Dht22Data:
    sensor = Adafruit_DHT.DHT22
    pin = 4

    def getData(self,numType):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)

        humidityInt=int(humidity+0.5)
        temperatureInt=int(temperature+0.5)
        
        if numType=='T':
            return temperatureInt

        if numType=='H':
            return humidityInt


