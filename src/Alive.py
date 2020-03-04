import json
import requests
import os

class Alive:
    def __init__(self, accesstoken):
        self.accesstoken = accesstoken
        cache_file = "./cache/cache.json"
        with open(cache_file, "r") as read_file:
            cache = json.load(read_file)
        self.url = cache["URL_ALIVE"]

    def send(self):
        try:
            response = requests.get(
                self.url,
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': str(self.accesstoken)
                })
            if (response.status_code == 200):
                # it's alive
                return True
            elif (response.status_code == 300):
                # parse response
                t = response.content
                r = json.loads(t)
                # do the task
                println(str(r[0]))
                comando = "sh ./tasks/" + str(r[0]['event']) + "/init.sh"
                os.system(comando)  # execute command
                return True
            else:
                os.system(" echo 'Cannot send alive request: " + str(response.content) + "' > ./logs/log.alive")
                return False
        except Exception as err:
            os.system(" echo 'Cannot send alive request: " + str(err) + "' > ./logs/log.alive")
            return False
