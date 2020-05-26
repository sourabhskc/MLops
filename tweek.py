import os
accuracy = os.system("cat /client/accuracy.txt")
x = 'model.add(Dense(units=64, activation=\"relu\"))'
if accuracy < 85:
    os.system("sed -i '/sigmoid/ i {}' /client/client.py".format(x))
else:
    print("Good going :)")
    exit()
