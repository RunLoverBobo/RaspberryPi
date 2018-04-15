#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'''
数据层
'''
import sqlite3

class Data(object):
    def __init__(self):
        conn=sqlite3.connect('/home/pi/github/RaspberryPi/TimerTH/THDATA.db')
        c=conn.cursor()

        cursor=c.execute("SELECT TIME, T, H FROM TH WHERE rowid=(Select max(rowid) from TH)");

        for row in cursor:
            datatime=row[0]
            self.T=row[1]
            self.H=row[2]
        conn.close()
        
    def getT(self):
        return self.T

    def getH(self):
        return self.H
