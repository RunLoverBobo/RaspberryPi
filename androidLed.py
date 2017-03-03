#!/usr/bin/python
#coding:utf-8

import socket;
import time;
import threading;
import thread
import RPi.GPIO as GPIO

PIN_NO=12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_NO,GPIO.OUT)

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

def send_time(clientSock,threadName):
    curTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print(threadName+" "+curTime)
    
    data=clientSock.recv(1024).replace('\n','');
    print(data)
    if data=="On":
        print("Led On")
        GPIO.output(PIN_NO,GPIO.HIGH)
    if data=="Off":
        print("Led Off")
        GPIO.output(PIN_NO,GPIO.LOW)

    clientSock.close()

try:
    threadNum=1
    while True:
        tcpClientSock, addr=sock.accept()        
        numStr='%d'%threadNum
        thread.start_new_thread(send_time,(tcpClientSock,"thread"+numStr,))
        threadNum=threadNum+1
        
except:
    print("unable to start thread")
    

sock.close()
