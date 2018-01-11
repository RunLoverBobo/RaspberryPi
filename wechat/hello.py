#encoding:utf-8
import itchat
from TM1637 import TM1637
from DhtTH import DhtTem

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])
    order=msg['Text']
    if order=="bobo":
        #获取数据
        file=open("/home/pi/github/RaspberryPi/TimerTH/data.txt")
        data=file.readline()
        #返回数据
        dataStr=data.split(' ')
        return "温度："+dataStr[0]+" 湿度："+dataStr[1]


#TM1637显示模块设置
CLK = 23
DIO = 24
tm=TM1637(CLK,DIO)


#微信登录
itchat.auto_login(hotReload=True)
itchat.run()



