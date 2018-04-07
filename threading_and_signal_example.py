import signal
import threading
import time
import sys


_stopper=False

def go():
    while True and not(_stopper):
        print("%s:%s: %s"%(time.time(), threading.current_thread().name, threading.active_count()))
        time.sleep(1)


def stopper(sn, fr):
    print("It's time to stop ...")
    for i in range(5, -1, -1):
        print("Stop in %s seconds (%s, %s)..."%(i, sn, fr))
        time.sleep(1)
    global _stopper
    _stopper=True
    time.sleep(1)
    sys.exit(0)



if __name__ == '__main__':

    signal.signal(signal.SIGINT, stopper)
    signal.signal(signal.SIGTERM, stopper) 

    for i in range(5):
        threading.Thread(target=go, args=()).start()

    while True:
        print("Running ...")
        time.sleep(1)

