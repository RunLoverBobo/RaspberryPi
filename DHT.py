#!/usr/bin/python
#encoding:utf-8

import RPi.GPIO as gpio
import time

PORT=7
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
time.sleep(1)


#start work
while True:
    data=[]
    gpio.setup(PORT,gpio.OUT)    
    gpio.output(PORT,gpio.LOW)
    time.sleep(0.02)
    gpio.output(PORT,gpio.HIGH)

    #wait to response
    gpio.setup(PORT,gpio.IN)

    while gpio.input(PORT)==1:
        continue

    while gpio.input(PORT)==0:
        continue

    while gpio.input(PORT)==1:
        continue

    #get data
    j=0

    while j<40:
        k=0
        while gpio.input(PORT)==0:
            continue

        while gpio.input(PORT)==1:
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
        curTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        print curTime,"wendu",temperature,"shidu",humidity

    time.sleep(1)
