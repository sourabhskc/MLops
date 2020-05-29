import os
accuracy = os.system("cat /taskCode/accuracy.txt")
x = 'model.add(Dense(units=64, activation=\"relu\"))'
if accuracy < 85:
    os.system("sed -i '/sigmoid/ i {}' /taskCode/train.py".format(x))
else:
    print("Good going :)")
    exit()
