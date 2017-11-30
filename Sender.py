#!/usr/bin/python
#coding:utf-8

import socket;
import time;
import threading;
import SensorData

class SendMessageThread(threading.Thread):
    def __init__(self,clientSock):
        threading.Thread.__init__(self)
        self.clientSock=clientSock

    def run(self):
        while True:
            curTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            dataToAndroid="<time>"+curTime+"</time>"+\
                         "<temperature>"+SensorData.temperature+"</temperature>"+\
                         "<humidity>"+SensorData.humidity+"</humidity>"+"\n";
            print(dataToAndroid)
            self.clientSock.send(dataToAndroid.encode())
            time.sleep(2)
        self.clientSock.close()

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

        try:
            while True:
                clientSock,addr=self.sock.accept()
                sendMsgThread=SendMessageThread(clientSock)
                sendMsgThread.start()
        except:
            print("unable to start thread")

        sock.close()
                
                
        
            
