#Threading

import threading
from threading import *
from time import sleep

class ThrOne(Thread) :
    def run(self): #run itself
        for i in range(10):
            print( "Threadl " , i, threading. current_thread() . name)
            sleep(2)
class Thrtwo(Thread) :
    def run(self):
        for i in range(10):
            print( "Thread2 " , i, threading. current_thread() . name)
            sleep(2)
a = ThrOne()
b = Thrtwo()
a.start()
sleep(1)
b.start()
print(a.is_a1ive())#Checks its running or not
a.join()#terminate the thread
print (a.is_alive())
print(threading.current_thread.name) #get name of threade