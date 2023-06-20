from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time
import os
from twilio.rest import Client
from config import twilio_sid, twilio_auth_token, sender_number, reciever_number

while(True):
    opt = Options()
    opt.add_argument("--headless")
    driver = webdriver.Chrome(options=opt)
    driver.get('https://d4armory.io/events/')
    driver.implicitly_wait(10)

    boss_timer = driver.find_element("xpath", '//*[@id="bossSpawnTime"]').text
    datetime_format = "%d/%m/%Y, %H:%M:%S"
    converted_date = datetime.strptime(boss_timer, datetime_format)
    boss_name = driver.find_element("xpath", '//*[@id="bossName"]').text
    curr_time = datetime.now()
    spawn_timer = converted_date - curr_time
    spawn_timer = spawn_timer.total_seconds()/60
    print(str(spawn_timer)[0:2])

    if(spawn_timer <= 30):
        print("starts in " + str(spawn_timer))
        print("sending msg ")
        client = Client(twilio_sid, twilio_auth_token)
        message = client.messages.create(
            body = "World boss spawning in " + str(spawn_timer)[0:2] + " minutes (" + name2 + ").",
            from_ = sender_number,
            to = reciever_number
        )
        print(message.body)
        print(message.sid)
        time.sleep(60*50)

    time.sleep(60*1)