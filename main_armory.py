from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import requests

import time
import os
from twilio.rest import Client

from config import twilio_sid, twilio_auth_token, sender_number, reciever_number


response = requests.get('https://d4armory.io/api/events/recent')



try:
    data = response.json()
    boss_data = data['boss']
    print(boss_data)
    boss_name = boss_data['name']
    boss_expected = boss_data['expected']
except:
    print("Request failed, status code " + str(response.status_code))


current = time.time()
print(current)

diff = boss_expected - current


print(diff)
print(diff/60)

if(diff/60 <= 30.0):
    print("sending msg ")
    print(diff/60)
    print(boss_name)


    client = Client(twilio_sid, twilio_auth_token)
    message = client.messages.create(
        body = "World boss spawning in " +  str(diff/60) +  " minutes (" + boss_name + ").",
        from_ = sender_number,
        to = reciever_number
    )
    print(message.body)
    print(message.sid)

    time.sleep(1800)

time.sleep(60)