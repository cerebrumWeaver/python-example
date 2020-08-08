from keras.datasets import imdb
# from tensorflow.keras.layers.experimental.preprocessing import RandomRotation
(train_data,train_labels), (test_data,test_labels) = imdb.load_data(num_words = 10000)
print(train_data[0])
# print(type(RandomRotation))