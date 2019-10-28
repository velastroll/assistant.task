  
#!/usr/bin/env python3
# coding=utf-8

import requests
import time
import json
from datetime import datetime

cache_file = "/home/pi/assistant.task/src/cache.json"   # sets the name of the cache file
with open (cache_file, "r") as read_file: # open the cache file and read the json
    cache = json.load(read_file)

values = {'action_alive': 'ALIVE'}
tmp = {'action': 'ALIVE'}
while 1==1:
    if (values['action_alive'] == tmp['action']):
        response = requests.post(cache["URL_ALIVE"])    # make a post http request
        x = tmp['action']
        tmp['action'] = str(response.json()['action'])
        print(x == tmp['action'])
        time.sleep(300)