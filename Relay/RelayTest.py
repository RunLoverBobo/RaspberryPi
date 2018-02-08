#!/usr/bin/env python3

from time import sleep
import RPi.GPIO as gpio


gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
controlPort=12
gpio.setup(controlPort,gpio.OUT)
while True:
    gpio.output(controlPort,gpio.HIGH)
    sleep(1)
    gpio.output(controlPort,gpio.LOW)
    sleep(1)
    
