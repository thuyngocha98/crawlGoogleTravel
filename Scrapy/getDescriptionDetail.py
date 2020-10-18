#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import json
from opencage.geocoder import OpenCageGeocode
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import urllib.request
import uuid
from PIL import Image
import asyncio
async def main():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    browser = webdriver.Chrome("C:/Users/thuyn/Desktop/chromedriver_win32/chromedriver.exe", chrome_options=chrome_options)

    uri = 'https://www.google.com/travel/things-to-do/see-all?dest_mid=%2Fm%2F03qjsf&dest_state_type=sattd&dest_src=yts&hl=vi&gl=VN&g2lb=2502548%2C4258168%2C4270442%2C4271060%2C4306835%2C4317915%2C4322823%2C4328159%2C4371335%2C4401769%2C4419364%2C4425458%2C4428792%2C4433754%2C4437438%2C4444000%2C4447566%2C4450122&tcfs=EiQKCS9tLzAzcWpzZhIXVGjDoG5oIHBo4buRIFbFqW5nIFTDoHU#ttdm=10.329787_107.084342_13&ttdmf=%252Fg%252F121vfhvz'
    browser.get(uri)
    locations = browser.find_elements_by_class_name("f4hh3d")
    data = []
    for locate in locations:
        try:
            locate.click()
            time.sleep(1)
            element = browser.find_element_by_class_name("U4rdx")
            while element is None:
                time.sleep(0.5)
                element = browser.find_element_by_class_name("U4rdx")
            description = element.find_element_by_class_name("NYYuTb").text
            t = 0
            while description is None and t < 7:
                t = t + 1
                time.sleep(0.5)
                description = element.find_element_by_class_name("NYYuTb").text
            images = element.find_elements_by_class_name("R1Ybne")
            title = element.find_element_by_class_name("HVJNrc").text
            listImage = []
            if description is None:
                description = "Not yet description"
            for i in range(3):
                if images[i].get_attribute("src") is not None:
                    pathDown = 'images/download/'+str(uuid.uuid4())+'.jpg'
                    urllib.request.urlretrieve(images[i].get_attribute("src"), pathDown)
                    basewidth = 200
                    img = Image.open(pathDown)
                    filename = str(uuid.uuid4())+'.jpg'
                    wpercent = (basewidth/float(img.size[0]))
                    hsize = int((float(img.size[1])*float(wpercent)))
                    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
                    img.save('images/resize/' + filename)
                    listImage.append(filename)
            obj = {
              "description": description,
              "images": listImage,
              "title": title
            }
            data.append(obj)
            print(title)
        except:
            print("errorrrrrrrrrrrrrrrrrrrrrrrrrrrr:   "+title)
    with open('vungtau.json', 'w', encoding="utf-8") as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=2)
    browser.close()
asyncio.run(main())
