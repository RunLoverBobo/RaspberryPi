# -*- coding: utf-8 -*-

from django.http import HttpResponse
import sqlite3

def sendData(request):
    request.encoding='utf-8'

    dataType=request.GET['type']

    #读数据库
    conn=sqlite3.connect('/home/pi/github/RaspberryPi/Sqlite/test.db')
    c=conn.cursor()

    cursor=c.execute("SELECT TIME, T, H FROM DATA WHERE rowid=(Select max(rowid) from DATA)");

    for row in cursor:
        datatime=row[0]
        T=row[1]
        H=row[2]
    conn.close()
    
    if dataType=='one':
        message=datatime+"温度："+T+"湿度："+H

    return HttpResponse(message)
            
