import RPi.GPIO as gpio
import time

class Led:
    def __init__(self):
        self.VccUp=18
        self.VccDown=33
        self.ledA=11
        self.ledB=7
        self.ledC=31
        self.ledD=35
        self.ledE=37
        self.ledF=13
        self.ledG=15
        self.ledH=29
                
        gpio.setwarnings(False)
        gpio.setmode(gpio.BOARD)
        time.sleep(1)

        gpio.setup(self.VccUp,gpio.OUT)
        gpio.setup(self.VccDown,gpio.OUT)
        gpio.setup(self.ledA,gpio.OUT)
        gpio.setup(self.ledB,gpio.OUT)
        gpio.setup(self.ledC,gpio.OUT)
        gpio.setup(self.ledD,gpio.OUT)
        gpio.setup(self.ledE,gpio.OUT)
        gpio.setup(self.ledF,gpio.OUT)
        gpio.setup(self.ledG,gpio.OUT)
        gpio.setup(self.ledH,gpio.OUT)

    def vccLow(self):
        gpio.output(self.VccUp,gpio.LOW)
        gpio.output(self.VccDown,gpio.LOW)

    def vccHigh(self):
        gpio.output(self.VccUp,gpio.HIGH)
        gpio.output(self.VccDown,gpio.HIGH)

    def on(self):
        self.vccLow()
        gpio.output(self.ledA,gpio.LOW)
        gpio.output(self.ledB,gpio.LOW)
        gpio.output(self.ledC,gpio.LOW)
        gpio.output(self.ledD,gpio.LOW)
        gpio.output(self.ledE,gpio.LOW)
        gpio.output(self.ledF,gpio.LOW)
        gpio.output(self.ledG,gpio.LOW)
        gpio.output(self.ledH,gpio.LOW)
        self.vccHigh()


    def show1(self):
        self.vccLow()
        gpio.output(self.ledA,gpio.HIGH)
        gpio.output(self.ledB,gpio.LOW)
        gpio.output(self.ledC,gpio.LOW)
        gpio.output(self.ledD,gpio.HIGH)
        gpio.output(self.ledE,gpio.HIGH)
        gpio.output(self.ledF,gpio.HIGH)
        gpio.output(self.ledG,gpio.HIGH)
        gpio.output(self.ledH,gpio.HIGH)
        self.vccHigh()

    def show2(self):
        self.vccLow()
        gpio.output(self.ledA,gpio.LOW)
        gpio.output(self.ledB,gpio.LOW)
        gpio.output(self.ledC,gpio.HIGH)
        gpio.output(self.ledD,gpio.LOW)
        gpio.output(self.ledE,gpio.LOW)
        gpio.output(self.ledF,gpio.HIGH)
        gpio.output(self.ledG,gpio.LOW)
        gpio.output(self.ledH,gpio.HIGH)
        self.vccHigh()

    def show3(self):
        self.vccLow()
        gpio.output(self.ledA,gpio.LOW)
        gpio.output(self.ledB,gpio.LOW)
        gpio.output(self.ledC,gpio.LOW)
        gpio.output(self.ledD,gpio.LOW)
        gpio.output(self.ledE,gpio.HIGH)
        gpio.output(self.ledF,gpio.HIGH)
        gpio.output(self.ledG,gpio.LOW)
        gpio.output(self.ledH,gpio.HIGH)
        self.vccHigh()

    def show4(self):
        self.vccLow()
        gpio.output(self.ledA,gpio.HIGH)
        gpio.output(self.ledB,gpio.LOW)
        gpio.output(self.ledC,gpio.LOW)
        gpio.output(self.ledD,gpio.HIGH)
        gpio.output(self.ledE,gpio.HIGH)
        gpio.output(self.ledF,gpio.LOW)
        gpio.output(self.ledG,gpio.LOW)
        gpio.output(self.ledH,gpio.HIGH)
        self.vccHigh()

    def show5(self):
        self.vccLow()
        gpio.output(self.ledA,gpio.LOW)
        gpio.output(self.ledB,gpio.HIGH)
        gpio.output(self.ledC,gpio.LOW)
        gpio.output(self.ledD,gpio.LOW)
        gpio.output(self.ledE,gpio.HIGH)
        gpio.output(self.ledF,gpio.LOW)
        gpio.output(self.ledG,gpio.LOW)
        gpio.output(self.ledH,gpio.HIGH)
        self.vccHigh()

    def show6(self):
        self.vccLow()
        gpio.output(self.ledA,gpio.LOW)
        gpio.output(self.ledB,gpio.HIGH)
        gpio.output(self.ledC,gpio.LOW)
        gpio.output(self.ledD,gpio.LOW)
        gpio.output(self.ledE,gpio.LOW)
        gpio.output(self.ledF,gpio.LOW)
        gpio.output(self.ledG,gpio.LOW)
        gpio.output(self.ledH,gpio.HIGH)
        self.vccHigh()

    def show7(self):
        self.vccLow()
        gpio.output(self.ledA,gpio.LOW)
        gpio.output(self.ledB,gpio.LOW)
        gpio.output(self.ledC,gpio.LOW)
        gpio.output(self.ledD,gpio.HIGH)
        gpio.output(self.ledE,gpio.HIGH)
        gpio.output(self.ledF,gpio.HIGH)
        gpio.output(self.ledG,gpio.HIGH)
        gpio.output(self.ledH,gpio.HIGH)
        self.vccHigh()

    def show8(self):
        self.vccLow()
        gpio.output(self.ledA,gpio.LOW)
        gpio.output(self.ledB,gpio.LOW)
        gpio.output(self.ledC,gpio.LOW)
        gpio.output(self.ledD,gpio.LOW)
        gpio.output(self.ledE,gpio.LOW)
        gpio.output(self.ledF,gpio.LOW)
        gpio.output(self.ledG,gpio.LOW)
        gpio.output(self.ledH,gpio.HIGH)
        self.vccHigh()

    def show9(self):
        self.vccLow()
        gpio.output(self.ledA,gpio.LOW)
        gpio.output(self.ledB,gpio.LOW)
        gpio.output(self.ledC,gpio.LOW)
        gpio.output(self.ledD,gpio.LOW)
        gpio.output(self.ledE,gpio.HIGH)
        gpio.output(self.ledF,gpio.LOW)
        gpio.output(self.ledG,gpio.LOW)
        gpio.output(self.ledH,gpio.HIGH)
        self.vccHigh()

    def show1To9(self,intTime):
        self.show1()
        time.sleep(intTime)
        self.show2()
        time.sleep(intTime)
        self.show3()
        time.sleep(intTime)
        self.show4()
        time.sleep(intTime)
        self.show5()
        time.sleep(intTime)
        self.show6()
        time.sleep(intTime)
        self.show7()
        time.sleep(intTime)
        self.show8()
        time.sleep(intTime)
        self.show9()
        time.sleep(intTime)

    def conShow(self):
        while(1):
            self.show1To9(1)

    def off(self):
        self.vccLow()

        
        
        

  
