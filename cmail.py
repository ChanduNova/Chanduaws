import smtplib
from email.message import EmailMessage
def send_mail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('battulachandu890@gmail.com','rkfb avru kgcz lbhy')
    msg=EmailMessage()
    msg['FROM']='battulachandu890@gmail.com'
    msg['TO']=to
    msg['SUBJECT']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.close()