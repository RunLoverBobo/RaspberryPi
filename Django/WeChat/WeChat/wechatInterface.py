#!/usr/bin/env python3
#-*- coding:utf-8 -*-

"""
RaspberryPi与微信的接口程序
"""
#路径设置
import sys
sys.path.append("/home/pi/github/RaspberryPi/Django/WeChat/WeChat")
from django.views.decorators.csrf import csrf_exempt
#微信验证模块

import wechatConfirm
from msg import Msg
from msgProcesser import MsgProcesser
from orderProcesser import OrderProcesser

from django.http import HttpResponse

import logging
from lxml import etree
from msg import Msg

import Humidifier 


logger = logging.getLogger('django')

import hashlib

@csrf_exempt
def wechat_main(request):
    #与微信服务器验证
    if request.method == "GET":        
        confirmResult=confirmWechat(request)        
        return HttpResponse(confirmResult)
     
    #响应用户消息
    else:        
        xmlStr=request.body

        #解析用户指令（表现层）
        msgProcesser=MsgProcesser()
        msg=msgProcesser.parseUserOrder(xmlStr)

        #响应用户指令（业务层）
        orderProcesser=OrderProcesser()
        replyMsg=orderProcesser.processOrder(msg)

        #返回指令执行结果（表现层）
        replyResult=msgProcesser.genMsg(replyMsg)        
        return HttpResponse(replyResult)



        

