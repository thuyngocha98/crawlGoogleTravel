#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import glob

result = []
with open("C:/Users/thuyn/Desktop/optimizeData/getDescriptionDetail/noAccentFile.json", encoding="utf-8") as infile1:
    dataMain = json.load(infile1)
with open("C:/Users/thuyn/Desktop/optimizeData/getDescriptionDetail/mergeFile1.json", encoding="utf-8") as infile2:
    data = json.load(infile2)
    for p1 in dataMain:
        p1['description'] = "Not yet description"
        p1['images'] = []
        for p2 in data:
            if p1['title'] == p2['title']:
                p1['description'] = p2['description']
                p1['images'] = p2['images']
                break
with open('fileFull.json', 'w', encoding="utf-8") as outfile:
    json.dump(dataMain, outfile, ensure_ascii=False, indent=2)