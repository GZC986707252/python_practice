import threading
import time

'''
def fun(x , y , thr=None):
    if thr:
        print(time.ctime())
        thr.join()
    else:
        pass
    for i in range(x,y):
        print (str(i * i)+"--"+time.ctime()+";")
ta = threading.Thread(target=fun ,args=(1,6))
tb = threading.Thread(target=fun , args=(16,21,ta))
ta.start()
tb.start()
'''

'''
class MyThread(threading.Thread):
    def run(self):
        global x
        lock.acquire()
        for i in range(5):
            x += 10
        print(x)
        lock.release()

x = 0
lock=threading.RLock()

ma = MyThread()
mb = MyThread()
ma.start()
mb.start()
'''

'''
class myThread(threading.Thread):
    def __init__(self,mynum):
        super().__init__()
        self.mynum = mynum

    def run(self):
        time.sleep(1)
        for i in range(self.mynum,self.mynum+5):
            print(str(i*i)+';')

def main():
    print('start...')
    ma = myThread(1)
    mb = myThread(16)
    ma.daemon = True
    mb.daemon = True
    ma.start()
    mb.start()
    #ma.join()
    #mb.join()
    print('end...')
if __name__ == "__main__":
    main()
'''


class myThreada(threading.Thread):
    def run(self):
        evt.wait()
        print(self.name,':Good morning!')
        evt.clear()
        time.sleep(1)
        evt.set()
        time.sleep(1)
        evt.wait()
        print(self.name,":I'm fine,thank you.")
        
class myThreadb(threading.Thread):
    def run(self):
        print(self.name,':Good morning!')
        evt.set()
        time.sleep(1)
        evt.wait()
        print(self.name,':How are you?')
        evt.clear()
        time.sleep(1)
        evt.set()

evt = threading.Event()
def main():
    John = myThreada()
    John.name = "John"
    Smith = myThreadb()
    Smith.name = 'Smith'
    John.start()
    Smith.start()
if __name__ == "__main__":
    main()


