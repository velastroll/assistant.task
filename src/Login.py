import os;
import time;
import requests;
import json;

class Login:
    # initializer
    def __init__(self):
        # retrieve MAC of device
        macfile = "./cache/macfile.txt"
        comando = "sudo ifconfig | grep ether > " + macfile
        os.system(comando)
        # wait to do more safe
        time.sleep(2) 
        # extract MAC
        with open(macfile, "r") as file: 
            data = file.readline().replace('ether', '').replace("\t", '').replace("\n", '').replace(" ", '')[:17]
        with open(macfile, "w") as file:
            file.write(data)
        # Generate credentials to sign in.
        tmp = data
        c = "K" + tmp[9:11] + "U" + tmp[15:17] + "i" + tmp[3:5] + "l" + tmp[12:14] + "p" + tmp[0:2] + "P" + tmp[6:8] + "j" 
        x = '{"user": "' + data + '", "password": "' + c + '"}'
        credentials = json.loads(x)
        self.credentials = credentials

    def signin(self):
        cache_file = "./cache/cache.json"
        with open (cache_file, "r") as read_file:
            cache = json.load(read_file)
        url = cache["URL_LOGIN"]
        try:
            # sign in the system
            response = requests.post(url, data = self.credentials)
            if (response.status_code == 200):
                # save tokens
                tokens = './cache/tokens.json'
                with open(tokens, "w") as file:
                    file.write(response.content)
                self.tokens = response.content
                return True
            else:
                os.system("echo '[login] Cannot sign in: " + str(response.content) + "' > ./logs/log.login")
                return False
        except Exception as err:
            os.system("echo '[login] Cannot connect to the host: " + str(err) + "' > ./logs/log.login")
            return False
