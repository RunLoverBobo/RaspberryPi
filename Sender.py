#!/usr/bin/python
#coding:utf-8

import socket;
import time;
import threading;
import SensorData 

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
            threading.Thread(target=self.sendData,args=(clientSock,addr)).start()
                            
    #连接客户端，启动发送数据线程,每秒发送一次数据
    def sendData(self,sock,addr):        
        try:
            while True:
                time.sleep(1)
                dataToAndroid="<time>0</time>"+\
                               "<temperature>"+SensorData.temperature+"</temperature>"+\
                               "<humidity>"+SensorData.humidity+"</humidity>"+"\n";
                sock.send(dataToAndroid)
                #sock.send(SensorData.temperature+"-"
                #          +SensorData.humidity+"\n")
                print(dataToAndroid)
        except:           
                sock.close()
                
        
            
