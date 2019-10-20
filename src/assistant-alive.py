  
#!/usr/bin/env python3
# coding=utf-8

import requests
import time
import json
from datetime import datetime

cache_file = "/home/pi/assistant.task/src/cache.json"   # sets the name of the cache file
# open the cache file and read the json
with open (cache_file, "r") as read_file:
    cache = json.load(read_file)
# cache_file.close()

values = {'status_alive': 'ALIVE'}
tmp = {'status': 'ALIVE'}
while 1==1:
    if (values['status_alive'] == tmp['status']):
        response = requests.get(cache["URL_ALIVE"])    # make a get http request
        x = tmp['status']
        tmp['status'] = str(response.json()['status'])
        print(x == tmp['status'])
        time.sleep(300)