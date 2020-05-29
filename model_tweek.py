import os
accuracy = os.system("cat /taskCode/model_accuracy.txt")
x = 'model.add(Dense(units=32, activation=\"relu\"))'
if accuracy < 98:
    os.system("sed -i '/softmax/ i {}' /taskCode/model_code.py".format(x))
else:
    print("Good going :)")
    exit()
