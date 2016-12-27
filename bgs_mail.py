# -*- coding: utf8 -*-
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import email as em

'''
for this project I'm gonna use SMTP(Simple Mail Transfer Protocol) protocol written on RFC 821 doc => RFC 5321

_Using port : 587
_Reference : http://blog.saltfactory.net/python/send-mail-via-smtp-and-python.html
'''


class Email:
    def __init__(self):
        # do initialize
        self.ID = None
        self.PASSWORD = None
        self.server = None
        self.FROM = None
        self.TO = None
        self.CC = None
        self.SUBJECT = None
        self.BODY = None

    def login(self):

        # check whether login is failed
        try:
            # self.ID = input("Enter your ID with domain [ex) fly0159@naver.com] : ")
            # self.PASSWORD = input("Enter your PASSWORD : ")

            self.ID = 'fly0159@naver.com'
            self.PASSWORD = 'Kiss5340'
            # connect to server
            server = self.server = smtplib.SMTP('smtp.' + self.ID[self.ID.index('@') + 1:], 587)
            self.server.starttls()

            assert server.login(self.ID, self.PASSWORD)
            self.server.quit()
            print("Login successfully")
        except Exception as e:
            print("Login is failed : {}".format(e.__str__()))

    def send(self):

        # when sending is successfully done, returns Nothing... so I won't use assert
        try:
            # generate MIMEText

            """
            :param TO: e-mail receiver
            :param CC: carbon copy or Co-receiver
            :param SUBJECT: title of e-mail
            :param BODY: main message
            :return: None
            """

            # connect to server
            server = self.server_connect()

            self.TO = input('Enter the receiver : ')
            self.CC = input('Enter the carbon copy [If you have a list of receiver, using a seperator ","] : ')
            self.SUBJECT = input('Enter the title of mail : ')
            self.BODY = input('Enter the message of mail : ')

            # Base class for MIME multipart/* type messages.
            msg = MIMEMultipart()

            msg['From'] = self.ID
            msg['To'] = self.TO.split(',')
            msg['Cc'] = self.CC
            msg['Subject'] = self.SUBJECT
            msg.attach(MIMEText(self.BODY, 'plain'))

            server.sendmail(self.ID, self.TO, msg.as_string())
            print("Sent successfully")
            self.server_quit()

        except Exception as e:
            print("Sending is failed : {}".format(e.__str__()))

    def read(self):
        try:
            # connect to server
            server = imaplib.IMAP4_SSL('imap.' + self.ID[self.ID.index('@') + 1:])

            # login
            server.login(self.ID, self.PASSWORD)
            server.list()
            server.select()

            typ, data = server.search(None, 'ALL')
            for num in data[0].split():
                typ, data = server.fetch(num, '(RFC822)')
                print('Message %s\n%s\n' % (num, data[0][1]))

            server.logout()
        except Exception as e:
            print("Reading is failed : {}".format(e.__str__()))

    def delete(self):
        pass


if __name__ == '__main__':
    email = Email()
    email.login()
    email.read()
