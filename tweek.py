import os
accuracy = os.system("cat /env_code/accuracy.txt")
x = 'model.add(Dense(units=64, activation=\"relu\"))'
if accuracy < 85:
    os.system("sed -i '/sigmoid/ i {}' /env_code/train.py".format(x))
else:
    print("Good going :)")
    exit()
