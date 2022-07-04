from faker import Faker
fake = Faker() 
from bs4 import BeautifulSoup
from multiprocessing import Pool
import requests, time, string
from time import sleep
import random

def regis(data):
    session = requests.Session()
    email_user = data
    print(f'[*] [{email_user}] Trying to solving captcha first!')
 
    headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "en-US,en;q=0.9,ru;q=0.8,id;q=0.7",
    "cache-control": "max-age=0",
    "content-type": "application/x-www-form-urlencoded",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\", \"Google Chrome\";v=\"102\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    #"cookie": "referralcode=7PSyr7; XSRF-TOKEN=eyJpdiI6IkNRNGpKTnBwVG4zbElsVEl3cW5IeEE9PSIsInZhbHVlIjoiOVh0elp6dmFScFJ3OU9TWjVER3Qvdis2ZFp6WmFuZ1lNTzNVS0RBY3RHMytxVFR4OVJmNlpWQTlWMkpIc0VQN0I2R2R1VHhCWVdtSlRINzBPUTNuLy9hdmJyK2tqMUVyZjJWenI0ZjllN0pQVlJHTTl6MTlzdE1nVkkzeUlxbmciLCJtYWMiOiI3ZjQ2ZTI1OTkwMzliNmFmMjhkZDI4NjdjZWNmZDk0YTc3ZmUzNmFhOTIyNWU3YTRlNTZjMWM5NDFlOGE3OWY5In0%3D; koinswap_session=eyJpdiI6IklJczVQUjdSZUR5a29GQUZ6RFp2UGc9PSIsInZhbHVlIjoic1JBVXZGV3Jkb2Y2K3FpUmY5eFBSNEkrUUEya3JqQW5NRG1ZT3Uwc3MvQm5KOXM5ZUlCMjI3ekVzRGhhMEZCenZwLytNUGoydzdhVlp0aTRWSCtEemFXcmsrUnNSMGJPVzB2VUZYSGFFYzZyekdINjQyZXg0cGxNWWgxVVhVRloiLCJtYWMiOiJjMGY4N2ZiMTk4YzhjMzNiN2E2YjQ5MGZkZTlhMjVjM2RlNDkyYjJjZTUzYTJmYTMxMDBiMjAzZTFlOThiN2JlIn0%3D",
    #"Referer": "https://koinswap.io/register?referralcode=7PSyr7&fbclid=IwAR33kKeo4y44g1uLG78Go5F7_xJoxvVwZeQ3gj8kf8SpOI-7oT5yj9gJH-8",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  }
    
    from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask

    api_key = 'apikeyganti'
    site_key = '6LeDDX8gAAAAAOhZWVtWTMrYwUocm34MtD6vZ9aI'  # grab from site
    url = 'https://koinswap.io/register?referralcode=7PSyr7'

 
    
    client = AnticaptchaClient(api_key)
    task = NoCaptchaTaskProxylessTask(url, site_key)
    job = client.createTask(task)
    job.join()
    token_captcha = job.get_solution_response()
    check = session.get('https://koinswap.io/register?referralcode=7PSyr7',headers=headers)
    
    get_token = check.text
    _token = get_token.split('''name="_token" value="''')[1].split('''"> <div class="form-group text-start">''')[0]
     
    data = {
        "_token": _token,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": email_user,
        "password": "password123@Os",
        "password_confirmation": "password123@Os",
        "referralcode": "7PSyr7",
        "g-recaptcha-response": token_captcha
    }
    print(f'[*] [{email_user}] Trying to registrating!')
    check = session.post('https://koinswap.io/register',headers=headers,data=data,allow_redirects=True)
    n = 1
    while True:
        sleep(5)
        if n == 5:
            print(f"[*] [{email_user}]  Verification Failed!")
            break
        import imaplib							
        import email
        from email.header import decode_header
        import webbrowser
        import os
        
        # establish connection with Gmail
        server ="imap.gmail.com"					
        imap = imaplib.IMAP4_SSL(server)

        # intantiate the username and the password
        username ="siskaputriutamia@gmail.com"
        password ="PASSWORDGANTI"

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
        #getting the latest message 
 
        try:
            try:
                myfiles = open(f"verif_url.txt","r")
                data_list = myfiles.read()
                list_check = data_list.split("\n")
                
            except:
                list_check = ['']
          
            #verif_url = get_data.split('<a href=3D"https://koinswap.io/verify-email/')[1].split('" style=3D"padding: 10px')[0].replace("&amp;",'').replace("\n",'')
            text = msg.as_string().split('https://koinswap.io/verify-email/')[1]
 
            verif_url = "https://koinswap.io/verify-email/"+text
          
            if n == 2:
                sleep(2)
                get_data = msg.as_string()
                
            #https://koinswap.io/verify-email/197176/14a340c613f3c67d550177b06cb9d8c8649f4ca4?expires=1656731407&signature=3de766a230bb244cd560f0cadc998f893770f8e17de436ad812d16b57ea770f8
                pass
            else:
                try:
                    n = n+1
                    if any(verif_url in s for s in list_check): 
                        
                        sleep(1)
                    else:
                        print(f'[*] [{email_user}] URL Verification: {verif_url}')
                    
                        with open('verif_url.txt','a') as f:
                                f.write(f"{verif_url}\n")
                        req = session.get(verif_url,timeout=10)
                        session.cookies.clear()
                        break
                except Exception as e:
                    print(e)
                    
                    break
        except Exception as e:
            print(e)
            if "list index out of range" == str(e):
                print(f"[*] [{email_user}] Your Email doesn't have a new message, Sleep 5!")
                sleep(5)
            else:
                print(f'[*] [{email_user}] Error: {e}')
            n = n+1
    
    
if __name__ == '__main__':
 
    global password
    print("[*] Auto Creator Koinswap")
    #jumlah = input("[*] Multiprocessing: ")
    myfiles = open(f"email.txt","r")
    data_list = myfiles.read()
    list_check = data_list.split("\n")

    start = time.time()
    for i in list_check:
        regis(i)
      
            
    end = time.time()
    print("[*] Time elapsed: ", end - start)
