#import packages
from keras.datasets import mnist
from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D,MaxPooling2D,Flatten,Dense
from keras.optimizers import Adam


#load dataset
dataset = mnist.load_data('projDataset.db')

#generating the training and testing sets
(X_train , y_train), (X_test , y_test) = dataset

#converting the by-default 28*28 input images into 1D 784 pixel images
reX_train = X_train.reshape(-1 , 28*28)
reX_test = X_test.reshape(-1 , 28*28)

#Force pixel precision to keras by-default 32bit
X_train = reX_train.astype('float32')
X_test = reX_test.astype('float32')

#one hot encoding the outputs
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

#create the CNN model
model = Sequential()
model.add(Dense(units=256, input_dim=28*28, activation='relu'))
model.add(Dense(units=128, activation='relu'))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=32, activation='relu'))
model.add(Dense(units=10, activation='softmax'))

#get the parameters for the model
model.summary()

#compile the model
model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

#train the model
model.fit(X_train,y_train,epochs=10,verbose=0,validation_data=(X_test,y_test))

#get the model accuracy
scores = model.evaluate(X_test,y_test,verbose=0)
acc = scores[1]*100
acc = int(acc)

#store the accuracy in a file
f = open("Accuracy.txt",'w+')
f.write(str(acc))
f.close()