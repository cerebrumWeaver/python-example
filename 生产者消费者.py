def creat_data():
    with open('C:\\Users\\Administrator\\Desktop\\ip.txt', 'w') as f:
        for i in range(20):
            f.write('172.25.254.%s\n' %(i+1))
        print("测试数据创建完成！")

import time
import threading
from queue import Queue
from urllib.request import urlopen

class Producer(threading.Thread):
    def __init__(self, queue):
        super(Producer,self).__init__()
        self.q = queue

    def run(self):
        # ports = [80, 443, 7001, 7002, 8000, 8080, 9000, 9001]

        ports = [80]
        with open('C:\\Users\\Administrator\\Desktop\\ip.txt') as f:
            for line in f:
                ip = line.strip()
                for port in ports:
                    url = 'http://%s:%s' %(ip,port)
                    time.sleep(0.1)
                    self.q.put(url)
                    print("生产者产生url: %s" %(url))

class Consumer(threading.Thread):
    def __init__(self,queue):
        super(Consumer,self).__init__()
        self.q = queue

    def run(self):
        url = self.q.get()
        try:
            urlObj = urlopen(url)
        except Exception as e:
            print("%s不可访问" %(url))
        else:
            pageContentSize = len(urlObj.read().decode('utf-8'))
            print("%s可以访问，页面大小为%s" %(url,pageContentSize))

def main():
    q = Queue()
    p = Producer(q)
    p.start()

    for i in range(18):
        c= Consumer(q)
        c.start()

if __name__ == '__main__':
    # creat_data()
    main()