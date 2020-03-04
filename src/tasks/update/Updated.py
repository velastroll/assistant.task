import json
import requests
import os

try:
    os.system("echo '[updated.py] --' > ./logs/log.ipdated")
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
except Exception as err:
    os.system("echo '[UPDATE.py] Error: "+ str(err) +"' > ./logs/log.updated")
