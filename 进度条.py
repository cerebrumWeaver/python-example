import time
for i in range(1,101):
    print('✈'*i+f' {i}%'+'\r',end='')
    time.sleep(0.1)