#!/usr/bin/python
#encoding:utf-8

from Dht22TH import Dht22Data
import sqlite3
import datetime

DHT22=Dht22Data()

lastT=0
lastH=0

#开始时间，每分钟写一个数据
startTime=datetime.datetime.now()

while True:
    #如本次温度数据无效，则显示上一帧数据
    curT=DHT22.getData('T')
    if curT>100 or curT<0:
        curT=lastT
    lastT=curT

    #如本次湿度数据无效，则显示上一帧数据
    curH=DHT22.getData('H')
    if curH>100 or curH<0:
        curH=lastH
    lastH=curH

    print("T",curT,"H",curH)
    
    endTime=datetime.datetime.now()
    if((endTime-startTime).total_seconds()>=10):
        #写数据库
        conn=sqlite3.connect('/home/pi/github/RaspberryPi/TimerTH/THDATA.db')
        c=conn.cursor()
        curTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c.execute("INSERT INTO TH (TIME,T,H) VALUES ('"+curTime+"', '"+str(curT)+"', '"+str(curH)+"')")
        conn.commit()
        conn.close()

        startTime=endTime
