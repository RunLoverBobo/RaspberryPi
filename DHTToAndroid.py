#!/usr/bin/python
#coding:utf-8

from SensorDHT import *
from Sender import *
import threading
import Queue

#定时获取温、湿度数据，并向客户端发送
global temp
#初始化DHT11
sensor=SensorDHT()

#初始化Android信息服务
sender=Sender()



    

