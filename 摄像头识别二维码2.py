import cv2
import pyzbar.pyzbar as pyzbar
import time
cap = cv2.VideoCapture(0)
fob = open('atendence.txt','w+')
names = []
def enterDate(z):
    if z in names:
        pass
    else:
        names.append(z)
        z = ''.join(str(z))
        fob.write(z+'\n')
    return names
print('二维码读取中...')

def checkData(data):
    data = str(data)
    if data in names:
        print('已签到')
    else:
        print('\n'+str(len(names)+1)+'\n'+data)
        enterData(data)