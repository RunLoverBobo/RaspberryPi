#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'''
加湿器类
'''

import RPi.GPIO as GPIO

class Humidifier(object):
    
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(12,GPIO.OUT)
        
    def open(self):
        GPIO.output(12,GPIO.LOW)

    def close(self):
        GPIO.output(12,GPIO.HIGH)
