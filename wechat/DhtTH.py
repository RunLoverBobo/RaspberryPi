#!/usr/bin/python
#encoding:utf-8

#import RPi.GPIO as gpio
from wiringpi import wiringPiSetupGpio, pinMode, digitalRead, digitalWrite, GPIO

from time import time,sleep


class DhtTem:
    PORT=4
    wiringPiSetupGpio()

    def getData(self,numType):
        data=[]
        pinMode(self.PORT,GPIO.OUTPUT)
        digitalWrite(self.PORT,GPIO.LOW)
        sleep(0.02)
        digitalWrite(self.PORT,GPIO.HIGH)

        #wait to response
        pinMode(self.PORT,GPIO.INPUT)

        while digitalRead(self.PORT)==GPIO.HIGH:
            continue

        while digitalRead(self.PORT)==GPIO.LOW:
            continue

        while digitalRead(self.PORT)==GPIO.HIGH:
            continue

        #get data
        j=0

        while j<40:
            k=0
            while digitalRead(self.PORT)==GPIO.LOW:
                continue

            while digitalRead(self.PORT)==GPIO.HIGH:
                k+=1
                if k>100:
                    break
            
            if k<8:
                data.append(0)
            else:
                data.append(1)
            j+=1

        #get temperature
        humidity_bit=data[0:8]
        humidity_point_bit=data[8:16]
        temperature_bit=data[16:24]
        temperature_point_bit=data[24:32]
        check_bit=data[32:40]

        humidity=0
        humidity_point=0
        temperature=0
        temperature_point=0
        check=0

        for i in range(8):
            humidity+=humidity_bit[i]*2**(7-i)
            humidity_point+=humidity_point_bit[i]*2**(7-i)
            temperature+=temperature_bit[i]*2**(7-i)
            temperature_point+=temperature_point_bit[i]*2**(7-i)
            check+=check_bit[i]*2**(7-i)

        tmp=humidity+humidity_point+temperature+temperature_point

        
        if check==tmp:
            if numType=='T':
                return temperature
            else:
                return humidity
        else:
            return 'e'
        

        




