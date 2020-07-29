from concurrent.futures import ThreadPoolExecutor

def job(num):
    print('这是一个%s任务' %(num))
    return '执行结果：%s' %(num)

if __name__=='__main__':
    pool = ThreadPoolExecutor(max_workers = 5)
    futures = []
    for i in range(10):
        f1 = pool.submit(job, i)
        futures.append(f1)
print(futures[0].done(),'------------')
print(futures[0].result())