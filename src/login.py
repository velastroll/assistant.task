import os;
import time;
import requests;
import json;

class Login:
    # initializer
    def __init__(self):
        macfile = "/home/pi/assistant.task/src/cache/macfile.txt"
        comando = "sudo ifconfig | grep ether > " + macfile
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
	print('[login] Credentials: ' + str(credentials))
        self.credentials = credentials

    def signin(self):
        cache_file = "./cache/cache.json"
        with open (cache_file, "r") as read_file:
            cache = json.load(read_file)
        url = cache["URL_LOGIN"]
	print("[login] post: " + str(url))
        try:
            response = requests.post(url, data = self.credentials)
            print('[login] post...')
            if (response.status_code == 200):
                # save tokens
                tokens = '/home/pi/assistant.task/src/cache/tokens.json'
                with open(tokens, "w") as file:
                    file.write(response.content)
                self.tokens = response.content
                return True
            else:
                print('[login] Cannot sign in: ' + str(response.content))
                return False
        except Exception as err:
            print('[login] Cannot connect to the host: ' + str(err))
            return False
