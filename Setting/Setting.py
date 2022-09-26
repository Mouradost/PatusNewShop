from dataclasses import dataclass
import socket
import json
import os
import logging


@dataclass
class ServerSetting:
    SHOP_NAME: str = "Restaurant"
    SHOP_DNS_PROVIDER: str = ""
    SHOP_DOMAIN: str = ""
    SHOP_TOKEN: str = ""
    SHOP_PHONE: str = ""
    SHOP_ADDRESS: str = ""
    SHOP_DISTRICT: str = ""
    KITCHEN_SECRET: str = "KITCHEN_SECRET"

    IP: str = socket.gethostbyname(socket.gethostname())
    PORT: int = 7800
    MAX_CLIENTS: int = 25

    CASHIER_IP: str = "192.168.1.201"
    KITCHEN_IP: str = "192.168.1.203"
    PIZZA_IP: str = "192.168.1.203"
    BAR_IP: str = "192.168.1.202"

    CASHIER_ACTIVE: bool = False
    KITCHEN_ACTIVE: bool = False
    PIZZA_ACTIVE: bool = False
    BAR_ACTIVE: bool = False

    DRAWER_PIN: int = 2
    PATH: str = os.path.join(os.getcwd(), "Setting", "Setting.json")

    def save(self):
        with open(self.PATH, "w") as f:
            json.dump(self.__dict__, f)

    def load(self):
        try:
            with open(self.PATH, "r") as f:
                # print(f)
                settings = json.load(f)

                self.SHOP_NAME = settings["SHOP_NAME"]
                self.SHOP_DNS_PROVIDER = settings["SHOP_DNS_PROVIDER"]
                self.SHOP_DOMAIN = settings["SHOP_DOMAIN"]
                self.SHOP_TOKEN = settings["SHOP_TOKEN"]
                self.SHOP_PHONE = settings["SHOP_PHONE"]
                self.SHOP_ADDRESS = settings["SHOP_ADDRESS"]
                self.SHOP_DISTRICT = settings["SHOP_DISTRICT"]
                self.KITCHEN_SECRET = settings["KITCHEN_SECRET"]

                self.IP = settings["IP"]
                self.PORT = settings["PORT"]
                self.MAX_CLIENTS = settings["MAX_CLIENTS"]

                self.CASHIER_IP = settings["CASHIER_IP"]
                self.KITCHEN_IP = settings["KITCHEN_IP"]
                self.PIZZA_IP = settings["PIZZA_IP"]
                self.BAR_IP = settings["BAR_IP"]

                self.CASHIER_ACTIVE = settings["CASHIER_ACTIVE"]
                self.KITCHEN_ACTIVE = settings["KITCHEN_ACTIVE"]
                self.PIZZA_ACTIVE = settings["PIZZA_ACTIVE"]
                self.BAR_ACTIVE = settings["BAR_ACTIVE"]

                self.DRAWER_PIN = settings["DRAWER_PIN"]
        except Exception as e:
            logging.error(f"No settings found --> {e}")
            logging.debug("Saving default settings")
            self.save()
