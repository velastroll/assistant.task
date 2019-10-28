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
    data = file.readline().replace('ether', '').replace("\t", '').replace("\n", '').replace(" ", '')
with open(macfile, "w") as file:
    file.write(data)

# Generate credentials
tmp = data
c = "K" + tmp[9:11] + "U" + tmp[14:16] + "i" + tmp[3:5] + "l" + tmp[12:14] + "p" + tmp[0:2] + "P" + tmp[6:8] + "j" 
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

# send POST
response = requests.post(url, data = credentials)
print(response)

if (response.status == 200):
   print("Yu-hu!")
   print(response.data)
else:
   print("Oups!")