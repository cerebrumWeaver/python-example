import time
import requests

def runningtime(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = f(*args,**kwargs)
        end_time = time.time()
        print("%s 函数执行时间：%.8f" % (f.__name__, end_time-start_time))
        return res
    return wrapper