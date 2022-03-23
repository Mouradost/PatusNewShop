from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import datetime
import os
from DB.DBHandler import DBHelper
from DB.DbTables import *
from functools import partial
from Setting.Setting import ServerSetting
from escpos.printer import Network
import logging


class Pay(QDialog):
    def __init__(self, callLog, printerProblem, worker_name: str, order_items: list, tax: float, comment: str, ticket_number: int, total: float, printerThread):
        super(Pay, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), 'uis', 'pay.ui'), self)
        self.lcdN_total.setProperty("value", total)
        self.le_givenAmount.setValidator(QDoubleValidator())
        self.le_givenAmount.textChanged.connect(self.calculator)
        self.buttonBox.accepted.connect(self.validate_print)
        self.buttonBox.rejected.connect(self.reject)
        self.worker_name = worker_name
        self.order_items = order_items
        self.tax = tax
        self.comment = comment
        self.ticket_number = ticket_number
        self.printerProblem = printerProblem
        self.callLog = callLog
        self.printerThreadInstance = printerThread

        self.printer_setting = ServerSetting()
        self.printer_setting.load()

    def calculator(self):
        if self.buttonBox.signalsBlocked():
            self.buttonBox.blockSignals(False)
        try:
            total = float(self.le_givenAmount.text()) - self.lcdN_total.value()
            self.lcdN_return.setProperty("value", total)
        except Exception as e:
            logging.error(e)
            self.lcdN_return.setProperty("value", 0)

    def validate_print(self):
        try:
            given = float(self.le_givenAmount.text())
            try:
                if self.cb_printTicket.isChecked():
                    try:
                        self.printerThread = self.printerThreadInstance(
                            which_printer="",
                            worker_name=self.worker_name,
                            order_items=self.order_items,
                            comment=self.comment,
                            ticket_number=self.ticket_number,
                            old=False,
                            tax=self.tax,
                            mobile=True,
                            given=given)
                        self.printerThread.printStatus.connect(
                            self.printerProblem)
                        self.printerThread.logUpdater.connect(self.callLog)
                        self.printerThread.start()

                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setText('Sent to printer!')
                        msg.setWindowTitle("Information message")
                        msg.exec_()

                    except Exception as e:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText('Problem sending to printer!')
                        msg.setDetailedText(str(e))
                        msg.setWindowTitle("Warning message")
                        msg.exec_()

                self.accept()
            except Exception as e:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText('Printer problem')
                msg.setInformativeText(
                    "Check if the cashier printer is connected")
                msg.setDetailedText(str(e))
                msg.setWindowTitle("Warning message")
                msg.exec_()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Received money error')
            msg.setInformativeText("Received money should not be empty")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()
            # self.buttonBox.blockSignals(True)


class Reducer(QDialog):
    def __init__(self):
        super(Reducer, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), 'uis', 'reducer.ui'), self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.le_reduction.clear()
        self.le_reduction.setValidator(QDoubleValidator())


class Holder(QDialog):
    def __init__(self):
        super(Holder, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), 'uis', 'holder.ui'), self)
        self.buttonBox.accepted.connect(self.validate_click)
        self.buttonBox.rejected.connect(self.reject)
        self.tw_orderHold.clear()
        self.DB = DBHelper()
        self.holdingOrders = self.DB.getAllHoldingSells()
        ho_show = []
        for ho in self.holdingOrders:
            ho_show.append(
                HoldingSellShow(
                    Ticket_Number=ho.id,
                    Total=ho.total,
                    Date=ho.date
                ))
        displayDbData(self.tw_orderHold, ho_show)

    def validate_click(self):
        if self.tw_orderHold.currentRow() > -1:
            self.done(self.holdingOrders[self.tw_orderHold.currentRow()].id)
        else:
            self.buttonBox.blockSignals(True)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('No order to resume')
            msg.setInformativeText("Please select the order to resume")
            msg.setWindowTitle("Warning message")
            msg.exec_()


class SettingUI(QDialog):
    def __init__(self):
        super(SettingUI, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), 'uis', 'Setting.ui'), self)
        self.buttonBox.accepted.connect(self.validate_click)
        self.buttonBox.rejected.connect(self.reject)
        self.serverSetting = ServerSetting()
        self.serverSetting.load()
        self.le_ip.setText(self.serverSetting.IP)
        self.sb_port.setValue(self.serverSetting.PORT)
        self.sb_maxClients.setValue(self.serverSetting.MAX_CLIENTS)
        self.le_cashier_ip.setText(self.serverSetting.CASHIER_IP)
        self.le_kitchen_ip.setText(self.serverSetting.KITCHEN_IP)
        self.le_pizza_ip.setText(self.serverSetting.PIZZA_IP)
        self.le_bar_ip.setText(self.serverSetting.BAR_IP)

        self.le_ip.setValidator(QRegExpValidator(
            QRegExp("(\\b25[0-5]|\\b2[0-4][0-9]|\\b[01]?[0-9][0-9]?)(\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}")))
        self.le_cashier_ip.setValidator(QRegExpValidator(
            QRegExp("(\\b25[0-5]|\\b2[0-4][0-9]|\\b[01]?[0-9][0-9]?)(\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}")))
        self.le_kitchen_ip.setValidator(QRegExpValidator(
            QRegExp("(\\b25[0-5]|\\b2[0-4][0-9]|\\b[01]?[0-9][0-9]?)(\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}")))
        self.le_pizza_ip.setValidator(QRegExpValidator(
            QRegExp("(\\b25[0-5]|\\b2[0-4][0-9]|\\b[01]?[0-9][0-9]?)(\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}")))
        self.le_bar_ip.setValidator(QRegExpValidator(
            QRegExp("(\\b25[0-5]|\\b2[0-4][0-9]|\\b[01]?[0-9][0-9]?)(\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}")))

    def validate_click(self):
        if len(self.le_ip.text()) > 0:
            self.serverSetting.IP = self.le_ip.text()
            self.serverSetting.PORT = self.sb_port.value()
            self.serverSetting.MAX_CLIENTS = self.sb_maxClients.value()
            self.serverSetting.CASHIER_IP = self.le_cashier_ip.text()
            self.serverSetting.KITCHEN_IP = self.le_kitchen_ip.text()
            self.serverSetting.PIZZA_IP = self.le_pizza_ip.text()
            self.serverSetting.BAR_IP = self.le_bar_ip.text()
            self.serverSetting.save()
            self.done(1)
        else:
            self.buttonBox.blockSignals(True)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('No order to resume')
            msg.setInformativeText("Please select the order to resume")
            msg.setWindowTitle("Warning message")
            msg.exec_()


class PrinterProblem(QDialog):

    def __init__(self, tickets: list, places: list):
        super(PrinterProblem, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), 'uis', 'PrinterProblem.ui'), self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        for child in self.f_ticketProblem.findChildren(QFrame):
            child.deleteLater()
        for ticket, place in zip(tickets, places):
            self.f_ticketProblem.layout().addWidget(
                createTicketContainer(self.f_ticketProblem, ticket, place))


def createTicketContainer(parent, ticket, place):
    frame = QFrame(parent=parent)
    frame.setMinimumSize(430, 650)
    frame.setMaximumSize(440, 660)
    frame.setFrameShape(QFrame.StyledPanel)
    frame.setLineWidth(1)
    frame.setLayout(QVBoxLayout())

    # Place
    label = QLabel()
    label.setText(place)
    label.setScaledContents(True)
    label.setAlignment(Qt.AlignHCenter)
    frame.layout().addWidget(label)

    # Ticket
    text_edit = QPlainTextEdit()
    text_edit.insertPlainText(ticket)
    text_edit.setReadOnly(True)
    frame.layout().addWidget(text_edit)

    return frame


def displayDbData(table_widget: QTableWidget, data):
    table_widget.clear()
    table_widget.setRowCount(0)
    if len(data) > 0:
        simple = data[0].__dict__.keys()
        table_widget.insertColumn(len(simple))
        table_widget.setColumnCount(len(simple))
        table_widget.setHorizontalHeaderLabels(simple)
        for i, row in enumerate(data):
            table_widget.insertRow(i)
            for j, key in enumerate(row.__dict__):
                item = QTableWidgetItem(str(row.__dict__[key]))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                table_widget.setItem(i, j, item)
        table_widget.resizeRowsToContents()
        table_widget.resizeColumnsToContents()
    else:
        table_widget.insertColumn(0)
        table_widget.setColumnCount(0)


def createProductContainer(parent, db, product, table_id, fc):
    frame = QFrame(parent=parent)
    frame.setFrameShape(QFrame.StyledPanel)
    frame.setLineWidth(1)
    frame.setLayout(QVBoxLayout())
    frame.setMaximumSize(200, 300)
    # Picture or name
    label = QLabel()
    label.setPixmap(QPixmap(os.path.join(
        os.getcwd(), "resource", "patus_logo.jpg")))
    label.setScaledContents(True)
    label.setAlignment(Qt.AlignHCenter)
    label.setMaximumSize(200, 200)
    frame.layout().addWidget(label)
    label = QLabel()
    label.setText(product.name)
    label.setAlignment(Qt.AlignHCenter)
    frame.layout().addWidget(label)
    supp_list = []
    for sup in db.getSupplementByMenuId(product.id):
        check_box = QCheckBox(parent=frame, text=f"{sup.name}")
        check_box.setObjectName(f"cb_{product.id}_{sup.id}")
        frame.layout().addWidget(check_box)
        supp_list.append(check_box)
    # Add and Reduce
    btn_layout = QFrame(parent=frame)
    btn_layout.setLayout(QHBoxLayout())
    btn_layout.setMaximumSize(200, 200)
    add_button = QPushButton(parent=btn_layout, text="+")
    remove_button = QPushButton(parent=btn_layout, text="-")
    order_item = OrderItem(table_id, product.id, product.name,
                           product.category_id, 1, product.price, [])
    order_item_ = OrderItem(table_id, product.id,
                            product.name, product.category_id, -1, -product.price, [])
    add_button.clicked.connect(partial(fc, order_item, supp_list))
    remove_button.clicked.connect(partial(fc, order_item_, supp_list))
    btn_layout.layout().addWidget(add_button)
    btn_layout.layout().addWidget(remove_button)
    # buttons
    frame.layout().addWidget(btn_layout)
    return frame


def createClientDashBoardContainer(parent, client, fc_ring, fc_message):
    frame = QFrame(parent=parent)
    frame.setObjectName(f"f_{client.address}")
    frame.setFrameShape(QFrame.StyledPanel)
    frame.setLineWidth(1)
    frame.setLayout(QVBoxLayout())
    frame.setMaximumSize(250, 300)

    # Name
    label = QLabel()
    label.setText(client.name)
    label.setFont(QFont('Times', 20))
    label.setScaledContents(True)
    label.setAlignment(Qt.AlignHCenter)
    label.setMaximumSize(250, 50)
    frame.layout().addWidget(label)

    # Message
    text_edit = QLineEdit()
    text_edit.setPlaceholderText("Message")
    text_edit.setAlignment(Qt.AlignHCenter)
    # text_edit.setMaximumSize(250, 100)
    frame.layout().addWidget(text_edit)

    # Ring button
    btn_layout = QFrame(parent=frame)
    btn_layout.setLayout(QHBoxLayout())
    btn_layout.setMaximumSize(250, 50)
    ring_button = QPushButton(parent=btn_layout, text="Ring")
    ring_button.clicked.connect(partial(fc_ring, client))
    btn_layout.layout().addWidget(ring_button)
    message_button = QPushButton(parent=btn_layout, text="Send")
    message_button.clicked.connect(
        partial(fc_message, client, text_edit))
    # message_button.clicked.connect(text_edit.clear)
    btn_layout.layout().addWidget(message_button)
    # buttons
    frame.layout().addWidget(btn_layout)
    return frame


def prepareTicketForReceipt(worker_name: str, order_items: list, tax: float, comment: str, ticket_number: int):
    total = 0
    ticket_txt = ""
    ticket_txt += '=' * 46 + ' \n'
    ticket_txt += f'Ticket Number : {ticket_number:>30}\n'
    ticket_txt += f'Worker Name : {worker_name:>32}\n'
    ticket_txt += f'Date and time : {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):>30}\n'
    ticket_txt += '-' * 46 + ' \n'
    if order_items[0].tableId is not None:
        ticket_txt += f'Table {order_items[0].tableId:>30}\n'
    else:
        ticket_txt += 'Take away \n'
    ticket_txt += '-' * 46 + ' \n'
    ticket_txt += f"{'ITEM':<20}{'QUANTITY':^13}{'PRICE':^13}\n"
    ticket_txt += '-' * 46 + ' \n'
    for order_item in order_items:
        total += order_item.orderItemTotal
        ticket_txt += f"{order_item.productName:<20}{order_item.orderItemQuantity:^13}{round(order_item.orderItemTotal, 2):^13}\n"
        for supp in order_item.orderItemSupplements:
            ticket_txt += f"+ {supp.name:<31}{round(order_item.orderItemQuantity * supp.price, 2):^13}\n"
            total += order_item.orderItemQuantity * supp.price
    if len(comment) > 0:
        ticket_txt += '-' * 46 + ' \n'
        ticket_txt += comment + ' \n'
    ticket_txt += '-' * 46 + ' \n'
    ticket_txt += f"{'TOTAL':<33}{round(total, 2):^13}\n"
    ticket_txt += f"{'REDUCTION':<33}{round(tax, 2):^13}\n"
    ticket_txt += f"{'TOTAL TO PAY':<33}{round(total - tax, 2):^13}\n"
    ticket_txt += '=' * 46 + ' \n'
    return ticket_txt


def prepareTicketForCashier(worker_name: str, order_items: list, tax: float, comment: str, ticket_number: int, given: float):
    total = 0
    ticket_txt = ""
    ticket_txt += '=' * 46 + ' \n'
    ticket_txt += f'Ticket Number : {ticket_number:>30}\n'
    ticket_txt += f'Worker Name : {worker_name:>32}\n'
    ticket_txt += f'Date and time : {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):>30}\n'
    ticket_txt += '-' * 46 + ' \n'
    if order_items[0].tableId is not None:
        ticket_txt += f'Table {order_items[0].tableId:>30}\n'
    else:
        ticket_txt += 'Take away \n'
    ticket_txt += '-' * 46 + ' \n'
    ticket_txt += f"{'ITEM':<20}{'QUANTITY':^13}{'PRICE':^13}\n"
    ticket_txt += '-' * 46 + ' \n'
    for order_item in order_items:
        total += order_item.orderItemTotal
        ticket_txt += f"{order_item.productName:<20}{order_item.orderItemQuantity:^13}{round(order_item.orderItemTotal, 2):^13}\n"
        for supp in order_item.orderItemSupplements:
            ticket_txt += f"+ {supp.name:<31}{round(order_item.orderItemQuantity * supp.price, 2):^13}\n"
            total += order_item.orderItemQuantity * supp.price
    if len(comment) > 0:
        ticket_txt += '-' * 46 + ' \n'
        ticket_txt += comment + ' \n'
    ticket_txt += '-' * 46 + ' \n'
    ticket_txt += f"{'TOTAL':<33}{round(total, 2):^13}\n"
    ticket_txt += f"{'REDUCTION':<33}{round(tax, 2):^13}\n"
    ticket_txt += f"{'TOTAL TO PAY':<33}{round(total - tax, 2):^13}\n"
    ticket_txt += '=' * 46 + ' \n'
    ticket_txt += f"{'RECEIVED':<33}{given:^13}\n"
    ticket_txt += f"{'RETURNED':<33}{round(given - total, 2):^13}\n"
    ticket_txt += '=' * 46 + ' \n'
    ticket_txt += f"{'PATUS vous remercie pour votre visite':^46}\n"
    ticket_txt += '=' * 46 + ' \n'

    return ticket_txt


def prepareTicketForOrder(worker_name: str, order_items: list, comment: str, ticket_number: int, old: bool):
    db = DBHelper()
    kitchen_count, pizza_count, drink_count = 0, 0, 0

    ticket_kitchen_txt = ""
    ticket_pizza_txt = ""
    ticket_bar_txt = ""

    now = datetime.datetime.now()
    if old:
        ticket_kitchen_txt += '=' * 46 + ' \n'
        ticket_kitchen_txt += f"{'UPDATE':^46}" + ' \n'

        ticket_pizza_txt += '=' * 46 + ' \n'
        ticket_pizza_txt += f"{'UPDATE':^46}" + ' \n'

        ticket_bar_txt += '=' * 46 + ' \n'
        ticket_bar_txt += f"{'UPDATE':^46}" + ' \n'

    # chef
    ticket_kitchen_txt += '=' * 46 + ' \n'
    ticket_kitchen_txt += f'Ticket Number : {ticket_number:>30}\n'
    ticket_kitchen_txt += f'Worker Name : {worker_name:>32}\n'
    ticket_kitchen_txt += f'Date and time : {now.strftime("%Y-%m-%d %H:%M:%S"):>30}\n'
    ticket_kitchen_txt += '-' * 46 + ' \n'
    if order_items[0].tableId is not None:
        ticket_kitchen_txt += f'Table {order_items[0].tableId:>40}\n'
    else:
        ticket_kitchen_txt += 'Take away \n'

    # pizza yolo
    ticket_pizza_txt += '=' * 46 + ' \n'
    ticket_pizza_txt += f'Ticket Number : {ticket_number:>30}\n'
    ticket_pizza_txt += f'Worker Name : {worker_name:>32}\n'
    ticket_pizza_txt += f'Date and time : {now.strftime("%Y-%m-%d %H:%M:%S"):>30}\n'
    ticket_pizza_txt += '-' * 46 + ' \n'
    if order_items[0].tableId is not None:
        ticket_pizza_txt += f'Table {order_items[0].tableId:>40}\n'
    else:
        ticket_pizza_txt += 'Take away \n'

    # bar
    ticket_bar_txt += '=' * 46 + ' \n'
    ticket_bar_txt += f'Ticket Number : {ticket_number:>30}\n'
    ticket_bar_txt += f'Worker Name : {worker_name:>32}\n'
    ticket_bar_txt += f'Date and time : {now.strftime("%Y-%m-%d %H:%M:%S"):>30}\n'
    ticket_bar_txt += '-' * 46 + ' \n'
    if order_items[0].tableId is not None:
        ticket_bar_txt += f'Table {order_items[0].tableId:>40}\n'
    else:
        ticket_bar_txt += 'Take away \n'

    # chef
    ticket_kitchen_txt += '-' * 46 + ' \n'
    ticket_kitchen_txt += f"{'ITEM':<23}{'QUANTITY':^23}\n"
    ticket_kitchen_txt += '-' * 46 + ' \n'

    # pizza yolo
    ticket_pizza_txt += '-' * 46 + ' \n'
    ticket_pizza_txt += f"{'ITEM':<23}{'QUANTITY':^23}\n"
    ticket_pizza_txt += '-' * 46 + ' \n'

    # bar
    ticket_bar_txt += '-' * 46 + ' \n'
    ticket_bar_txt += f"{'ITEM':<23}{'QUANTITY':^23}\n"
    ticket_bar_txt += '-' * 46 + ' \n'

    for order_item in order_items:
        if db.getMenuCategoryById(order_item.productCategory).printing_place == 2:
            ticket_bar_txt += f"{order_item.productName:<23} {order_item.orderItemQuantity:^23}\n"
            for supp in order_item.orderItemSupplements:
                ticket_bar_txt += f"+ {supp.name:<23}\n"
            drink_count += 1
        else:
            ticket_kitchen_txt += f"{order_item.productName:<23} {order_item.orderItemQuantity:^23}\n"
            kitchen_count += 1
            for supp in order_item.orderItemSupplements:
                ticket_kitchen_txt += f"+ {supp.name:<23}\n"
            if db.getMenuCategoryById(order_item.productCategory).printing_place == 1:
                ticket_pizza_txt += f"{order_item.productName:<23} {order_item.orderItemQuantity:^23}\n"
                for supp in order_item.orderItemSupplements:
                    ticket_pizza_txt += f"+ {supp.name:<23}\n"
                pizza_count += 1
    if len(comment) > 0:
        ticket_kitchen_txt += '-' * 46 + ' \n'
        ticket_pizza_txt += '-' * 46 + ' \n'
        ticket_bar_txt += '-' * 46 + ' \n'

        ticket_kitchen_txt += comment + ' \n'
        ticket_pizza_txt += comment + ' \n'
        ticket_bar_txt += comment + ' \n'

    ticket_kitchen_txt += '=' * 46 + ' \n'
    ticket_pizza_txt += '=' * 46 + ' \n'
    ticket_bar_txt += '=' * 46 + ' \n'

    return ticket_kitchen_txt, ticket_pizza_txt, ticket_bar_txt, kitchen_count, pizza_count, drink_count
