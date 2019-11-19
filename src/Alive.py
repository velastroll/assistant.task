import json;
import requests;
import os;

class Alive:

    def __init__(self, accesstoken):
        self.accesstoken = accesstoken
        cache_file = "./cache.json"
        with open (cache_file, "r") as read_file:
            cache = json.load(read_file)
        self.url = cache["URL_ALIVE"]

    def send(self):
        try:
            print('auth: ' + str(self.accesstoken))
            print("url: " + str(self.url)) 
            response = requests.get('http://virtual.lab.infor.uva.es:65143/device/alive', 
                headers={'Content-Type':'application/json',
                'Authorization': str(self.accesstoken)})
            print(response)
            if (response.status_code == 200):
                # it's alive
                print(response.content)
                return True
            elif (response.status_code == 300):
                # parse response
                t = response.text()
                r = response.json()

                # TODO: DELETE THIS, ITS TO TEST
                macfile = "/home/pi/assistant.task/src/macfile.txt"
                comando = "echo '"  + t + "' > task_retrieved.json"
                os.system(comando) # execute command

                # receive a new task
                if (r['action'] == 'EXE'):
                    print(r['command'])
                elif (r['action'] == 'UPDATE'):
                    print(r['file'])
                print('status_code: 300')
            else:
                print('Cannot send alive request: ' + str(response.content))
                return False
        except Exception as err:
            print('Cannot connect to the host: ' + str(err))
            return False
