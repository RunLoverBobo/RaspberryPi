#!/usr/bin/python
#coding:utf-8

import socket;
import time;
import threading;
import thread
import RPi.GPIO as GPIO
import sensorData 

class Sender:   

    #初始化socket
    def __init__(self):
        HOST=''
        PORT=9999        
        ADDR=(HOST, PORT)        
        self.sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.sock.bind(ADDR)
        self.sock.listen(5)
        
        while True:
            clientSock,addr=self.sock.accept()
            t=threading.Thread(target=self.sendData,args=(clientSock,addr))
            t.start()
                
    #连接客户端，启动发送数据线程
    def sendData(self,sock,addr):        
        try:
            while True:
                print("senddata")
                time.sleep(1)                
                sock.send(sensorData.temperature+"-"
                          +sensorData.humidity+"\n")
        except:           
                sock.close()
                
        
            
