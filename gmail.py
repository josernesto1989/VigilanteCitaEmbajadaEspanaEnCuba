import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class MailTo:
    def __init__(self):
        self.mail_content= '''Hello,
        This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
        Thank You
        '''
        #The mail addresses and password
        self.sender_address = 'jedevelop3@gmail.com'
        self.sender_pass = 'xxxxx'

        self.receiver_address = 'josernesto1989@gmail.com'
        #Setup the MIME
        

    def sendMail(self):
        message = MIMEMultipart()
        message['From'] = self.sender_address
        message['To'] = self.receiver_address
        message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line
        #The body and the attachments for the mail
        message.attach(MIMEText(self.mail_content, 'plain'))
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent')
