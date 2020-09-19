import threading
from time import sleep
from showtime import runningtime
from queue import Queue

def job(li, queue2):
    sleep(1)
    queue2.put(sum(li))
@runningtime
def use_thread():
    q = Queue()
    # q.get()
    # q.put(value)
    lis = [range(5), range(2,10) ,range(1000,20000) ,range(3000,10000)]
    print(lis)
    threads = []
    for li in lis:
        t = threading.Thread(target = job, args = (li,q))
        t.start()
        threads.append(t)
    [thread.join() for thread in threads]
    results = [q.get() for li in lis]
    print(results)
    

if __name__ == "__main__":
    use_thread()