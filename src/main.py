import json;
import time;
import os;
import requests;

while(1==1):
    login = Login()
    while (login.signin()):
        alive = Alive(login.tokens.access_token)
        alive.send()
        time.sleep(300)

class Login:
    # initializer
    def __init__(self):
        macfile = "macfile.txt"
        comando = "ifconfig | grep ether > " + macfile
        os.system(comando) # execute command
        # wait to do more safe
        time.sleep(2) 
        # extract MAC
        with open(macfile, "r") as file: 
            data = file.readline().replace('ether', '').replace("\t", '').replace("\n", '').replace(" ", '')[:17]
        with open(macfile, "w") as file:
            file.write(data)
        # Generate credentials
        tmp = data
        c = "K" + tmp[9:11] + "U" + tmp[15:17] + "i" + tmp[3:5] + "l" + tmp[12:14] + "p" + tmp[0:2] + "P" + tmp[6:8] + "j" 
        x = '{"user": "' + data + '", "password": "' + c + '"}'
        credentials = json.loads(x)
        self.credentials = credentials

    def signin(self):
        cache_file = "./cache.json"
        with open (cache_file, "r") as read_file:
            cache = json.load(read_file)
        url = cache["URL_LOGIN"]

        try:
            response = requests.post(url, data = credentials)
            print(response)
            if (response.status_code == 200):
                # save tokens
                tokens = '/home/pi/assistant.task/src/tokens.json'
                with open(tokens, "w") as file:
                    file.write(response.content)
                self.tokens = response.content
                return True
            else:
                print('Cannot sign in.')
                return False
        except Exception as err:
            print('Cannot connect to the host.')
            return False

class Alive:

    def __init__(self, accesstoken):
        self.accesstoken = accesstoken
        cache_file = "./cache.json"
        with open (cache_file, "r") as read_file:
            cache = json.load(read_file)
        self.url = cache["URL_ALIVE"]

    def send(self):
        try:
            response = requests.post(url, 
                headers={'Content-Type':'application/json',
                'Authorization': '{}'.format(self.accesstoken)})
            print(response)
            if (response.status_code == 200):
                # save tokens
                print(response.content)
                return True
            else:
                print('Cannot sign in.')
                return False
        except Exception as err:
            print('Cannot connect to the host.')
            return False