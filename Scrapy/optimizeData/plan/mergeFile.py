#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import glob

result = []
count  = 1
for f in glob.glob("C:/Users/thuyn/Desktop/optimizeData/plan/*.json"):
    with open(f, encoding="utf-8") as infile:
        print(count)
        count = count+1
        data = json.load(infile)
        for p in data:
            result.append(p)
with open('mergeFile.json', 'w', encoding="utf-8") as outfile:
    json.dump(result, outfile, ensure_ascii=False, indent=2)