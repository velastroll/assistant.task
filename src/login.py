import os;
import time;
import requests;
import json;

# retrieve MAC
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
print(data + " -> " + c)
x = '{"user": "' + data + '", "password": "' + c + '"}'
credentials = json.loads(x)
print(credentials)

# read URL
# cache_file = "/home/pi/assistant.task/src/cache.json"
cache_file = "./cache.json"
with open (cache_file, "r") as read_file:
    cache = json.load(read_file)
url = cache["URL_LOGIN"]

retrieved = False
# send POST
while (retrieved == False):
  try:
    response = requests.post(url, data = credentials)
    print(response)
    if (response.status_code == 200):
      # save tokens
      tokens = "/home/pi/assistant.task/src/tokens.json"
      with open(tokens, "w") as file:
        file.write(response.content)
      retrieved = True
    else:
      print("Cannot connect... waits 30 second to retry")
      time.sleep(30)
  except Exception as err:
    print("Cannot connect to the host... try again in 30 seconds...")
    time.sleep(30)