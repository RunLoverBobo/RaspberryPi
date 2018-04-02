#!/usr/bin/env python3
#-*- coding:utf-8 -*-

"""
处理用户指令模块
"""
from msg import Msg
from lxml import etree
import time
import Humidifier
from roomData import Data

import logging

logger = logging.getLogger('django')


class OrderProcesser(object):    
    '''
    指令处理模块
    '''
    def processOrder(self,msg):
        '''
        处理指令
        '''
        replyMsg=Msg()
        
        humidifier=Humidifier.Humidifier()
        content=msg.content
        replyMsg.content=content

        if('温度' in content):
            replyMsg.content=Data().getT()

        if('湿度' in content):
            replyMsg.content=Data().getH()

        if('开' in content):
            humidifier.open()
            replyMsg.content='加湿器已打开'

        if('关' in content):
            humidifier.close()
            replyMsg.content='加湿器已关闭'
        
        replyMsg.fromUserName=msg.toUserName
        replyMsg.toUserName=msg.fromUserName
 
        return replyMsg
        
    
    
