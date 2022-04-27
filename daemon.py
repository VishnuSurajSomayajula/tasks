from threading import *
import time


def job():
    for i in range(12):
        print("Lazzzie Thread..!")
        time.sleep(3)
t = Thread(target=job)
t.setDaemon(True)
t.start()
time.sleep(10)
print("end of the thread")