import os
accuracy = os.system("cat /dsp/accuracy.txt")
x = 'model.add(Dense(units=64, activation=\"relu\"))'
if accuracy < 85:
    os.system("sed -i '/sigmoid/ i {}' /dsp/train.py".format(x))
else:
    print("Good going :)")
    exit()
