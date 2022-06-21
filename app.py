from weakref import proxy
from faker import Faker
fake = Faker() 
from multiprocessing import Pool
import requests, time, string
from time import sleep
import random
from requests_html import HTMLSession

session = HTMLSession()
def regis(data):
    random_angka = random.randint(100,999)
    random_angka_dua = random.randint(10,99)
    additonal = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))
    format_email = ['getnada.com','abyssmail.com','boximail.com','clrmail.com','dropjar.com','getairmail.com','givmail.com','inboxbear.com','tafmail.com','vomoto.com']
    email = fake.first_name()+fake.last_name()+str(random_angka)+"@"+random.choice(format_email)
    email = email.lower()
    print(f'[*] [{email}] Trying to Register')
 
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

    api_key = '7bf444b8f62a49c72f3324e371d58321'
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
        "email": email,
        "password": "password123@Os",
        "password_confirmation": "password123@Os",
        "referralcode": "7PSyr7",
        "g-recaptcha-response": token_captcha
    }
 
    check = session.post('https://koinswap.io/register',headers=headers,data=data,allow_redirects=True)
    n = 1
    while True:
        sleep(5)
        if n == 5:
            print(f"[*] [{email}]  Verification Failed!")
            break
        URL = f'https://getnada.com/api/v1/inboxes/{email}'
        
        r = requests.get(URL).json()
        #getting the latest message

        try:
            global uid
            
            uid = r['msgs'][0]['uid']
        
            mes = requests.get(f'https://getnada.com/api/v1/messages/html/{uid}')
            get_data = mes.text
            verif_url = get_data.split('href="https://koinswap.io/verify-email/')[1].split('" style="padding: 10px;')[0]
            verif_url = "https://koinswap.io/verify-email/"+verif_url.replace('amp','').replace(";",'')
            req = session.get(verif_url)
            #print(req.text)
            req.html.render()  
            print(f'[*] [{email}] URL Verification: {verif_url}')
            sleep(10)
            break
        except Exception as e:
         
            print(f"[*] [{email}] Your Email doesn't have a new message, Reload!")
            n = n+1
    
    
if __name__ == '__main__':
 
    global password
    print("[*] Auto Creator Koinswap")
    jumlah = input("[*] Multiprocessing: ")
    loop_input = int(input("[*] How Much Account: "))
    loop = []
    for i in range(1, loop_input+1):
        loop.append(i)
    
    start = time.time()
    with Pool(int(jumlah)) as p:  
        p.map(regis,loop)
      
            
    end = time.time()
    print("[*] Time elapsed: ", end - start)