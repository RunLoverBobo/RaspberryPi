#!/usr/bin/python
#encoding:utf-8

from TM1637 import TM1637
from DhtTH import DhtTem
from time import sleep
import sqlite3
import datetime

#TM1637管脚设定
CLK = 23
DIO = 24

tm=TM1637(CLK,DIO)
A=DhtTem()

lastT=0
lastH=0

#文件设置
startTime=datetime.datetime.now()

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

    endTime=datetime.datetime.now()
    if((endTime-startTime).total_seconds()>=60):
        #写数据库
        conn=sqlite3.connect('/home/pi/github/RaspberryPi/TimerTH/THDATA.db')
        c=conn.cursor()
        curTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(curTime)
        c.execute("INSERT INTO TH (TIME,T,H) VALUES ('"+curTime+"', '"+str(curT)+"', '"+str(curH)+"')")
        conn.commit()
        conn.close()

        startTime=endTime
