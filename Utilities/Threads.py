from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from DB.DBHandler import DBHelper
from Setting.Setting import ServerSetting
from Utilities.UiUtilities import prepareTicketForOrder, prepareTicketForCashier, prepareTicketForReceipt
from DB.DbTables import *
import datetime
import hashlib
import socket
import json
from escpos.printer import Network
import os


class InfoThread(QtCore.QThread):
    UpdateInfo = QtCore.pyqtSignal(int, int, int, int)
    logUpdater = pyqtSignal(str, bool)

    def __init__(self, parent=None):
        super(InfoThread, self).__init__(parent)
        self.DB = DBHelper()
        self.active = True

    def run(self):
        self.logUpdater.emit(f"[INFO THREAD] Started", False)
        try:
            while self.active:
                self.logUpdater.emit(f"[INFO THREAD] Updating", False)
                nb_free_tables, nb_busy_tables, nb_month_sells, nb_day_sells = self.DB.getHomeScreenInfo(
                    datetime.datetime.now().strftime("%Y-%m"), datetime.datetime.now().strftime("%Y-%m-%d"))
                self.UpdateInfo.emit(
                    nb_free_tables[0], nb_busy_tables[0], nb_month_sells[0], nb_day_sells[0])
                # sleep for a minute
                self.sleep(60)
        except Exception as e:
            self.logUpdater.emit(f"[INFO THREAD ERROR] {e}", True)
            self.active = False
            self.terminate()

    def stop(self):
        self.logUpdater.emit(f"[INFO THREAD] Stopped", False)
        self.active = False
        self.terminate()


@dataclass
class Client:
    name: str = None
    socket: object = None
    address: str = None


class ServerThread(QThread):
    addClient = pyqtSignal(Client)
    removeClient = pyqtSignal(str)
    logUpdater = pyqtSignal(str, bool)
    tablesUpdated = pyqtSignal()
    updateServerStatus = pyqtSignal(str)
    printerCall = pyqtSignal(str, list, str, int, bool, float, QThread)
    SIZE = 1024
    FORMAT = 'utf-8'

    def __init__(self):
        super(ServerThread, self).__init__()
        self.SETTINGS = ServerSetting()
        self.socket = None
        self.count = 0
        self.active = False
        self.clients = []

    def run(self):
        try:
            self.SETTINGS.load()
            self.logUpdater.emit(
                f"[SERVER] Load setting: {self.SETTINGS}", False)
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.bind((self.SETTINGS.IP, self.SETTINGS.PORT))
        except Exception as e:
            self.logUpdater.emit(f"[SERVER] {e}", True)
            self.SETTINGS = ServerSetting()
            self.logUpdater.emit(
                f"[SERVER] Trying default setting \n {self.SETTINGS}", False)
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.bind((self.SETTINGS.IP, self.SETTINGS.PORT))
        self.updateServerStatus.emit(
            f"Server started on {self.SETTINGS.IP}:{self.SETTINGS.PORT}")

        try:
            self.logUpdater.emit("[SERVER] Server is configured", False)
            self.active = True
            self.socket.listen(self.SETTINGS.MAX_CLIENTS)
            self.logUpdater.emit(
                f"[SERVER] Server is listening on {self.SETTINGS.IP}:{self.SETTINGS.PORT}", False)
            while self.active:
                client_socket, client_address = self.socket.accept()
                client_socket.settimeout(1000)
                clientHandler = ClientHandler(
                    client=Client(
                        socket=client_socket,
                        address=client_address[0]),
                    removeClient=self.removeClient,
                    addClient=self.addClient,
                    logUpdater=self.logUpdater,
                    tablesUpdated=self.tablesUpdated,
                    printerCall=self.printerCall
                )
                clientHandler.signalFinish.connect(self.removeClientHandler)
                self.clients.append(clientHandler)
                clientHandler.start()
                self.logUpdater.emit(
                    f"[SERVER] Active connection: {len(self.clients)}", False)
        except Exception as e:
            self.logUpdater.emit(f"[SERVER] {e}", True)
            self.stop()

    def removeClientHandler(self, clientHandler):
        try:
            self.clients.remove(clientHandler)
            self.logUpdater.emit(
                f"[SERVER] Client list size: {len(self.clients)}", False)
        except Exception as e:
            self.logUpdater.emit(
                f"[SERVER] Client list size: {len(self.clients)}", False)

    def ringClient(self, client):
        for clientHandler in self.clients:
            if clientHandler.client == client:
                clientHandler.ring()

    def messageClient(self, client, msg):
        for clientHandler in self.clients:
            if clientHandler.client == client:
                clientHandler.messageMe(msg)

    def notifyClients(self, signal):
        for clientHandler in self.clients:
            clientHandler.notifyChange(signal)

    def notifyClient(self, signal, client):
        client.messageRaw(signal)

    def stop(self):
        self.active = False
        for client in self.clients:
            client.stop()
        self.socket.close()
        self.logUpdater.emit("[SERVER] Server is stopped", False)
        self.updateServerStatus.emit(
            f"Server closed")
        self.quit()


class ClientHandler(QThread):
    SIZE = 1024
    FORMAT = 'utf-8'
    signalFinish = pyqtSignal(QThread)

    def __init__(self, client, addClient, removeClient, logUpdater, tablesUpdated, printerCall):
        super(ClientHandler, self).__init__()
        self.SETTINGS = ServerSetting()
        self.client = client
        self.addClient = addClient
        self.removeClient = removeClient
        self.logUpdater = logUpdater
        self.tablesUpdated = tablesUpdated
        self.printerCall = printerCall
        self.start_time = ""
        self.end_time = ""

        self.connected = True
        self.worker = None
        self.logUpdater.emit(
            f"[SERVER] New connection: Connected to {self.client.address}", False)
        self.db = DBHelper()

    def run(self):
        while self.connected:
            try:
                msg = ""
                receiving = True
                while (receiving and self.connected):
                    msg += self.client.socket.recv(
                        self.SIZE).decode(self.FORMAT)
                    if msg[-1] == "&":
                        receiving = False
                        msg = msg[:-1]
                if msg == "":
                    self.logUpdater.emit(
                        f"[{self.client.address}] {msg}", False)
                    self.connected = False
                else:
                    data = msg.split("!")
                    if len(data) > 1:
                        if data[-1] == "AUTH":
                            username, password = data[0].split(";")

                            worker = self.db.getWorkerByUsername(username)

                            if isinstance(worker, Worker) and \
                                    hashlib.sha3_512(password.encode()).hexdigest() == worker.password and \
                                    isinstance(worker.id_category, int):
                                self.client.socket.send(
                                    "ok!AUTH\n".encode(self.FORMAT))
                                self.start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                self.worker = worker
                                self.client.name = username
                                self.addClient.emit(self.client)
                            else:
                                self.client.socket.send(
                                    "no!AUTH\n".encode(self.FORMAT))
                        elif data[-1] == "MENUCATEGORY":
                            self.logUpdater.emit(
                                f"[{self.client.address}] {msg}", False)

                            self.client.socket.send(
                                (json.dumps(
                                    [x.__dict__ for x in self.db.getAllMenuCategories()])
                                 + "!MENUCATEGORY\n").encode(self.FORMAT))

                        elif data[-1] == "MENUITEM":
                            self.logUpdater.emit(
                                f"[{self.client.address}] {msg}", False)

                            self.client.socket.send(
                                (json.dumps(
                                    [x.toJson() for x in self.db.getAllMenusPhone()])
                                 + "!MENUITEM\n").encode(self.FORMAT))

                        elif data[-1] == "TABLES":
                            self.logUpdater.emit(
                                f"[{self.client.address}] {msg}", False)

                            self.client.socket.send(
                                (json.dumps(
                                    [x.__dict__ for x in self.db.getAllTables()])
                                 + "!TABLES\n").encode(self.FORMAT))

                        elif data[-1] == "TABLECONTENT":
                            self.logUpdater.emit(
                                f"[{self.client.address}] {msg}", False)

                            self.client.socket.send(
                                (json.dumps(
                                    [x.toJson() for x in self.db.getTableContent(int(data[0]))[0]])
                                 + "!TABLECONTENT\n").encode(self.FORMAT))

                        elif data[-1] == "ORDER":
                            self.logUpdater.emit(
                                f"[{self.client.address}] {msg}", False)
                            orders, sell_id, total, comment = data[0].split(
                                ";")
                            orders = self.constructOrder(json.loads(orders))
                            old = False
                            if sell_id == "":

                                sell_id = self.db.insertOrder(
                                    order_items=orders, total=total, id_worker=self.worker.id, id_customer=1, completed=0)

                            else:

                                sell = self.db.getSellById(int(sell_id))
                                sell.total = total
                                self.db.updateOrder(
                                    sell=sell, order_items=orders, completed=0)

                                old = True
                            self.printerCall.emit(
                                self.worker.name,
                                orders,
                                comment,
                                int(sell_id),
                                old,
                                0,
                                self)
                            self.client.socket.send(
                                ("ok!ORDER\n").encode(self.FORMAT))
                            self.tablesUpdated.emit()
                        elif data[-1] == "DISCONNECT":
                            self.client.socket.send(
                                "ok!DISCONNECT\n".encode(self.FORMAT))
                            self.end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            self.logUpdater.emit(
                                f"[{self.client.address}] {msg}", False)
                            self.connected = False
                    else:
                        self.logUpdater.emit(
                            f"[{self.client.address}] {msg}", False)
            except Exception as e:
                self.logUpdater.emit(f"[{self.client.address}] {e}", True)
                self.connected = False

        self.stop()

    def ring(self):
        self.client.socket.send(("!RING" + "\n").encode(self.FORMAT))
        self.logUpdater.emit(f"[{self.client.address}] Is ringing", False)

    def messageMe(self, message):
        self.client.socket.send(
            (message + "!MESSAGE" + "\n").encode(self.FORMAT))
        self.logUpdater.emit(f"[{self.client.address}] Message send", False)

    def messageRaw(self, message):
        self.client.socket.send(
            (message + "\n").encode(self.FORMAT))
        self.logUpdater.emit(f"[{self.client.address}] Message send", False)

    def constructOrder(self, data):
        current_order = []
        for orderItem in data:
            if orderItem["orderItemSupplements"] != []:
                orderItem["orderItemSupplements"] = [Supplement(
                    **x) for x in orderItem["orderItemSupplements"]]
            current_order.append(OrderItem(**orderItem))
        return current_order

    def notifyChange(self, signal):
        if signal == "MENUCATEGORY":

            self.client.socket.send(
                (json.dumps(
                    [x.__dict__ for x in self.db.getAllMenuCategories()])
                    + "!MENUCATEGORY\n").encode(self.FORMAT))

        elif signal == "MENUITEM":

            self.client.socket.send(
                (json.dumps(
                    [x.toJson() for x in self.db.getAllMenusPhone()])
                    + "!MENUITEM\n").encode(self.FORMAT))

        elif signal == "TABLES":

            self.client.socket.send(
                (json.dumps(
                    [x.__dict__ for x in self.db.getAllTables()])
                    + "!TABLES\n").encode(self.FORMAT))

    def stop(self):
        if self.worker is not None:
            if self.end_time == "":
                self.end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.db.insertPointer(
                Pointer(
                    date_start=self.start_time,
                    date_end=self.end_time,
                    id_worker=self.worker.id))
        self.connected = False
        self.removeClient.emit(self.client.address)
        self.signalFinish.emit(self)
        self.client.socket.close()
        self.logUpdater.emit(
            f"[SERVER] Server is not connected anymore to {self.client.address}", False)
        self.quit()


class PrinterThread(QThread):
    printStatus = pyqtSignal(list, list, QThread)
    logUpdater = pyqtSignal(str, bool)
    signalCallingThread = pyqtSignal(str, QThread)

    def __init__(
            self,
            which_printer: str,
            worker_name: str,
            order_items: list,
            comment: str,
            ticket_number: int,
            old: bool,
            tax: float,
            mobile: bool = False,
            given: float = 0.,
            calling_thread: QThread = None):

        super(PrinterThread, self).__init__()
        self.which_printer = which_printer
        self.worker_name = worker_name
        self.order_items = order_items
        self.comment = comment
        self.ticket_number = ticket_number
        self.old = old
        self.tax = tax
        self.mobile = mobile
        self.given = given
        self.ticket = None
        self.ticket_kitchen = None
        self.ticket_pizza = None
        self.ticket_bar = None
        self.kitchen_count = None
        self.pizza_count = None
        self.drink_count = None
        self.callingThread = calling_thread
        self.printer_setting = ServerSetting()
        self.printer_setting.load()

    def run(self):
        try:
            self.logUpdater.emit(
                f"[PRINTER THREAD] Start printing", False)

            if self.which_printer == "Kitchen":

                self.ticket_kitchen, self.ticket_pizza, self.ticket_bar, self.kitchen_count, self.pizza_count, self.drink_count = prepareTicketForOrder(
                    worker_name=self.worker_name,
                    order_items=self.order_items,
                    comment=self.comment,
                    ticket_number=self.ticket_number,
                    old=self.old)
                kitchen_tickets = []
                kitchen_places = []

                try:
                    if self.kitchen_count > 0:
                        kitchen = Network(self.printer_setting.KITCHEN_IP)

                        kitchen.text(self.ticket_kitchen)
                        kitchen.cut()

                        if self.pizza_count > 0:
                            kitchen.text(self.ticket_pizza)
                            kitchen.cut()
                except Exception as e:
                    self.logUpdater.emit(
                        f"[PRINTER THREAD] Kitchen ({self.printer_setting.KITCHEN_IP}) is down with error ({e})", True)
                    if self.kitchen_count > 0:
                        kitchen_tickets.append(self.ticket_kitchen)
                        kitchen_places.append("Kitchen")
                    if self.pizza_count > 0:
                        kitchen_tickets.append(self.ticket_pizza)
                        kitchen_places.append("Pizza")

                try:
                    if self.drink_count > 0:
                        bar = Network(self.printer_setting.BAR_IP)
                        bar.text(self.ticket_bar)
                        bar.cut()
                except Exception as e:
                    self.logUpdater.emit(
                        f"[PRINTER THREAD] Bar ({self.printer_setting.BAR_IP}) is down with error ({e})", True)
                    if self.drink_count > 0:
                        kitchen_tickets.append(self.ticket_bar)
                        kitchen_places.append("Bar")
                if len(kitchen_tickets) > 0:
                    self.signalCallingThread.emit(
                        f"{self.ticket_number}!PRINTER", self.callingThread)
                    self.printStatus.emit(
                        kitchen_tickets, kitchen_places, self)

            elif self.which_printer == "Cashier":

                self.ticket = prepareTicketForReceipt(
                    worker_name=self.worker_name,
                    order_items=self.order_items,
                    tax=self.tax,
                    comment=self.comment,
                    ticket_number=self.ticket_number)

                # Print the receipt
                try:
                    cashier = Network(self.printer_setting.CASHIER_IP)
                    cashier.image(os.path.join(
                        os.getcwd(), "resource", "patus_ticket_logo.jpg"))
                    cashier.text(self.ticket)
                    # cashier.qr("https://www.instagram.com/__patus_/")
                    # cashier.qr(
                    #     "https://www.facebook.com/PATUS-il-dio-della-pasta-106229107452308")
                    cashier.cut()
                except Exception as e:
                    self.logUpdater.emit(
                        f"[PRINTER THREAD] Cashier ({self.printer_setting.BAR_IP}) is down with error ({e})", True)
                    self.printStatus.emit([self.ticket], ["Cashier"], self)

            else:

                self.ticket = prepareTicketForCashier(
                    worker_name=self.worker_name,
                    order_items=self.order_items,
                    tax=self.tax,
                    comment=self.comment,
                    ticket_number=self.ticket_number,
                    given=self.given)

                # Print the Checker
                try:
                    cashier = Network(self.printer_setting.CASHIER_IP)
                    cashier.text(self.ticket)
                    cashier.cut()
                except Exception as e:
                    self.logUpdater.emit(
                        f"[PRINTER THREAD] Cashier ({self.printer_setting.BAR_IP}) is down with error ({e})", True)
                    self.printStatus.emit([self.ticket], ["Cashier"], self)

        except Exception as e:
            self.logUpdater.emit(
                f"[PRINTER THREAD] {e}", True)
        self.stop()

    def stop(self):
        self.logUpdater.emit(
            f"[PRINTER THREAD] Finished printing", False)
        self.quit()
