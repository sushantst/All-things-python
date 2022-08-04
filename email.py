import smtplib
smtobj=smtplib.SMTP("smtp.gmail.com", 587)
smtobj.ehlo()
smtobj.starttls()
smtobj.login("Rmessona@gmail.com","ME5048@1st")
smtobj.sendmail("Rmessona@gmail.com","sushantst15@gmail.com","Subject: SMPT check.\n just checking to see if my mail is being send via python smtp protocol ")
smtobj.quit()