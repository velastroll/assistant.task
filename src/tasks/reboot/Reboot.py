import json
import requests
import os

try:
    tkns_file = '/home/pi/assistant.task/src/cache/tokens.json'
    with open(tkns_file, "r") as read_file:
        tkns = json.load(read_file)
    response = requests.get(
        'http://virtual.lab.infor.uva.es:65143/device/task/REBOOT/doing',
        headers={
            'Authorization': str(tkns['access_token'])
        })
    print(response)
    if (response.status_code == 200):
        # it's alive
        command = "sudo reboot"
        os.system(command)
    else:
        print('[REBOOT.py] Cannot do the action due to a problem with the server.')
except Exception as err:
    print('[REBOOT.py] There was a problem: ' + str(err))
