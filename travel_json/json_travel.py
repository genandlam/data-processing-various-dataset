#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 17:44:30 2018

@author: genevieve
"""

import json
from pprint import pprint

with open('./Frames-dataset/frames.json') as f:
    data = json.load(f)

pprint(data)