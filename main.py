from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time
import os
from twilio.rest import Client

from config import twilio_sid, twilio_auth_token, sender_number, reciever_number

opt = Options()
opt.add_argument("--headless")
driver = webdriver.Chrome(options=opt)
driver.get('https://diablo4.life/trackers/overview')
driver.implicitly_wait(10)

driver.find_element("xpath", '//*[@class="fc-button fc-cta-consent fc-primary-button"]').click()
boss_status = driver.find_element("xpath", '/html/body/div[1]/main/div/div[6]/div[2]/div[4]/a[1]/div/div/div[1]/div/div/span[1]').text
print(boss_status)

timer = driver.find_element("xpath", '/html/body/div[1]/main/div/div[6]/div[2]/div[4]/a[1]/div/div/div[1]/div/div/span[2]').text
boss_timer = timer[0:2] + ':' + timer[5:7] + ':' + timer[10:12]
print(boss_timer)

boss_name = driver.find_element("xpath", '/html/body/div[1]/main/div/div[6]/div[2]/div[4]/a[1]/div/div/div[1]/h3').text
print(boss_name + '\n')

#time.sleep(100)


if(boss_status == "starts in"):
    print("sending msg")

    client = Client(twilio_sid, twilio_auth_token)
    message = client.messages.create(
    body = "World boss spawning in " + boss_timer +  " (" + boss_name + ").",
    from_ = sender_number,
    to = reciever_number
    )
    print(message.body)
    print(message.sid)

else:
    print("not sending (" + boss_status + ")")