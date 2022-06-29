# import the modules
import imaplib							
import email
from email.header import decode_header
import webbrowser
import os
from time import sleep
# establish connection with Gmail
server ="imap.gmail.com"					
imap = imaplib.IMAP4_SSL(server)

# intantiate the username and the password
username ="***************@gmail.com"
password ="fasdalsdkasdkkosq"

# login into the gmail account

imap.login(username, password)			

# select the e-mails
res, messages = imap.select('"[Gmail]/All Mail"')

# calculates the total number of sent messages
messages = int(messages[0])
 
# determine the number of e-mails to be fetched
n = 1

# iterating over the e-mails
for i in range(messages, messages - n, -1):
    res, msg = imap.fetch(str(i), "(RFC822)")	
    data = []
    for response in msg:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            
            # mes1 = BeautifulSoup(mes.content,'html.parser')
            #         get_data = mes1.prettify()
imap.logout()
