import json
import requests
import os

try:
    os.system("echo '[Conf.py] --' > ./logs/log.conf")
    # extract token
    with open('./cache/token.json', "r") as read_file:
        tkns = json.load(read_file)
    # extract url
    with open('./cache/cache.json', "r") as read_file:
        cache = json.load(read_file)
    # inform about the task
    response = requests.get(
        cache["URL_BASE"] + "/device/task/CONF/doing",
        headers={
            'Authorization': str(tkns['access_token'])
        })
    if (response.status_code == 200):
        # retrieves config
        response = requests.get(
            cache["URL_BASE"] + "/device/conf",
            headers={
                'Authorization': str(tkns['access_token'])
            })
        # saves it
        if (response.status_code == 200):
            conf = './cache/conf.json'
            with open(conf, "w") as file:
                file.write(response.content)
                self.tokens = response.content

            # informs to server about successful task
            response = requests.get(
                cache["URL_BASE"] + "/device/conf/" + json.load(response.content)["timestamp"],
                headers={
                    'Authorization': str(tkns['access_token'])
                })
    else:
        os.system("echo '[CONF.py] Cannot do the action"+ str(response.content) +"' > ./logs/log.conf")
except Exception as err:
    os.system("echo '[CONF.py] Error: "+ str(err) +"' > ./logs/log.reboot")
