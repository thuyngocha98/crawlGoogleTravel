#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import glob

result = []
for f in glob.glob("C:/Users/thuyn/Desktop/optimizeData/*.json"):
    with open(f, encoding="utf-8") as infile:
        data = json.load(infile)
        for p in data:
            result.append(p)

with open('mergeFile.json', 'w', encoding="utf-8") as outfile:
    json.dump(result, outfile, ensure_ascii=False, indent=2)