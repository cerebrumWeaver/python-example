import time
t1 = time.clock()
res = sum((i*i for i in range(1,100000000)))
print(res)
t2 = time.clock()
time_diff = t2 - t1
print(f"It took {time_diff} secs to execte this method")
