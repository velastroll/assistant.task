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
        confData = requests.get(
            cache["URL_BASE"] + "/device/conf",
            headers={
                'Authorization': str(tkns['access_token'])
            })
        # saves it
        if (confData.status_code == 200):
            confDataJSON = json.load(confData.content)

            # save configuration
            confFILE = './cache/conf.json'
            with open(confFILE, "w") as file:
                file.write(confDataJSON['body'])

            # informs to server about successful task
            response = requests.get(
                cache["URL_BASE"] + "/device/conf/" + confDataJSON["timestamp"],
                headers={
                    'Authorization': str(tkns['access_token'])
                })
            if (response.status_code == 200):
                os.system("echo '[CONF.py] Update configuration: Device should be rebooted")
            else:
                os.system("echo '[CONF.py] Cannot do the action"+ str(response.content) +"' > ./logs/log.conf")
    else:
        os.system("echo '[CONF.py] Cannot do the action"+ str(response.content) +"' > ./logs/log.conf")
except Exception as err:
    os.system("echo '[CONF.py] Error: "+ str(err) +"' > ./logs/log.reboot")
