from threading import Semaphore, Thread
import time

sem = Semaphore()
exit_flag = False


def fun1():
    global exit_flag
    while not exit_flag:
        sem.acquire()
        print(1)
        sem.release()
        time.sleep(0.25)


def fun2():
    global exit_flag
    while not exit_flag:
        sem.acquire()
        print(2)
        sem.release()
        time.sleep(0.25)


t1 = Thread(target=fun1)
t2 = Thread(target=fun2)

try:
    t1.start()
    t2.start()
    t1.join()
    t2.join()
except KeyboardInterrupt:
    print('\nReceived keyboard interrupt, quitting threads.')
    exit_flag = True
    t1.join()
    t2.join()
    exit(1)
