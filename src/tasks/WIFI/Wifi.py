import json
import requests
import os

try:
    print("[Wifi.py] --")
    print("Updating Wifi credentials")
    # extract token
    with open('./cache/token.json', "r") as read_file:
        tkns = json.load(read_file)
    # extract url
    with open('./cache/cache.json', "r") as read_file:
        cache = json.load(read_file)
    # inform about the task
    response = requests.get(
        cache["URL_BASE"] + "/device/tasks/WIFI/doing",
        headers={
            'Authorization': str(tkns['access_token'])
        })
    if (response.status_code == 200):
        if (response.json()['content']):
            print('Splitting response...')
            ssid = str(response.json()['content']).split(';')
            print(' > ' + str(ssid))
            command = "sudo echo 'ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\n"
            command += "update_config=1\ncountry=ES\n\nnetwork={\nssid=\"" + str(ssid[0]) + "\"\npsk=\"" + str(ssid[1]) + "\"\n}' "
            command += " > /boot/wpa_supplicant.conf"
            print('Generated command: \n' + str(command))
            os.system(command)
            print('Executed command, rebooting the system...')
            os.system("sudo reboot")
    else:
        print("[Updated.py] cannot do the action" + str(response) )
except Exception as err:
    print("[UPDATE.py] Error: "+ str(err))
