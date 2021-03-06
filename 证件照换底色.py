import cv2
import numpy as np
# 读取照片
img=cv2.imread(r'C:\\Users\\Administrator\\Desktop\\girl.jpg')

# 图像缩放
img = cv2.resize(img,None,fx=0.3,fy=0.3)
rows,cols,channels = img.shape
print(rows,cols,channels)

img_medianBlur=cv2.medianBlur(img,3) # 中值滤波
# cv2.namedWindow('median', cv2.WINDOW_NORMAL)  #可自动改变大小
cv2.namedWindow('median', cv2.WINDOW_AUTOSIZE)
cv2.imshow("median",img_medianBlur)


# 显示原始图像
cv2.imshow('img',img)


# 图片转换为灰度图
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# 显示灰度图像
cv2.imshow('hsv',hsv)

# 图片的二值化处理，可能会出现噪声（白点），有的图片显示的很明显，这就需要我们进行腐蚀或膨胀。
lower_blue = np.array([90,70,70])
upper_blue = np.array([110,255,255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)
# 显示二值化处理图像
cv2.imshow('mask',mask)

#腐蚀膨胀，主要用于去处噪声
erode=cv2.erode(mask,None,iterations=1) #进行腐蚀操作
#显示腐蚀后的图片
cv2.imshow('erode',erode)

dilate=cv2.dilate(mask,None,iterations=1)  #进行膨胀操作
#显示膨胀后的图片
cv2.imshow('dilate',dilate)



#遍历每个像素点，进行颜色的替换
for i in range(rows):
  for j in range(cols):
    if dilate[i,j]==255: # 像素点为255表示的是白色，我们就是要将白色处的像素点，替换为红色
      img[i,j]=(0,0,255) # 此处替换颜色，为BGR通道，不是RGB通道
img = cv2.flip(img, 1)
cv2.imshow('red',img)

# 窗口等待的命令，0表示无限等待
k = cv2.waitKey(0)
if k == ord('s'):
  font = cv2.FONT_HERSHEY_DUPLEX
  img = cv2.putText(img,"girl",(10,20),font,5.5,(0,0,0),2)
  cv2.imwrite(r'C:\\Users\\Administrator\\Desktop\\girl3.jpg',img, [int(cv2.IMWRITE_JPEG_QUALITY),100])
  cv2.destroyWindow('red')
else:
  cv2.destroyAllWindows()







# import numpy as np
# import cv2
# import matplotlib.pyplot as plot
# img = np.array([
#     [[255,0,0],[0,255,0],[0,0,255]],
#     [[255,255,0],[255,0,255],[0,255,255]],
#     [[255,255,255],[128,128,128],[0,0,0]],
# ],dtype = np.uint8)
# plot.imsave(r'C:\\Users\\Administrator\\Desktop\\plot.jpg',img)
# cv2.imwrite(r'C:\\Users\\Administrator\\Desktop\\cv2.jpg',img)

