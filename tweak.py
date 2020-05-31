import os
accuracy = os.system("cat /taskCode/accuracy.txt")
x = 'model.add(Dense(units=32, activation=\"relu\"))'
if accuracy < 80:
    os.system("sed -i '/sigmoid/ i {}' /taskCode/train.py".format(x))
else:
    print("You Achieved wnated accuracy :)")
    exit()
