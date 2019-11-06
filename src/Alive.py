import json;
import requests;


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
                # save tokens
                print(response.content)
                return True
            else:
                print('Cannot send alive request: ' + str(response.content))
                return False
        except Exception as err:
            print('Cannot connect to the host: ' + str(err))
            return False
