#!/usr/bin/env python3
#-*- coding:utf-8 -*-

"""
微信接口验证模块
"""
import hashlib

def confirm(request):
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
