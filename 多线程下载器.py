import threading
from urllib.request import urlopen

DOWNLOAD_DIR = 'C:/Users/Administrator/Desktop/'
class DownloadThread(threading.Thread):
    def __init__(self, url, i):
        super(DownloadThread, self).__init__()
        self.url = url
        self.i = i
    def run(self):
        try:
            urlObj = urlopen(self.url, timeout = 3)
        except Exception as e:
            print('download %s error\n' %(self.url), e)
            imgContent = None
        else:
            # filename = self.url.split('/')[-1]
            filename = str(self.i)+'img.jpg'

            with open('%s/%s' %(DOWNLOAD_DIR, filename), 'wb') as f:
                while True:
                    imgContentChunk = urlObj.read(1024*3)
                    if not imgContentChunk:
                        break
                    f.write(imgContentChunk)
                print("%s下载成功" %(filename))

url1 = 'http://nbimg.jgyljt.com/newImgs/img/157267440683ab7.jpg?t=1595501364000'
url2 = 'http://nbimg.jgyljt.com/newImgs/img/157267440407d35.jpg?t=1595501364000'
url3 = 'http://nbimg.jgyljt.com/newImgs/img/157267440587b52.jpg?t=1595501364000'
urls = [url1, url2, url3]
i = 0
for url in urls:
    i+=1
    print("i=%d" %(i))
    thread = DownloadThread(url, i)
    thread.start()