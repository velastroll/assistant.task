  
#!/usr/bin/env python3
# coding=utf-8

import requests
import time
import json
from datetime import datetime

cache_file = "cache.json"   # sets the name of the cache file
# open the cache file and read the json
with open (cache_file, "r") as read_file:
    cache = json.load(read_file)

status = "ALIVE"
while 1==1:
    if (status is "ALIVE"):
        response = requests.get(cache["URL_ALIVE"])    # make a get http request
        status = response.json()["status"]
        time.sleep(30)