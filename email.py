import smtplib

smtObj =smtplib.SMTP('smtp.gmail.com', 587)
smtObj.ehlo()  #connects the serves snder and recicer
smtObj.starttls()
smtObj.login() #username and login
smtObj.sendmail()
#email sent too, Email sent from, Subject: items. \n the body


smtObj.quit() #end the connection