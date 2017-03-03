#coding:utf-8
import threading
import time


class WorkThread(threading.Thread):
    def __init__(self,signal):
        threading.Thread.__init__(self)
        self.signal=signal

    def run(self):
        print("线程%s,准备进入等待状态"%self.name)
        self.signal.wait()
        print("线程%s,退出等待"%self.name)

if __name__=="__main__":
    signal = threading.Event()
    for t in range(0,6):
        thread = WorkThread(signal)
        thread.start()

    print("三秒后退出等待")
    time.sleep(3)
    signal.set()
        
