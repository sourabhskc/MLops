#import packages
import pandas as pd
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from keras.layers import Dense
from keras.models import Sequential

#load dataset
dataset = pd.read_csv('/taskCode/Churn_Modelling.csv')

y = dataset['Exited']
X = dataset[['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
       'IsActiveMember', 'EstimatedSalary']]
geo = dataset['Geography']
geo = pd.get_dummies(geo, drop_first=True )
gender = dataset['Gender']
gender = pd.get_dummies(gender, drop_first=True )
X = pd.concat([X,gender,geo], axis=1)

#generating the training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)


#creating the CNN model
model = Sequential()
model.add(Dense(units=6, input_dim=11, activation='relu' ))
model.add(Dense(units=64, activation="relu"))
model.add(Dense(units=1,  activation='sigmoid' ))

# model summary 
model.summary()

#compile the model
model.compile(optimizer=Adam(learning_rate=0.001),loss='binary_crossentropy' , metrics=['accuracy'])

#train the model
ep=30
model.fit(X_train,y_train , epochs=ep, validation_data=(X_test, y_test) )

#get the model accuracy
accuracy = model.evaluate(X_test, y_test, verbose=0)
acc=accuracy[1]*100
print(acc)

#save the accuracy in a file 
f = open("/taskCode/accuracy.txt",'w+')
f.write(str(acc))
f.close()

#save the model for future use
model.save('/taskCode/ann.h5')





