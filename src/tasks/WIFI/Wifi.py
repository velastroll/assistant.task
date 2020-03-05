import json
import requests
import os

try:
    print("[Wifi.py] --")
    print("Updating Wifi credentials")
    # extract token
    with open('./cache/token.json', "r") as read_file:
        tkns = json.load(read_file)
    # extract url
    with open('./cache/cache.json', "r") as read_file:
        cache = json.load(read_file)
    # inform about the task
    response = requests.get(
        cache["URL_BASE"] + "/device/tasks/WIFI/doing",
        headers={
            'Authorization': str(tkns['access_token'])
        })
    print(str(response))
    print(str(response.json()))
    print(str(response.json()['content']))
    cssid = str(response.json()['content`]).split(';')

    if (response.status_code == 200):
        # do the task
        command = "sudo reboot"
        os.system(command)
    else:
        print("[Updated.py] cannot do the action" + str(response) )
except Exception as err:
    print("[UPDATE.py] Error: "+ str(err))
