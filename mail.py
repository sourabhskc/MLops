import smtplib
rcvr = "saptarsiroy12@gmail.com"
sender = "chattopadhyaysaranya@gmail.com"
msg = "Hey Developer, your model has greater than 96% accuracy and is ready to use for predictions!!" 
pswd = "***" #password for sender's mail address
server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login(sender,pswd)
print("Access Granted")
server.sendmail(sender,rcvr,msg)
print("Mail sent!!")