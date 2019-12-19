import json
import requests
import os

try:
    # extract token
    with open('./cache/token.json', "r") as read_file:
        tkns = json.load(read_file)
    read_file.close()
    # extract url
    with open('./cache/cache.json', "r") as read_file:
        cache = json.load(read_file)
    read_file.close()
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
            # save configuration
            confFILE = './cache/conf.json'
            with open(confFILE, "w") as file:
                file.write(confData.content)
            file.close()
            # informs to server about successful task
            print('> confirm update')
            print(confData)
	    print(confData.content)
	    print(confData.json())
	    response = requests.put(
                cache["URL_BASE"] + "/device/conf/" + confData.json()["timestamp"],
                headers={
                    'Authorization': str(tkns['access_token'])
                })
            print('> Confirmed')
except Exception as err:
    print("[CONF.py] Error: "+ str(err))
