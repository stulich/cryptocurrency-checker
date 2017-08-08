import smtplib

#username and password for gmail account
username='enter email here'
password='enter password here'

def sendReport(destination, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(username, password)
    server.sendmail(username, destination, message)
    server.quit()