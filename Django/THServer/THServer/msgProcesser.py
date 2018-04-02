#!/usr/bin/env python3
#-*- coding:utf-8 -*-


from lxml import etree
import time
from msg import Msg
import chardet
from django.core.files.base import ContentFile
from django.core.files.storage import get_storage_class
import logging

logger = logging.getLogger('django')

class MsgProcesser(object):
    '''
    消息处理模块
    '''
   
    def parseUserOrder(self,xmlStr):
        '''
        解析用户消息
        '''
        xml=etree.fromstring(xmlStr)

        msg=Msg()
        
        msg.msgType=xml.find("MsgType").text
        msg.fromUserName=xml.find("FromUserName").text
        msg.toUserName=xml.find("ToUserName").text
        msg.createTime=xml.find("CreateTime").text

        if(msg.msgType=='text'):
            msg.content=xml.find("Content").text

        if(msg.msgType=='voice'):
            msg.content=xml.find("Recognition").text

        logger.info(msg.content)
       

        return msg

    def genMsg(self,msg):
        '''
        生成用户消息
        '''
        self.__dict=dict()
        self.__dict['ToUserName']=msg.toUserName
        self.__dict['FromUserName']=msg.fromUserName
        self.__dict['CreateTime']=int(time.time())
        self.__dict['Content']=msg.content
        
        XmlForm="""
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        """

        return XmlForm.format(**self.__dict)

    
        

