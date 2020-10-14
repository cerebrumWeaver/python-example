import numpy as np
import numpy
from numpy.core.defchararray import decode
import tensorflow as tf
import os
from tensorflow.python.ops.image_ops_impl import ResizeMethod
import tensorflow as tf
import matplotlib.pylab as plt


path = 'C:\\Users\\Administrator\\Desktop\\girl.jpg'
target='C:\\Users\\Administrator\\Desktop\\girl.txt'

# 读取数据文件
image = tf.compat.v1.read_file(path, 'r')

# 将图像文件解码为Tensor
image_tensor = tf.image.decode_jpeg(image)
image_tensor_numpy = image_tensor.numpy()
# print(type(image_tensor[0][1][1]))
print('#######################################################################')
# image_resize = tf.image.resize(image_tensor, [400, 300], method='nearest')
# image_resize = tf.image.resize_with_pad(image_tensor,600,375,method=ResizeMethod.NEAREST_NEIGHBOR)
# print(image_resize)


# 图像各 像素点 数值对 写入文件
# try:
#     # coding=UTF-8,写入多行取消注释即可
#     with open(target, 'w',encoding="UTF-8") as file_object:
#         for h in range(image_tensor.shape[0]):
#             for w in range(image_tensor.shape[1]):
#                 for i in range(image_tensor.shape[2]):
#                     file_object.write(image_tensor_numpy[h][w][i].astype(np.str)+'\t')
#                 file_object.write('\r\n')   # 每输入一个像素点数值对(3个一对)后换一行
# finally:
#     file_object.close()


# 读取文件 像素点 数值对
file = open('C:\\Users\\Administrator\\Desktop\\girl.txt', 'r',encoding="utf-8")
image_tensor_init = tf.zeros(shape=(image_tensor.shape[0],image_tensor.shape[1],image_tensor.shape[2]))
tensor_string = None
tensor_int_list = []
try:
    tensor_string=file.read()                       
finally:
    file.close()
tensor_string_str=tensor_string.replace('\n','')
tensor_string_list = tensor_string_str.split('\t')
array_numpy = np.array(tensor_string_list[:-1])
array_numpy = array_numpy.astype(np.int)
numpy_to_tensor = tf.convert_to_tensor(array_numpy)
# image_numpy_to_tensor = tf.reshape(numpy_to_tensor,(image_tensor.shape[0], image_tensor.shape[1], image_tensor.shape[2]))
image_numpy_to_tensor = tf.reshape(numpy_to_tensor,(1000, 460, 3))

print(image_numpy_to_tensor)
print(type(image_numpy_to_tensor))



# 图像张量的形状
# shape = tf.shape(image_tensor)
# print(shape)

# # 显示图片
plt.imshow(image_numpy_to_tensor)
plt.show()


