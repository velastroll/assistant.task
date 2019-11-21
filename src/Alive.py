import json
import requests
import os


class Alive:
    def __init__(self, accesstoken):
        self.accesstoken = accesstoken
        cache_file = "./cache.json"
        with open(cache_file, "r") as read_file:
            cache = json.load(read_file)
        self.url = cache["URL_ALIVE"]

    def send(self):
        try:
            print('auth: ' + str(self.accesstoken))
            print("url: " + str(self.url))
            response = requests.get(
                'http://virtual.lab.infor.uva.es:65143/device/alive',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': str(self.accesstoken)
                })
            print(response)
            if (response.status_code == 200):
                # it's alive
                print(response.content)
                return True
            elif (response.status_code == 300):
                print('Ha sido 300')
                # parse response
                t = response.content
                print(str(t))
                print('Procediendo a imprimirlo en un archivo...')
                # TODO: DELETE THIS, ITS TO TEST
                comando = "sudo echo '" + t + "' > /home/pi/assistant.task/src/task_retrieved.json"
                os.system(comando)  # execute command
                print('Impreso')
                # receive a new task
                r = json.loads(t)
                print('r = json')
                print('TO DO: ' + str(r[0]['event']))
                return True
            else:
                print('Cannot send alive request: ' + str(response.content))
                return False
        except Exception as err:
            print('Cannot connect to the host: ' + str(err))
            return False
