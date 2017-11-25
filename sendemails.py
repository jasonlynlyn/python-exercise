import smtplib
print "Sending emails via python"
m=raw_input("Please enter your emaili address: ")
n=raw_input("Please enter your email password: ")
r=raw_input("please enter the receiver's email address: ")
smtpobj=smtplib.SMTP("smtp.gmail.com", 587)
smtpobj.ehlo()
smtpobj.starttls()
smtpobj.login(m, n)
smtpobj.sendmail(n, r,"subject: I know what you did last summer")
smtpobj.quit()