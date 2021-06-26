import json
import socket
h_name = socket.gethostname()
IP_addres = socket.gethostbyname(h_name)
from datetime import datetime

def add_log(text):
    print(text)
    with open('main/config.json', 'r') as jsonConfig:
        config = json.load(jsonConfig)
        if config['options']['log'] == 'enabled':
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            with open('main/data.log', 'a') as file_object:
                file_object.write('\n'+dt_string+' - '+h_name+'('+IP_addres+')'+': '+text.lower())


