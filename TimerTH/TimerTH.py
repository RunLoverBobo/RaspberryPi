#!/usr/bin/python
#encoding:utf-8

from TM1637 import TM1637
from DhtTH import DhtTem
from time import sleep

#TM1637管脚设定
CLK = 23
DIO = 24

tm=TM1637(CLK,DIO)
A=DhtTem()

lastT=0
lastH=0

while True:
    for i in range(5):
        tm.show_clock()        

    #如本次温度数据无效，则显示上一帧数据
    curT=A.getTem('T')
    if curT=='e':
        curT=lastT
    lastT=curT
    tm.show_num(curT,'T')
    sleep(1)

    #如本次湿度数据无效，则显示上一帧数据
    curH=A.getTem('H')
    if curH=='e':
        curH=lastH
    lastH=curH
    tm.show_num(curH,'H')
    sleep(1)

