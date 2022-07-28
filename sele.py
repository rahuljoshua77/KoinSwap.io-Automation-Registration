import undetected_chromedriver as uc
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os, random, time, requests
from multiprocessing import Pool
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
cwd = os.getcwd()
from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
opts = uc.ChromeOptions()
from faker import Faker
fake = Faker() 
opts.headless = False
opts.add_argument('--log-level=3') 

opts.add_argument('--no-sandbox')
opts.add_argument('--disable-setuid-sandbox')
opts.add_argument('disable-infobars')
opts.add_argument('--ignore-certifcate-errors')
opts.add_argument('--ignore-certifcate-errors-spki-list')
opts.add_argument("--incognito")
opts.add_argument('--no-first-run')
opts.add_argument('--disable-dev-shm-usage')
opts.add_argument("--disable-infobars")
opts.add_argument("--disable-extensions")
opts.add_argument("--disable-popup-blocking")
opts.add_argument('--log-level=3') 

def xpath_type(el,mount):
    return wait(browser,10).until(EC.presence_of_element_located((By.XPATH, el))).send_keys(mount)

def xpath_el(el):
    element_all = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, el)))
    
    return browser.execute_script("arguments[0].click();", element_all)

def get_mail():
    n=1
    while True:
        sleep(5)
        if n == 5:
            print(f"[*] [{email_user}]  Verification Failed!")
            break
        import imaplib							
        import email
 
    
        
        # establish connection with Gmail
        server ="imap.gmail.com"					
        imap = imaplib.IMAP4_SSL(server)

        # intantiate the username and the password
        username ="siskaputriutamia@gmail.com"
        password ="GANTI_PASSWORD"

# login into the gmail account

        imap.login(username, password)			

# select the e-mails
        res, messages = imap.select('"[Gmail]/All Mail"')

        # calculates the total number of sent messages
        messages = int(messages[0])
        
        # determine the number of e-mails to be fetched
        n = 1

        # iterating over the e-mails
        collect_msg = []
        for i in range(messages, messages - n, -1):
            res, msg = imap.fetch(str(i), "(RFC822)")	
            data = []
            for response in msg:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    collect_msg.append(msg.as_string())
                    # mes1 = BeautifulSoup(mes.content,'html.parser')
                    #         get_data = mes1.prettify()
        imap.logout()
        #getting the latest message 
 
        try:
            try:
                myfiles = open(f"verif_url.txt","r")
                data_list = myfiles.read()
                list_checks = data_list.split("\n")
                
            except:
                list_checks = ['']
          
            #verif_url = get_data.split('<a href=3D"https://koinswap.io/verify-email/')[1].split('" style=3D"padding: 10px')[0].replace("&amp;",'').replace("\n",'')
            text = str(collect_msg).split('https://koinswap.io/verify-email/')[1]
            split_sig = text.split("&signature=")[1]
        
          
            verif_url = "https://koinswap.io/verify-email/"+text.split("&signature=")[0]+"&signature="+split_sig[0:64]
       
          
            if n == 2:
                sleep(2)
                get_data = str(collect_msg).as_string()
                
            #https://koinswap.io/verify-email/197176/14a340c613f3c67d550177b06cb9d8c8649f4ca4?expires=1656731407&signature=3de766a230bb244cd560f0cadc998f893770f8e17de436ad812d16b57ea770f8
                pass
            else:
                try:
                    n = n+1
                    if any(verif_url in s for s in list_checks): 
                        
                        sleep(1)
                    else:
                        print(f'[*] [{email_user}] URL Verification: {verif_url}')
                        try:
                            browser.get(verif_url.replace("\n']",''))
                            browser.quit()
                        except:
                            pass
                        
                        with open('verif_url.txt','a') as f:
                                f.write(f"{verif_url}\n")
                    
                        list_check.remove(email_user)
                        with open('email.txt','w',encoding='utf-8') as f: f.write(f'')
                        for m in list_check[:]:
                            with open('email.txt','a',encoding='utf-8') as f: f.write(f'{m}\n')
                        break
                except Exception as e:
                    print(e)
                    
                    break
        except Exception as e:
            
            if "list index out of range" == str(e):
                print(f"[*] [{email_user}] Your Email doesn't have a new message, Sleep 5!")
                sleep(5)
            else:
                print(f'[*] [{email_user}] Error: {e}')
            n = n+1
    
    
    
def regis(email):
    global email_user
    global browser
    email_user = email
    browser = uc.Chrome()

    browser.get('https://koinswap.io/register?referralcode=7PSyr7')

    api_key = 'GANTI_API_KEY'
    site_key = '6LeDDX8gAAAAAOhZWVtWTMrYwUocm34MtD6vZ9aI'  # grab from site
    url = 'https://koinswap.io/register?referralcode=7PSyr7'
    
    client = AnticaptchaClient(api_key)
    task = NoCaptchaTaskProxylessTask(url, site_key)
    job = client.createTask(task)
    job.join()
    token_captcha = job.get_solution_response()
 
    xpath_type('//*[@id="first_name"]',fake.first_name())
    xpath_type('//*[@id="last_name"]',fake.last_name())
    xpath_type('//*[@id="email"]',email_user)
    xpath_type('//*[@id="password"]','passwOrd123@@')
    xpath_type('//*[@id="password_confirmation"]','passwOrd123@@')
    browser.execute_script("document.getElementsByClassName('g-recaptcha-response')[0].innerHTML = "
                                    f"'{token_captcha}';")
    xpath_el('//*[@class="btn ripple btn-main-primary btn-block"]')
    get_mail()
    
    
if __name__ == '__main__':
    global list_check
    print("[*] Auto Creator Koinswap")
    #jumlah = input("[*] Multiprocessing: ")
    myfiles = open(f"email.txt","r")
    data_list = myfiles.read()
    list_check = data_list.split("\n")

    start = time.time()
    for i in list_check:
        try:
            regis(i)
        except:
            pass
      
            
    end = time.time()
    print("[*] Time elapsed: ", end - start)
