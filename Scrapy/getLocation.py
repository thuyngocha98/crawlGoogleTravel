#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import json
from opencage.geocoder import OpenCageGeocode
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome("C:/Users/thuyn/Desktop/chromedriver_win32/chromedriver.exe")
browser.get('https://www.google.com.vn/')
with open("C:/Users/thuyn/Desktop/scrapy/vungtau.json", encoding="utf-8") as json_file:
    data = json.load(json_file)
    for p in data:
        p['code'] = 44
        browser.execute_script("window.open('');")
        browser.switch_to.window(browser.window_handles[1])
        browser.get('https://www.google.com/maps/@9.779349,105.6189045,11z?hl=vi-VN')
        inputElement = browser.find_element_by_id("searchboxinput")
        location = p['title']+ " Vũng Tàu"
        inputElement.send_keys(location)
        inputElement.send_keys(Keys.ENTER)
        url = browser.current_url
        t = 0
        while "data=" not in url and t < 7:
            t = t + 1
            time.sleep(0.5)
            url = browser.current_url
        if "!3d" in url:
            split1 = url.split("!3d")
            split2 = split1[1].split("!4d")
            p['latitude'] = float(split2[0])
            p['longitude'] = float(split2[1].split("?")[0])
            print(split2[0])
        else:
            p['latitude'] = ""
            p['longitude'] = ""
            print("No find: "+location)
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
    browser.close()
with open('vungtau.json', 'w', encoding="utf-8") as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=2)
