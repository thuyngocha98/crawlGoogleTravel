#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from unidecode import unidecode

with open("C:/Users/thuyn/Desktop/optimizeData/main/main.json", encoding="utf-8") as infile:
    data = json.load(infile)
    for p in data:
        p['noAccent'] = unidecode(p['title']).lower()

with open('noAccentFile.json', 'w', encoding="utf-8") as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=2)