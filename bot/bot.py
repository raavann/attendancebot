from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys

from time import sleep
from datetime import datetime, timedelta

import os
from dotenv import load_dotenv
load_dotenv()

class meet_bot:
    def __init__(self):
        chrome_options = Options()

        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_experimental_option("prefs", { \
            "profile.default_content_setting_values.media_stream_mic": 2, 
            "profile.default_content_setting_values.media_stream_camera": 2,
            "profile.default_content_setting_values.geolocation": 2, 
            "profile.default_content_setting_values.notifications": 2
        })
        sleep(2)

        self.bot = webdriver.Chrome(options=chrome_options)
        self.bot.implicitly_wait(0.5)
        self.bot.set_page_load_timeout(10)
        sleep(2)
    
    def login(self, email, pas):
        try:
            bot = self.bot
            bot.get('https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&&o_ref=https%3A%2F%2Fmeet.google.com%2F_meet%2Fwhoops%3Fsc%3D232%26alias%3Dmymeetingraheel&_ga=2.262670348.1240836039.1604695943-1869502693.1604695943&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
            sleep(1)
            email_in = bot.find_element_by_id('identifierId')  # enter email
            email_in.send_keys(email)
            next_btn = bot.find_element_by_id('identifierNext')  # next
            next_btn.click()
            sleep(2)
            pas_in = bot.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')  # enter password
            pas_in.send_keys(pas)
            next1_btn = bot.find_element_by_xpath('//*[@id="passwordNext"]/div/button')  # next
            next1_btn.click()
            sleep(3)

            return False
        except:
            return True

    def get_meet(self, meeting_link):
        try:
            bot = self.bot

            bot.get(meeting_link)
            sleep(2)

            # dissmiss button
            try:
                bot.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span').click()
                sleep(3)
                print('found the dissmiss button')
            except:
                print('okay, no did not find the dissmuss button')
                return True

            # IF YOU'RE HERE THEN PAGE LOADED SUCCESSFULLY RETURN FALSE
            print('everthing went well, returning false for some reason')
            return False
        except Exception as e:
            print('something went terrible at 94 returning true at get link\n', e)
            return True

    def join(self):
        bot = self.bot

        sleep(5)
        join = False
        join_btn = ''
        try:
            # join button, ask or join directly has same xpath
            join_btn = bot.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span')
            join = True
        except:
            join = False
            print(join_btn)
        
        if (join):
            join_btn.click()

            sleep(180) # sleep for 3minutes

            try:
                bot.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[2]/div/div[7]/span/button/i')
                sleep(2)
                return 0
            except:
                # No leave button
                return -1
        else:
            # join button do not exist
            return -2
    
    def quit(self):
        bot = self.bot
        bot.quit()
