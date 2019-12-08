import json;
import time;
import os;
import requests;
import Login;
import Alive;

# metodo principal
while(1==1):
    login = Login.Login()
    semaphore = login.signin()
    # extract token
    with open('./cache/conf.json', "r") as read_file:
        conf = json.load(read_file)
    # ALIVE solo si esta logeado
    while (semaphore):
        tokens = json.loads(login.tokens)
        alive = Alive.Alive(tokens["access_token"])
        semaphore = alive.send()
        # espera para la siguiente peticion
        time.sleep(conf["sleep_sec"])