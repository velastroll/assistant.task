import json
import requests
import os

try:
    os.system("echo '[reboot.py] --' > ./logs/log.reboot")
    # extract token
    with open('./cache/token.json', "r") as read_file:
        tkns = json.load(read_file)
    # extract url
    with open('./cache/cache.json', "r") as read_file:
        cache = json.load(read_file)
    # inform about the task
    response = requests.get(
        cache["URL_BASE"] + "/device/task/REBOOT/doing",
        headers={
            'Authorization': str(tkns['access_token'])
        })
    if (response.status_code == 200):
        # do the task
        command = "sudo reboot"
        os.system(command)
    else:
        os.system("echo '[REBOOT.py] Cannot do the action"+ str(response) +"' > ./logs/log.reboot")
except Exception as err:
    os.system("echo '[REBOOT.py] Error: "+ str(err) +"' > ./logs/log.reboot")
