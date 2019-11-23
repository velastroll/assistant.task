import json;
import time;
import os;
import requests;
import Login;
import Alive;

# método principal
while(1==1):
    login = Login.Login()
    semaphore = login.signin()
    # ALIVE solo si está logeado
    while (semaphore):
        tokens = json.loads(login.tokens)
        alive = Alive.Alive(tokens["access_token"])
        semaphore = alive.send()
        # espera para la siguiente petición
        time.sleep(60)
