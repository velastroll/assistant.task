import json
import requests
import os

try:
    # extract token
    with open('./cache/token.json', "r") as read_file:
        tkns = json.load(read_file)
    # extract url
    with open('./cache/cache.json', "r") as read_file:
        cache = json.load(read_file)
    # inform about the task
    response = requests.get(
        cache["URL_BASE"] + "/device/tasks/OFF/doing",
        headers={
            'Authorization': str(tkns['access_token'])
        })
    if (response.status_code == 200):
        # do the task
        command = "sudo poweroff"
        os.system(command)
    else:
        print("[Off.py] Cannot power off: "+ str(response))
except Exception as err:
    print("[Off.py] Exception: "+ str(err))
