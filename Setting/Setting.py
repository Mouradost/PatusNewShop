from dataclasses import dataclass
import socket
import json
import os


@dataclass
class ServerSetting:
    IP: str = socket.gethostbyname(socket.gethostname())
    PORT: int = 7800
    MAX_CLIENTS: int = 5
    PATH: str = os.path.join(os.getcwd(), 'Setting', 'Setting.json')

    def save(self):
        with open(self.PATH, 'w') as f:
            json.dump(self.__dict__, f)

    def load(self):
        try:
            with open(self.PATH, "r") as f:
                settings = json.load(f)
            self.IP = settings['IP']
            self.PORT = settings['PORT']
            self.MAX_CLIENTS = settings['MAX_CLIENTS']
        except Exception as e:
            print(f"No settings found --> {e}")
            print("Saving default settings")
            self.save()
