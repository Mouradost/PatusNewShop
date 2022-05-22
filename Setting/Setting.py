from dataclasses import dataclass
import socket
import json
import os
import logging


@dataclass
class ServerSetting:
    IP: str = socket.gethostbyname(socket.gethostname())
    PORT: int = 7800
    MAX_CLIENTS: int = 25
    CASHIER_IP: str = "192.168.1.201"
    KITCHEN_IP: str = "192.168.1.203"
    PIZZA_IP: str = "192.168.1.203"
    BAR_IP: str = "192.168.1.202"
    PATH: str = os.path.join(os.getcwd(), 'Setting', 'Setting.json')

    def save(self):
        with open(self.PATH, 'w') as f:
            json.dump(self.__dict__, f)

    def load(self):
        try:
            with open(self.PATH, "r") as f:
                # print(f)
                settings = json.load(f)
                self.IP = settings['IP']
                self.PORT = settings['PORT']
                self.MAX_CLIENTS = settings['MAX_CLIENTS']
                self.CASHIER_IP = settings['CASHIER_IP']
                self.KITCHEN_IP = settings['KITCHEN_IP']
                self.PIZZA_IP = settings['PIZZA_IP']
                self.BAR_IP = settings['BAR_IP']
        except Exception as e:
            logging.error(f"No settings found --> {e}")
            logging.debug("Saving default settings")
            self.save()
