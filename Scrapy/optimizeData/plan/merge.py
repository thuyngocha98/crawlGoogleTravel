#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import json
with open("C:/Users/thuyn/Desktop/scrapy/plan/vinhahlong.json", encoding="utf-8") as json_file1:
    data1 = json.load(json_file1)
with open("C:/Users/thuyn/Desktop/optimizeData/vinhhalong.json", encoding="utf-8") as json_file2:
    data2 = json.load(json_file2)
    for p1 in data1:
        for p2 in data2:
            if(p1['title'] == p2['title']):
                p1['code'] = p2['code']
                p1['latitude'] = p2['latitude']
                p1['longitude'] = p2['longitude']

with open('vinhhalong.json', 'w', encoding="utf-8") as outfile:
    json.dump(data1, outfile, ensure_ascii=False, indent=2)