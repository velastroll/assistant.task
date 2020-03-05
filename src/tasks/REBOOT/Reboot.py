import json
import requests
import os

try:
    print("[reboot.py] --")
    # extract token
    with open('./cache/token.json', "r") as read_file:
        tkns = json.load(read_file)
    # extract url
    with open('./cache/cache.json', "r") as read_file:
        cache = json.load(read_file)
    # inform about the task
    response = requests.get(
        cache["URL_BASE"] + "/device/tasks/REBOOT/doing",
        headers={
            'Authorization': str(tkns['access_token'])
        })
    if (response.status_code == 200):
        # do the task
        command = "sudo reboot"
        os.system(command)
    else:
        print("[REBOOT.py] Cannot do the action")
except Exception as err:
    print("[REBOOT.py] Error: " + str(err))
