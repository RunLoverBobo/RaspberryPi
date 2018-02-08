#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from django.views.decorators.csrf import csrf_exempt
import hashlib
from django.http import HttpResponse
import logging
from lxml import etree
from django.utils.encoding import smart_str
import sqlite3
import RPi.GPIO as gpio

#from wiringpi import wiringPiSetupGpio, pinMode, digitalWrite, GPIO

logger = logging.getLogger('django')


@csrf_exempt
def wechat_main(request):

    if request.method == "GET":
        #接收微信服务器get请求发过来的参数
        signature = request.GET.get('signature',None)
        timestamp = request.GET.get('timestamp',None)
        nonce = request.GET.get('nonce',None)
        echostr = request.GET.get('echostr',None)
        #服务器配置中的token
        token='BoboRaspberryPi'
        #把参数放到list中排序后合成一个字符串，再用sha1加密得到新的字符串与微信发来的
        #signature对比，如果相同就返回echostr给服务器，校验通过
        hashlist=[token,timestamp,nonce]
        hashlist.sort()
        hashstr=''.join([s for s in hashlist])
        hashstr=hashlib.sha1(hashstr.encode(encoding='utf-8')).hexdigest()
        
        if hashstr==signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse('failed')       

    else:
        str_xml=request.body
        logger.info(str_xml)
        xml=etree.fromstring(str_xml)
        content=xml.find("Content").text
        msgType=xml.find("MsgType").text
        fromUser=xml.find("FromUserName").text
        toUser=xml.find("ToUserName").text
        createTime=xml.find("CreateTime").text

        if(content=='温度'):
           content=Data().getT()

        if(content=='湿度'):
            content=Data().getH()

        if(content=='开加湿'):
            Humidifier().open()
            content='加湿器已打开'

        if(content=='关加湿'):
            Humidifier().close()
            content='加湿器已关闭'
          
        
        replyMsg=TextMsg(toUser,fromUser,content,createTime)
        return HttpResponse(replyMsg.send())
    
import RPi.GPIO as GPIO

class Humidifier(object):
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(12,GPIO.OUT)

        logger.info('Humidifier_init')
        
    def open(self):
        #digitalWrite(self.controlPort,GPIO.LOW)
        GPIO.output(12,GPIO.LOW)

    def close(self):
        #digitalWrite(self.controlPort,GPIO.HIGH)
        GPIO.output(12,GPIO.HIGH)
  

import time
class TextMsg(object):
    def __init__(self,toUserName,fromUserName,content,createTime):
        self.__dict=dict()
        self.__dict['ToUserName']=fromUserName
        self.__dict['FromUserName']=toUserName
        self.__dict['CreateTime']=int(time.time())
        self.__dict['Content']=content

    def send(self):
        XmlForm="""
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        """
        logger.info(XmlForm.format(**self.__dict))
        return XmlForm.format(**self.__dict)

class Data(object):
    def __init__(self):
        conn=sqlite3.connect('/home/pi/github/RaspberryPi/TimerTH/THDATA.db')
        c=conn.cursor()

        cursor=c.execute("SELECT TIME, T, H FROM TH WHERE rowid=(Select max(rowid) from TH)");

        for row in cursor:
            datatime=row[0]
            self.T=row[1]
            self.H=row[2]
        logger.info([self.T,self.H])
        conn.close()
        
    def getT(self):
        logger.info(self.T)
        return self.T

    def getH(self):
        return self.H

