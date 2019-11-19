import json;
import time;
import os;
import requests;
import Login;
import Alive;

while(1==1):
    login = Login.Login()
    semaphore = login.signin()
    while (semaphore):
        tokens = json.loads(login.tokens)
        alive = Alive.Alive(tokens["access_token"])
        r = alive.send()
        print('[main] alive: ' + str(r))
        time.sleep(300)
        # no se puede mandar peticion, logear de nuevo
        sempahore = r
