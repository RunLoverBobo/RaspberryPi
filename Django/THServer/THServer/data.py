# -*- coding: utf-8 -*-

from django.http import HttpResponse
import sqlite3
import datetime
import time
import logging

logger = logging.getLogger('django')

def sendData(request):                        
    request.encoding='utf-8'

    dataType=request.GET['type']

    #读数据库
    conn=sqlite3.connect('/home/pi/github/RaspberryPi/TimerTH/THDATA.db')
    c=conn.cursor()

    cursor=c.execute("SELECT TIME, T, H FROM TH WHERE rowid=(Select max(rowid) from TH)");

    for row in cursor:
        datatime=row[0]
        T=row[1]
        H=row[2]
    conn.close()
    
    if dataType=='one':
        curTime=time.strftime('%S')
        message=curTime+"测试时间："+datatime+" 温度："+T+" 湿度："+H
        logger.info('DataTime:'+datatime+'T:'+T+'H:'+H)
        

    return HttpResponse(message)
            
