import json
import requests
import os

try:
    os.system("echo '[updated.py] --'")
    print("Updating Update")
    # extract token
    with open('./cache/token.json', "r") as read_file:
        tkns = json.load(read_file)
    # extract url
    with open('./cache/cache.json', "r") as read_file:
        cache = json.load(read_file)
    # inform about the task
    response = requests.get(
        cache["URL_BASE"] + "/device/tasks/UPDATE/doing",
        headers={
            'Authorization': str(tkns['access_token'])
        })
    print(str(response))
    if (response.status_code == 200):
        # do the task
        command = "sudo reboot"
        os.system(command)
    else:
        os.system("echo '[Updated.py] cannot do the action" + str(response) + "'")
except Exception as err:
    os.system("echo '[UPDATE.py] Error: "+ str(err) +"'")
