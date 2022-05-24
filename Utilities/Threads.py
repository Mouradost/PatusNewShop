from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from DB.DBHandler import DBHelper
from Setting.Setting import ServerSetting
from Utilities.UiUtilities import (
    prepareTicketForOrder,
    prepareTicketForCashier,
    prepareTicketForReceipt,
    getTicketDifference,
    handlePrint,
)
from DB.DbTables import *
import datetime
import hashlib
import socket
import json
from typing import List
import logging


class InfoThread(QtCore.QThread):
    UpdateInfo = pyqtSignal(int, int, int, int)
    logUpdater = pyqtSignal(str, bool)
    UpdateTables = pyqtSignal()

    def __init__(self, parent=None):
        super(InfoThread, self).__init__(parent)
        self.DB = DBHelper()
        self.active = True

    def run(self):
        self.logUpdater.emit(f"[INFO THREAD] Started", False)
        try:
            while self.active:
                self.logUpdater.emit(f"[INFO THREAD] Updating", False)
                (
                    nb_free_tables,
                    nb_busy_tables,
                    nb_month_sells,
                    nb_day_sells,
                ) = self.DB.getHomeScreenInfo(
                    datetime.datetime.now().strftime("%Y-%m"),
                    datetime.datetime.now().strftime("%Y-%m-%d"),
                )
                self.UpdateInfo.emit(
                    nb_free_tables[0],
                    nb_busy_tables[0],
                    nb_month_sells[0],
                    nb_day_sells[0],
                )
                # Check for any reservation in 1h range
                self.check_tables()
                # sleep for a minute
                self.sleep(60)
        except Exception as e:
            self.logUpdater.emit(f"[INFO THREAD ERROR] {e}", True)
            self.active = False
            self.terminate()

    def check_tables(self):
        # Active reservation
        reservations = self.DB.getReservationByDateRange(
            start_date=(
                datetime.datetime.now() - datetime.timedelta(minutes=30)
            ).strftime("%Y-%m-%d %H:%M"),
            end_date=(
                datetime.datetime.now() + datetime.timedelta(minutes=30)
            ).strftime("%Y-%m-%d %H:%M"),
        )
        count = 0
        active_reserved_tables = []
        for reservation in reservations:
            table = self.DB.getTableById(reservation.table_id)
            active_reserved_tables.append(table.id)
            if table.reserved == 0:
                table.reserved = 1
                count += 1
                self.DB.updateTable(table)
        # Outdated reservation
        tables = self.DB.getReservedTables()
        for table in tables:
            if table.id not in active_reserved_tables and table.reserved == 1:
                count += 1
                table.reserved = 0
                self.DB.updateTable(table)
        if count > 0:
            self.UpdateTables.emit()

    def stop(self):
        self.logUpdater.emit(f"[INFO THREAD] Stopped", False)
        self.active = False
        self.exit()


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
    printerCall = pyqtSignal(str, list, str, int, bool, float, int)
    notificationCall = pyqtSignal(str)
    SIZE = 1024
    FORMAT = "utf-8"

    def __init__(self):
        super(ServerThread, self).__init__()
        self.SETTINGS = ServerSetting()
        self.socket = None
        self.count = 0
        self.active = False
        self.clients = []

    def run(self):
        try:
            self.bindServer()
            self.logUpdater.emit("[SERVER] Server is configured", False)
            self.active = True
            self.socket.listen(self.SETTINGS.MAX_CLIENTS)
            self.logUpdater.emit(
                f"[SERVER] Server is listening on {self.SETTINGS.IP}:{self.SETTINGS.PORT}",
                False,
            )
            while self.active:
                client_socket, client_address = self.socket.accept()
                client_socket.settimeout(2000)
                clientHandler = ClientHandler(
                    client=Client(socket=client_socket, address=client_address[0]),
                    addClient=self.addClient,
                    logUpdater=self.logUpdater,
                    removeClient=self.removeClient,
                    tablesUpdated=self.tablesUpdated,
                    printerCall=self.printerCall,
                )
                clientHandler.signalFinish.connect(self.removeClientHandler)
                clientHandler.signalKitchen.connect(self.sendToKitchen)
                clientHandler.signalFromKitchen.connect(self.notifyTheClient)
                self.clients.append(clientHandler)
                clientHandler.start()
                self.logUpdater.emit(
                    f"[SERVER] Active connection: {len(self.clients)}", False
                )
        except Exception as e:
            self.logUpdater.emit(f"[SERVER] {e}", True)
            self.stop()

    def bindServer(self):
        try:
            self.SETTINGS.load()
            self.logUpdater.emit(f"[SERVER] Load setting: {self.SETTINGS}", False)
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.bind((self.SETTINGS.IP, self.SETTINGS.PORT))
            self.updateServerStatus.emit(
                f"Server started on {self.SETTINGS.IP}:{self.SETTINGS.PORT}"
            )
        except Exception as e:

            self.logUpdater.emit(f"[SERVER] {e}", True)
            self.sleep(10)
            self.SETTINGS = ServerSetting()
            self.logUpdater.emit(
                f"[SERVER] Trying default setting \n {self.SETTINGS}", False
            )
            # self.bindServer() Need to implement a reconnect method

    def removeClientHandler(self, clientHandler):
        try:
            self.clients.remove(clientHandler)
            self.logUpdater.emit(
                f"[SERVER] Client list size: {len(self.clients)}", False
            )
        except Exception as e:
            self.logUpdater.emit(f"[SERVER ERROR] Client removed error: {e}", True)

    def ringClient(self, client):
        for clientHandler in self.clients:
            if clientHandler.client == client:
                clientHandler.ring()

    def messageClient(self, client: Client, msg: str):
        for clientHandler in self.clients:
            if clientHandler.client == client:
                clientHandler.messageMe(msg)

    def notifyClients(self, signal):
        for clientHandler in self.clients:
            clientHandler.notifyChange(signal)

    def notifyClient(self, signal, worker_id):
        for clientHandler in self.clients:
            if isinstance(clientHandler.worker, Worker):
                if clientHandler.worker.id == worker_id:
                    clientHandler.messageRaw(signal)

    def notifyCompletionOrder(self) -> None:
        for clientHandler in self.clients:
            clientHandler.sendUncompleteOrders()

    @pyqtSlot(Ticket)
    def sendToKitchen(self, ticket: Ticket) -> None:
        for client in self.clients:
            client.sendNewOrder(ticket)

    @pyqtSlot(Ticket)
    def notifyTheClient(self, ticket: Ticket) -> None:
        if ticket.table_id is not None:
            self.notificationCall.emit(
                f"Ticket {ticket.id} Table {ticket.table_id} ready"
            )
        else:
            self.notificationCall.emit(f"Ticket {ticket.id} Take away ready")
        for client in self.clients:
            client.sendOrderUpdate(ticket)

    def restart(self) -> None:
        for client in self.clients:
            client.stop()
        self.socket.close()
        self.bindServer()

    def stop(self):
        self.socket.close()
        for client in self.clients:
            client.sendDisconnect("Server down")
            client.wait()
        self.logUpdater.emit("[SERVER] Server is stopped", False)
        self.updateServerStatus.emit(f"Server closed")
        self.active = False
        self.exit()


class ClientHandler(QThread):
    SIZE = 1024
    FORMAT = "utf-8"
    signalFinish = pyqtSignal(QThread)
    signalKitchen = pyqtSignal(Ticket)
    signalFromKitchen = pyqtSignal(Ticket)

    def __init__(
        self, client, addClient, logUpdater, removeClient, tablesUpdated, printerCall
    ):
        super(ClientHandler, self).__init__()
        self.SETTINGS = ServerSetting()
        self.client = client
        self.addClient = addClient
        self.logUpdater = logUpdater
        self.removeClient = removeClient
        self.tablesUpdated = tablesUpdated
        self.printerCall = printerCall
        self.start_time = ""
        self.end_time = ""
        self.is_kitchen = False

        self.connected = True
        self.worker = None
        self.logUpdater.emit(
            f"[SERVER] New connection: Connected to {self.client.address}", False
        )
        self.db = DBHelper()

    def run(self):
        while self.connected:
            try:
                msg = ""
                receiving = True
                while receiving and self.connected:
                    msg += self.client.socket.recv(self.SIZE).decode(self.FORMAT)
                    if msg[-1] == "&":
                        receiving = False
                        msg = msg[:-1]
                self.logUpdater.emit(f"[{self.client.address}] {msg}", False)
                if msg == "":
                    self.logUpdater.emit(f"[{self.client.address}] {msg}", False)
                    self.connected = False
                else:
                    data = msg.split("!")
                    if len(data) > 1:
                        if data[-1] == "AUTH":
                            self.authenticate(data)
                        else:
                            if self.is_kitchen:
                                self.kitchen_handler(data=data, msg=msg)
                            else:
                                self.serving_handler(data=data, msg=msg)
                    else:
                        self.logUpdater.emit(f"[{self.client.address}] {msg}", False)
            except Exception as e:
                self.logUpdater.emit(f"[{self.client.address}] {e}", True)
                self.connected = False

        self.stop()

    def ring(self):
        self.client.socket.send(("!RING" + "\n").encode(self.FORMAT))
        self.logUpdater.emit(f"[{self.client.address}] Is ringing", False)

    def messageMe(self, message):
        self.client.socket.send((message + "!MESSAGE" + "\n").encode(self.FORMAT))
        self.logUpdater.emit(f"[{self.client.address}] Message send", False)

    def messageRaw(self, message):
        self.client.socket.send((message + "\n").encode(self.FORMAT))
        self.logUpdater.emit(f"[{self.client.address}] Message send", False)

    def constructOrder(self, data) -> List[OrderItem]:
        current_order = []
        for orderItem in data:
            if orderItem["orderItemSupplements"] != []:
                orderItem["orderItemSupplements"] = [
                    Supplement(**x) for x in orderItem["orderItemSupplements"]
                ]
            current_order.append(OrderItem(**orderItem))
        return current_order

    def constructTicket(self, data) -> Ticket:
        data["orders"] = self.constructOrder(data["orders"])
        return Ticket(**data)

    def notifyChange(self, signal):
        if signal == "MENUCATEGORY":

            self.client.socket.send(
                (
                    json.dumps([x.__dict__ for x in self.db.getAllMenuCategories()])
                    + "!MENUCATEGORY\n"
                ).encode(self.FORMAT)
            )

        elif signal == "MENUITEM":

            self.client.socket.send(
                (
                    json.dumps([x.toJson() for x in self.db.getAllMenusPhone()])
                    + "!MENUITEM\n"
                ).encode(self.FORMAT)
            )

        elif signal == "TABLES":

            self.client.socket.send(
                (
                    json.dumps([x.__dict__ for x in self.db.getAllTables()])
                    + "!TABLES\n"
                ).encode(self.FORMAT)
            )

    def authenticate(self, data: List[str]) -> None:
        username, password = data[0].split(";")
        if username == "Kitchen" and password == "|---Mouradost---|":
            self.is_kitchen = True
            self.client.socket.send("ok!AUTH\n".encode(self.FORMAT))
            self.client.name = username
            self.addClient.emit(self.client)
            return
        else:
            self.is_kitchen = False

        worker = self.db.getWorkerByUsername(username)
        if (
            isinstance(worker, Worker)
            and hashlib.sha3_512(password.encode()).hexdigest() == worker.password
            and isinstance(worker.id_category, int)
        ):
            self.client.socket.send("ok!AUTH\n".encode(self.FORMAT))
            self.start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.worker = worker
            self.client.name = username
            self.addClient.emit(self.client)
        else:
            self.client.socket.send("no!AUTH\n".encode(self.FORMAT))

    def serving_handler(self, data: List[str], msg: str) -> None:
        if data[-1] == "MENUCATEGORY":
            self.logUpdater.emit(f"[{self.client.address}] {msg}", False)

            self.client.socket.send(
                (
                    json.dumps([x.__dict__ for x in self.db.getAllMenuCategories()])
                    + "!MENUCATEGORY\n"
                ).encode(self.FORMAT)
            )

        elif data[-1] == "MENUITEM":
            self.logUpdater.emit(f"[{self.client.address}] {msg}", False)
            self.client.socket.send(
                (
                    json.dumps([x.toJson() for x in self.db.getAllMenusPhone()])
                    + "!MENUITEM\n"
                ).encode(self.FORMAT)
            )

        elif data[-1] == "TABLES":
            self.logUpdater.emit(f"[{self.client.address}] {msg}", False)

            self.client.socket.send(
                (
                    json.dumps([x.__dict__ for x in self.db.getAllTables()])
                    + "!TABLES\n"
                ).encode(self.FORMAT)
            )

        elif data[-1] == "TABLECONTENT":
            self.logUpdater.emit(f"[{self.client.address}] {msg}", False)
            results, _, result_sell = self.db.getTableContent(int(data[0]))
            if result_sell is not None:
                if result_sell.id_worker == self.worker.id:
                    msg_to_send = (
                        json.dumps([x.toJson() for x in results]) + "!TABLECONTENT\n"
                    )
                else:
                    msg_to_send = "NO!TABLECONTENT\n"
            else:
                msg_to_send = "[]!TABLECONTENT\n"
            self.client.socket.send((msg_to_send).encode(self.FORMAT))
        elif data[-1] == "TABLEOWNERSHIP":
            self.logUpdater.emit(f"[{self.client.address}] {msg}", False)

            self.client.socket.send(
                (
                    json.dumps([x.toJson() for x in self.db.getAllTableOwnership()])
                    + "!TABLEOWNERSHIP\n"
                ).encode(self.FORMAT)
            )

        elif data[-1] == "ORDER":
            self.logUpdater.emit(f"[{self.client.address}] {msg}", False)
            orders, sell_id, total, comment, nb_covers = data[0].split(";")
            orders = self.constructOrder(json.loads(orders))
            order_show = orders
            old = False
            if sell_id == "":
                sell_id = self.db.insertOrder(
                    order_items=orders,
                    total=total,
                    id_worker=self.worker.id,
                    id_customer=1,
                    completed=0,
                    nb_covers=nb_covers,
                    on_table=True,
                )

            else:

                sell = self.db.getSellById(int(sell_id))
                sell.total = total
                old_order = self.db.updateOrder(
                    sell=sell, order_items=orders, completed=0
                )
                order_show = getTicketDifference(old_order, orders)

                old = True
            self.printerCall.emit(
                self.worker.name,
                order_show,
                comment,
                int(sell_id),
                old,
                0,
                self.worker.id,
            )
            self.client.socket.send(("ok!ORDER\n").encode(self.FORMAT))

            self.signalKitchen.emit(
                Ticket(
                    id=sell_id,
                    table_id=orders[0].tableId,
                    worker_id=self.worker.id,
                    worker_name=self.worker.name,
                    orders=orders,
                )
            )
            self.tablesUpdated.emit()
        elif data[-1] == "DISCONNECT":
            self.sendDisconnect(msg)

    def kitchen_handler(self, data: List[str], msg: str) -> None:
        if data[-1] == "TICKETUPDDATED":
            ticket = self.constructTicket(json.loads(data[0]))
            self.signalFromKitchen.emit(ticket)
            self.db.updateTicket(ticket)
        elif data[-1] == "UNCOMPLETEDORDERS":
            self.sendUncompleteOrders()
        elif data[-1] == "DISCONNECT":
            self.sendDisconnect(msg)

    def sendNewOrder(self, ticket: Ticket) -> None:
        self.client.socket.send(
            (json.dumps(ticket.toJson()) + "!NEWUNCOMPLETEDORDER" + "\n").encode(
                self.FORMAT
            )
        )
        self.logUpdater.emit(
            f"[{self.client.address}] New order send to kitchen", False
        )

    def sendOrderUpdate(self, ticket: Ticket) -> None:
        if self.worker is not None:
            if self.worker.id == ticket.worker_id:
                if ticket.table_id is not None:
                    self.client.socket.send(
                        (
                            f"Ticket {ticket.id} Table {ticket.table_id} ready!MESSAGE"
                            + "\n"
                        ).encode(self.FORMAT)
                    )
                else:
                    self.client.socket.send(
                        (f"Ticket {ticket.id} Take away ready!MESSAGE" + "\n").encode(
                            self.FORMAT
                        )
                    )

    def sendUncompleteOrders(self) -> None:
        tickets_json = json.dumps([x.toJson() for x in self.db.getUncompletedTickets()])
        if tickets_json is not None:
            self.client.socket.send(
                (tickets_json + "!UNCOMPLETEDORDERS\n").encode(self.FORMAT)
            )
        else:
            self.client.socket.send(("!UNCOMPLETEDORDERS\n").encode(self.FORMAT))

    def sendDisconnect(self, msg) -> None:
        self.client.socket.send("ok!DISCONNECT\n".encode(self.FORMAT))
        self.end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.logUpdater.emit(f"[{self.client.address}] {msg}", False)
        self.connected = False

    def stop(self):
        try:
            if self.connected:
                self.client.socket.send(("!DISCONNECT\n").encode(self.FORMAT))
            if self.worker is not None:
                if self.end_time == "":
                    self.end_time = datetime.datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                self.db.insertPointer(
                    Pointer(
                        date_start=self.start_time,
                        date_end=self.end_time,
                        id_worker=self.worker.id,
                    )
                )
            self.removeClient.emit(self.client.address)
            self.signalFinish.emit(self)
            self.logUpdater.emit(
                f"[SERVER] Server is not connected anymore to {self.client.address}",
                False,
            )

            self.client.socket.close()
            self.connected = False
            self.exit()
        except Exception as e:
            self.logUpdater.emit(f"[{self.client.address} ERROR] {e} ", True)


class PrinterThread(QThread):
    printStatus = pyqtSignal(list, list, QThread)
    logUpdater = pyqtSignal(str, bool)
    signalCallingThread = pyqtSignal(str, int)

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
        given: float = 0.0,
        calling_thread: QThread = None,
        cancel: bool = False,
        errors_dictionary: dict = None,
    ):

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
        self.cancel = cancel
        self.errors_dictionary = errors_dictionary
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
        self.db = DBHelper()

    def run(self):
        if self.errors_dictionary is None:
            try:
                self.logUpdater.emit(f"[PRINTER THREAD] Start printing", False)

                if self.which_printer == "Kitchen":
                    (
                        self.ticket_kitchen,
                        self.ticket_pizza,
                        self.ticket_bar,
                        self.kitchen_count,
                        self.pizza_count,
                        self.drink_count,
                    ) = prepareTicketForOrder(
                        worker_name=self.worker_name,
                        order_items=self.order_items,
                        comment=self.comment,
                        ticket_number=self.ticket_number,
                        old=self.old,
                        cancel=self.cancel,
                    )
                    kitchen_tickets = []
                    kitchen_places = []

                    try:
                        if self.kitchen_count > 0:
                            handlePrint(
                                ip_address=self.printer_setting.KITCHEN_IP,
                                text=self.ticket_kitchen,
                                show_logo=False,
                                show_qr_code=False,
                                height=2,
                            )
                    except Exception as e:
                        self.logUpdater.emit(
                            f"[PRINTER THREAD] Kitchen ({self.printer_setting.KITCHEN_IP}) is down with error ({e})",
                            True,
                        )
                        if self.kitchen_count > 0:
                            kitchen_tickets.append(self.ticket_kitchen)
                            kitchen_places.append("Kitchen")
                        # if self.pizza_count > 0:
                        #     kitchen_tickets.append(self.ticket_pizza)
                        #     kitchen_places.append("Pizza")

                    try:
                        if self.drink_count > 0:
                            handlePrint(
                                ip_address=self.printer_setting.BAR_IP,
                                text=self.ticket_bar,
                                show_logo=False,
                                show_qr_code=False,
                                height=2,
                            )
                    except Exception as e:
                        self.logUpdater.emit(
                            f"[PRINTER THREAD] Bar ({self.printer_setting.BAR_IP}) is down with error ({e})",
                            True,
                        )
                        if self.drink_count > 0:
                            kitchen_tickets.append(self.ticket_bar)
                            kitchen_places.append("Bar")
                    if len(kitchen_tickets) > 0:
                        self.signalCallingThread.emit(
                            f"{self.ticket_number}!PRINTER", self.callingThread
                        )
                        self.printStatus.emit(kitchen_tickets, kitchen_places, self)

                elif self.which_printer == "Receipt":

                    self.ticket = prepareTicketForReceipt(
                        worker_name=self.worker_name,
                        order_items=self.order_items,
                        tax=self.tax,
                        comment=self.comment,
                        ticket_number=self.ticket_number,
                    )

                    # Print the receipt
                    try:
                        handlePrint(
                            ip_address=self.printer_setting.CASHIER_IP,
                            text=self.ticket,
                            show_logo=True,
                            show_qr_code=False,
                        )
                    except Exception as e:
                        self.logUpdater.emit(
                            f"[PRINTER THREAD] Cashier ({self.printer_setting.CASHIER_IP}) is down with error ({e})",
                            True,
                        )
                        self.printStatus.emit([self.ticket], ["Receipt"], self)

                else:

                    self.ticket = prepareTicketForCashier(
                        worker_name=self.worker_name,
                        order_items=self.order_items,
                        tax=self.tax,
                        comment=self.comment,
                        ticket_number=self.ticket_number,
                        given=self.given,
                    )

                    # Print the Checker
                    try:
                        handlePrint(
                            ip_address=self.printer_setting.CASHIER_IP,
                            text=self.ticket,
                            show_logo=True,
                            show_qr_code=False,
                            cash_drawer=True,
                            pin=self.printer_setting.DRAWER_PIN,
                        )
                    except Exception as e:
                        self.logUpdater.emit(
                            f"[PRINTER THREAD] Cashier ({self.printer_setting.CASHIER_IP}) is down with error ({e})",
                            True,
                        )
                        self.printStatus.emit([self.ticket], ["Cashier"], self)

            except Exception as e:
                self.logUpdater.emit(f"[PRINTER THREAD] {e}", True)
            self.stop()
        else:
            self.handleError()

    def handleError(self):
        try:
            remaining_places = []
            for place in self.errors_dictionary:
                if place == "Kitchen":
                    try:
                        if self.kitchen_count > 0:
                            handlePrint(
                                ip_address=self.printer_setting.KITCHEN_IP,
                                text=self.errors_dictionary[place],
                                show_logo=False,
                                show_qr_code=False,
                                height=2,
                            )
                    except Exception as e:
                        self.logUpdater.emit(
                            f"[PRINTER THREAD] Kitchen ({self.printer_setting.KITCHEN_IP}) is down with error ({e})",
                            True,
                        )
                        remaining_places += "Kitchen"
                elif place == "Bar":
                    try:
                        if self.drink_count > 0:
                            handlePrint(
                                ip_address=self.printer_setting.BAR_IP,
                                text=self.errors_dictionary[place],
                                show_logo=False,
                                show_qr_code=False,
                                height=2,
                            )
                    except Exception as e:
                        self.logUpdater.emit(
                            f"[PRINTER THREAD] Bar ({self.printer_setting.BAR_IP}) is down with error ({e})",
                            True,
                        )
                        remaining_places += "Bar"
                elif place == "Cashier":
                    try:
                        handlePrint(
                            ip_address=self.printer_setting.CASHIER_IP,
                            text=self.errors_dictionary[place],
                            show_logo=True,
                            show_qr_code=False,
                            cash_drawer=True,
                            pin=self.printer_setting.DRAWER_PIN,
                        )
                    except Exception as e:
                        self.logUpdater.emit(
                            f"[PRINTER THREAD] Cashier ({self.printer_setting.CASHIER_IP}) is down with error ({e})",
                            True,
                        )
                        remaining_places += "Cashier"
                else:
                    try:
                        handlePrint(
                            ip_address=self.printer_setting.CASHIER_IP,
                            text=self.errors_dictionary[place],
                            show_logo=True,
                            show_qr_code=False,
                        )
                    except Exception as e:
                        self.logUpdater.emit(
                            f"[PRINTER THREAD] Cashier ({self.printer_setting.CASHIER_IP}) is down with error ({e})",
                            True,
                        )
                        remaining_places += "Receipt"
            if len(remaining_places) > 0:
                self.printStatus.emit(
                    [self.errors_dictionary[p] for p in remaining_places],
                    [p for p in remaining_places],
                    self,
                )

        except Exception as e:
            self.logUpdater.emit(f"[PRINTER THREAD HANDLE ERROR] {e}", True)
        self.stop()

    def stop(self):
        self.logUpdater.emit(f"[PRINTER THREAD] Finished printing", False)
        self.exit()
