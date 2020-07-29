import threading
from showtime import timeit

@timeit
def add(lock):
    global money
    for i in range(1000000):
        lock.acquire()
        money += 1
        lock.release()
@timeit
def reduce(lock):
    global money
    for i in range(1000000):
        lock.acquire()
        money -= 1
        lock.release()

if __name__ == '__main__':
    money = 23
    lock = threading.Lock()
    t1 = threading.Thread(target = add, args = (lock,))
    t2 = threading.Thread(target = reduce, args = (lock,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("当前金额：%d " %(money))