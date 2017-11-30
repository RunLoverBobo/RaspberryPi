#coding:utf-8

import RPi.GPIO as gpio
import time
import threading
import SensorData 

class SensorDHT:    
    def __init__(self):
        self.PORT=7
        gpio.setwarnings(False)
        gpio.setmode(gpio.BOARD)
        time.sleep(1)
        threading.Thread(target=self.getConData,args=()).start()

    def getOneData(self):
        self.PORT=7
        data=[]
        gpio.setup(self.PORT,gpio.OUT)    
        gpio.output(self.PORT,gpio.LOW)
        time.sleep(0.02)
        gpio.output(self.PORT,gpio.HIGH)

        #wait to response
        gpio.setup(self.PORT,gpio.IN)

        while gpio.input(self.PORT)==1:
            continue

        while gpio.input(self.PORT)==0:
            continue

        while gpio.input(self.PORT)==1:
            continue

        #get data
        j=0

        while j<40:
            k=0
            while gpio.input(self.PORT)==0:
                continue

            while gpio.input(self.PORT)==1:
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
            return ('%d'%temperature,'%d'%humidity)
        else:
            return ("err","err")

    def getConData(self):        
        while True:            
            SensorData.temperature,SensorData.humidity=self.getOneData()
            time.sleep(1)

      
            
            

        
        

        

        
        
        

        



    
