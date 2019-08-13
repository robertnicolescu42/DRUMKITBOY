import smtplib
from urllib import request
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import requests
import urllib.request
from bs4 import BeautifulSoup

def getmails():
    filename = 'mails.txt'
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

#input("execute?")
#imi trimit singur mail
sender = "drumkitboydrumkitboy@gmail.com"
recipients = getmails()
passd = input("Drumkitboy password: ")


##########################################################


def getlink():
    fp = urllib.request.urlopen("https://api.hackertarget.com/pagelinks/?q=https://www.reddit.com/r/Drumkits/top/?sort=top&t=week")
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    links = mystr.splitlines()
    return links[12]

#fac rost de link
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = ", ".join(recipients)
msg['Subject'] = 'Your weekly drumkit is here!'

body = "Hey, here's the top drumkit this week from /r/drumkits! " + getlink()
msg.attach(MIMEText(body,'plain'))

text = msg.as_string()

#pun linkul in text

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, passd)
print("The login was done succesfully !")
server.sendmail(sender, recipients, text)
print("The email was sent to ", recipients)

input("press enter")
