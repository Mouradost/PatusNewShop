from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox

from DB.DBHandler import DBHelper
from Setting.Setting import ServerSetting
from DB.DbTables import *
import threading
import datetime
import hashlib
import socket
import json


class ServerThread(QtCore.QThread):
    def __init__(self, parent=None):
        super(ServerThread, self).__init__(parent)
        try:
            settings = ServerSetting()
            settings.load()
            print(f"[SERVER] Using setting {settings}")
            self.server = Server(settings=settings)
        except Exception as e:
            print(f"[SERVER] {e}")
            settings = ServerSetting()
            print(f"[SERVER] Using default setting {settings}")
            self.server = Server(settings=settings)

    def run(self):
        self.server.start()

    def stop(self):
        self.server.stop()


class InfoThread(QtCore.QThread):
    UpdateInfo = QtCore.pyqtSignal(int, int, int, int)

    def __init__(self, parent=None):
        super(InfoThread, self).__init__(parent)
        print(f"[INFO THREAD] Starting")
        self.DB = None
        self.active = True

    def run(self):
        print(f"[INFO THREAD] Started")
        try:
            self.DB = DBHelper()
            while self.active:
                print(f"[INFO THREAD] Updating")
                nb_free_tables, nb_busy_tables, nb_month_sells, nb_day_sells = self.DB.getHomeScreenInfo(
                    datetime.datetime.now().strftime("%Y-%m"), datetime.datetime.now().strftime("%Y-%m-%d"))
                self.UpdateInfo.emit(
                    nb_free_tables[0], nb_busy_tables[0], nb_month_sells[0], nb_day_sells[0])
                # sleep for a minute
                self.sleep(60)
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Info thread problem')
            msg.setInformativeText("The top info are not available anymore")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Info thread warning message")
            msg.exec_()
            print(f"[INFO THREAD ERROR] {e}")
            self.active = False
            self.terminate()

    def stop(self):
        print(f"[INFO THREAD] Stopped")
        self.active = False
        self.terminate()


class Server:
    SIZE = 1024
    FORMAT = 'utf-8'
    SEND_TABLES_MSG = "!TABLES"
    SEND_TABLE_MSG = "!TABLE"
    ASK_WHICH_MSG = "!WHICH"
    SEND_PRODUCTS_MSG = "!PRODUCTS"
    RECEIVE_ORDER_MSG = "!ORDER"
    LOGIN_MSG = "!LOGIN"
    ASK_PASSWORD_MSG = "!PASSWORD"
    SEND_CONFIRM_MSG = "!CONFIRM"
    SEND_DENY_MSG = "!DENY"
    STOP_MSG = "!DISCONNECT"

    def __init__(self, settings):
        super(Server, self).__init__()
        self.SETTINGS = settings
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.SETTINGS.IP, self.SETTINGS.PORT))
        self.count = 0
        self.active = False
        self.workers = {}
        print(f"[CONFIG] Server is configured")

    def start(self):
        print(f"[STARTING] Server is started")
        self.active = True
        self.socket.listen(self.SETTINGS.MAX_CLIENTS)
        print(
            f"[LISTENING] Server is listening on {self.SETTINGS.IP}:{self.SETTINGS.PORT}")
        while self.active:
            client_socket, client_address = self.socket.accept()
            thread = threading.Thread(
                target=self.handle_client, args=(client_socket, client_address))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

    def handle_client(self, client_socket, client_address):
        print(f"[NEW CONNECTION] Server is connected to {client_address}")
        connected = True
        db = DBHelper()
        while connected:
            msg = client_socket.recv(self.SIZE).decode(self.FORMAT)

            if msg == self.STOP_MSG:
                print(f"[{client_address}] {msg}")
                connected = False
            elif msg == self.SEND_TABLES_MSG:
                print(f"[{client_address}] {msg}")
                msg_send = json.dumps([x.__dict__ for x in db.getAllTables()])
                client_socket.send((msg_send + "\n").encode(self.FORMAT))
                print(f"[SEND TO {client_address}] {msg_send}")
            elif msg == self.SEND_PRODUCTS_MSG:
                print(f"[{client_address}] {msg}")
                msg_send = json.dumps(
                    [x.__dict__ for x in db.getAllFinishProducts()])
                client_socket.send((msg_send + "\n").encode(self.FORMAT))
                print(f"[SEND TO {client_address}] {msg_send}")
            elif msg == self.SEND_TABLE_MSG:
                print(f"[{client_address}] {msg}")
                client_socket.send(
                    (self.ASK_WHICH_MSG + "\n").encode(self.FORMAT))
                print(f"[SEND TO {client_address}] {self.ASK_WHICH_MSG}")
                msg = client_socket.recv(self.SIZE).decode(self.FORMAT)
                print(f"[RECEIVED FROM {client_address}] {msg}")
                msg_send = json.dumps(
                    [x.__dict__ for x in db.getTableContent(int(msg))[0]])
                client_socket.send((msg_send + "\n").encode(self.FORMAT))
                print(f"[SEND TO {client_address}] {msg_send}")
            elif msg == self.RECEIVE_ORDER_MSG:
                msg = client_socket.recv(self.SIZE).decode(self.FORMAT)
                print(f"[{client_address}] {msg.split('!')}")
                try:
                    data = json.loads(msg)
                except Exception as e:
                    data = json.loads(msg.split('!')[0])
                    print(f"[ERROR {client_address}] {e}")
                    connected = False
                print(f"[{client_address}] {data}")
                total = 0
                current_order = []
                for orderItem in data:
                    current_order.append(OrderItem(**orderItem))
                    total += current_order[-1].orderItemTotal
                if client_address[0] in self.workers.keys():
                    db.insertOrder(current_order, total,
                                   self.workers[client_address[0]].id, 1)
                else:
                    db.insertOrder(current_order, total, 1, 1)
            elif msg == self.LOGIN_MSG:
                username = client_socket.recv(self.SIZE).decode(self.FORMAT)
                print(f"[{client_address}] username: {username}")
                worker = db.getWorkerByUsername(username)
                msg_send = self.ASK_PASSWORD_MSG
                client_socket.send((msg_send + "\n").encode(self.FORMAT))
                print(f"[SEND TO {client_address}] {msg_send}")
                password = client_socket.recv(self.SIZE).decode(self.FORMAT)
                print(f"[{client_address}] password: {password}")
                if password == worker.password:
                    msg_send = self.SEND_CONFIRM_MSG
                    self.workers[client_address[0]] = worker
                elif hashlib.sha3_512(password.encode()).hexdigest() == worker.password:
                    msg_send = self.SEND_CONFIRM_MSG
                    self.workers[client_address[0]] = worker
                else:
                    msg_send = self.SEND_DENY_MSG
                client_socket.send((msg_send + "\n").encode(self.FORMAT))
                print(f"[SEND TO {client_address}] {msg_send}")

        client_socket.close()
        print(
            f"[DISCONNECTION] Server is not connected anymore to {client_address}")
        print(self.workers)

    def stop(self):
        self.active = False
        self.socket.close()
        print(f"[STOPPED] Server is stopped")
