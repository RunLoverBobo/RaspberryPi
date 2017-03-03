#!/usr/bin/python
#coding:utf-8

import DHT11
#定时获取温、湿度数据，并向客户端发送

#初始化DHT11
DHTSensor=DHT11()

while True:
    #获取温、湿度数据
    temperature,humidity=DHTSensor.getData()
    #发送数据
    
    
