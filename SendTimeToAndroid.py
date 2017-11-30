#!/usr/bin/python
#coding:utf-8

import socket;
import time;
import threading;

class SendTimeThread(threading.Thread):
    def __init__(self,clientSock):
        threading.Thread.__init__(self)
        self.clientSock=clientSock

    def run(self):
        while True:
            curTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            print("现在时间："+curTime)
            self.clientSock.send(('Time from RaspberryPi:%s\n'%curTime).encode())
            time.sleep(1)
        self.clientSock.close()


#等待客户端连接
HOST=''
PORT=9999
BUFSIZ=1024
ADDR=(HOST, PORT)
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

sock.bind(ADDR)
sock.listen(5)
print('waiting for connection')

try:
    while True:
        tcpClientSock, addr=sock.accept()
        sendTimeThread=SendTimeThread(tcpClientSock)
        sendTimeThread.start()    
     
except:
    print("unable to start thread")    

sock.close()

