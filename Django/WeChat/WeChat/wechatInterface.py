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
import hashlib

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

def confirmWechat(request):
    """
    接收微信服务器get请求发过来的参数
    处理后返回验证字符串
    """
        
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
        return echostr
    else:
        return 'failed'   




        

