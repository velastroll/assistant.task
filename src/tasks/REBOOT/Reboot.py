import json
import requests
import os

try:
    os.system('[reboot.py] --')
    tkns_file = '/home/pi/assistant.task/src/cache/tokens.json'
    with open(tkns_file, "r") as read_file:
        tkns = json.load(read_file)
    os.system('[reboot.py] READ FILE')
    response = requests.get(
        'http://virtual.lab.infor.uva.es:65143/device/task/REBOOT/doing',
        headers={
            'Authorization': str(tkns['access_token'])
        })
    os.system(str(response))
    print(response)
    if (response.status_code == 200):
        # it's alive
        command = "sudo reboot"
        os.system(command)
    else:
        os.system('[reboot.py] ELSE')
        print('[REBOOT.py] Cannot do the action due to a problem with the server.')
except Exception as err:
    os.system('[reboot.py] ERROR')
    print('[REBOOT.py] There was a problem: ' + str(err))
