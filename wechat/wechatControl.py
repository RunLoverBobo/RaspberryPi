#encoding:utf-8
import itchat


@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    
    order=msg['Text']
    print(order)
    if order=="bobo":
        #获取数据
        file=open("/home/pi/github/RaspberryPi/TimerTH/data.txt")
        data=file.readline()
        file.close()
        #返回数据
        dataStr=data.split(' ')
        return "温度："+dataStr[0]+" 湿度："+dataStr[1]


#微信登录
itchat.auto_login(hotReload=True)

itchat.run()



