#!/usr/bin/python
#encoding:utf-8

#增加搜索路径
import sys
sys.path.append("/home/pi/github/RaspberryPi/Django/WeChat/WeChat")

from TM1637 import TM1637
from time import sleep
from roomData import Data
import sqlite3
import datetime

#TM1637管脚设定
CLK = 23
DIO = 24

tm=TM1637(CLK,DIO)

while True:    
    for i in range(5):
        tm.show_clock()        

    #读取并显示温度数据
    T=Data().getT()
    tm.show_num(T,'T')
    sleep(1)

    #读取并显示湿度数据
    H=Data().getH()
    tm.show_num(H,'H')
    sleep(1)

