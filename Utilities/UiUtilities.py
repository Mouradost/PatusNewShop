from typing import List, Union
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
from Utilities import LicenseChecker
import logging
from escpos.printer import Network
from Utilities.Utility import openConvertFile


def handlePrint(
    ip_address: str,
    text: str,
    show_logo: bool = False,
    show_qr_code: bool = False,
    height: int = 1,
    cash_drawer: bool = False,
    pin: int = 2,
) -> None:
    printer = Network(ip_address)
    printer.set(
        align="center",
        font="a",
        text_type="normal",
        width=1,
        height=height,
        density=9,
        invert=False,
        smooth=False,
        flip=False,
    )
    printer.charcode("MULTILINGUAL")
    if show_logo:
        printer.image(os.path.join(os.getcwd(), "resource", "patus_ticket_logo.jpg"))
    printer.text(text)
    if show_qr_code:
        printer.qr("https://www.instagram.com/__patus_/")
        printer.qr("https://www.facebook.com/PATUS-il-dio-della-pasta-106229107452308")
    printer.cut()
    if cash_drawer and pin in [2, 5]:
        printer.cashdraw(pin)
    printer.close()


class Pay(QDialog):
    def __init__(
        self,
        callLog,
        printerProblem,
        worker_name: str,
        order_items: list,
        tax: float,
        comment: str,
        ticket_number: int,
        total: float,
        printerThread,
    ):
        super(Pay, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), "uis", "pay.ui"), self)
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

            if self.le_givenAmount.text() != "":
                total = float(self.le_givenAmount.text()) - self.lcdN_total.value()
                self.lcdN_return.setProperty("value", total)
        except Exception as e:
            logging.error(f"[PAY] ERROR: {e}")
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
                            given=given,
                        )
                        self.printerThread.printStatus.connect(self.printerProblem)
                        self.printerThread.logUpdater.connect(self.callLog)
                        self.printerThread.start()

                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setText("Sent to printer!")
                        msg.setWindowTitle("Information message")
                        msg.exec_()

                    except Exception as e:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText("Problem sending to printer!")
                        msg.setDetailedText(str(e))
                        msg.setWindowTitle("Warning message")
                        msg.exec_()

                self.accept()
            except Exception as e:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Printer problem")
                msg.setInformativeText("Check if the cashier printer is connected")
                msg.setDetailedText(str(e))
                msg.setWindowTitle("Warning message")
                msg.exec_()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Received money error")
            msg.setInformativeText("Received money should not be empty")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()
            # self.buttonBox.blockSignals(True)


class CheckerL(QDialog):
    def __init__(self):
        super(CheckerL, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), "uis", "LicenseProblem.ui"), self)
        self.l_adressMac.setText(LicenseChecker.get_mac())
        self.tb_copyMac.clicked.connect(self.copyMac)

    def accept(self):
        if LicenseChecker.check_license(self.le_licenseCode.text()):
            LicenseChecker.save_current_license(self.le_licenseCode.text())
            super().accept()
        else:
            self.le_licenseCode.clear()

    def copyMac(self):
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(self.l_adressMac.text())


class Reducer(QDialog):
    def __init__(self):
        super(Reducer, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), "uis", "reducer.ui"), self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.le_reduction.clear()
        self.le_reduction.setValidator(QDoubleValidator())


class LogPreviewer(QDialog):
    def __init__(self, logPath: str) -> None:
        super(LogPreviewer, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), "uis", "LogPreview.ui"), self)
        self.logPath = logPath
        self.btn_clear_logs.clicked.connect(self.clearLogs)
        self.btn_refresh_logs.clicked.connect(self.readLogs)
        self.btn_refresh_logs.click()

    def readLogs(self) -> None:
        if not os.path.exists(self.logPath):
            os.makedirs(self.logPath)
        self.tb_logs.clear()
        with open(self.logPath, "r") as f:
            self.tb_logs.setText(f.read())

    def clearLogs(self):
        with open(self.logPath, "r+") as f:
            f.truncate(0)
        self.readLogs()


class BlockNote(QDialog):
    def __init__(self, db=None) -> None:
        super(BlockNote, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), "uis", "BlockNote.ui"), self)
        self.db = db
        self.btn_clear.clicked.connect(self.clearNote)
        self.btn_save.clicked.connect(self.saveNote)

    def clearNote(self):
        self.pte_blockNote.clear()

    def saveNote(self):
        try:
            with open(os.path.join(os.getcwd(), "tmp", "note.txt"), "w") as f:
                f.write(self.pte_blockNote.toPlainText())
            description_json = openConvertFile(
                os.path.join(os.getcwd(), "tmp", "note.txt")
            )
            fileDoc = FileDoc(
                name="Block_Note",
                date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                comment="AUTO_GENERATED",
                file=description_json,
            )
            self.db.insertFileDoc(fileDoc)
            self.close()
        except Exception as e:
            logging.error(f"[BLOCK NOTE] Error: {e}")


class ConfirmDeletingOrder(QDialog):
    def __init__(self):
        super(ConfirmDeletingOrder, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), "uis", "ConfirmDeleteOrder.ui"), self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)


class ConfirmFullTicket(QDialog):
    def __init__(self):
        super(ConfirmFullTicket, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), "uis", "ConfirmFullTicket.ui"), self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)


class NbCoversChooser(QDialog):
    def __init__(self):
        super(NbCoversChooser, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), "uis", "NbCovers.ui"), self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.le_nb_covers.clear()
        self.le_nb_covers.setValidator(QIntValidator())


class EditOrderOnFly(QDialog):
    def __init__(self, quantity):
        super(EditOrderOnFly, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), "uis", "EditOrderOnFly.ui"), self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.le_orderItemOnFly_quantity.clear()
        self.le_orderItemOnFly_quantity.setText(str(quantity))
        self.le_orderItemOnFly_quantity.setValidator(QDoubleValidator())


class Holder(QDialog):
    def __init__(self):
        super(Holder, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), "uis", "holder.ui"), self)
        self.buttonBox.accepted.connect(self.validate_click)
        self.buttonBox.rejected.connect(self.reject)
        self.tw_orderHold.clear()
        self.DB = DBHelper()
        self.holdingOrders = self.DB.getAllHoldingSells()
        ho_show = []
        for ho in self.holdingOrders:
            ho_show.append(
                HoldingSellShow(Ticket_Number=ho.id, Total=ho.total, Date=ho.date)
            )
        displayDbData(self.tw_orderHold, ho_show)

    def validate_click(self):
        if self.tw_orderHold.currentRow() > -1:
            self.done(self.holdingOrders[self.tw_orderHold.currentRow()].id)
        else:
            self.buttonBox.blockSignals(True)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No order to resume")
            msg.setInformativeText("Please select the order to resume")
            msg.setWindowTitle("Warning message")
            msg.exec_()


class SellHistory(QDialog):
    def __init__(self, sell_id: int, parent: QWidget = None) -> None:
        super(SellHistory, self).__init__(parent=parent)
        uic.loadUi(os.path.join(os.getcwd(), "uis", "SellHistory.ui"), self)
        self.l_title.setText(self.l_title.text() + f" {sell_id}")
        self.tw_sellHistory.clear()
        self.DB = DBHelper()
        self.history = self.DB.getDifferenceHistoryBySellId(sell_id)
        displayDbData(self.tw_sellHistory, self.history)


class TableChanger(QDialog):
    def __init__(self, free_tables):
        super(TableChanger, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), "uis", "TableChanger.ui"), self)
        self.buttonBox.accepted.connect(self.validate_click)
        self.buttonBox.rejected.connect(self.reject)
        self.tw_freeTables.clear()
        self.free_tables = free_tables
        print("-" * 100)
        print(self.free_tables)
        print("-" * 100)
        displayDbData(self.tw_freeTables, self.free_tables)

    def validate_click(self):
        if self.tw_freeTables.currentRow() != -1:
            self.done(self.free_tables[self.tw_freeTables.currentRow()].id)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No table selected")
            msg.setInformativeText("Please select the new table")
            msg.setWindowTitle("Warning message")
            msg.exec_()
            self.done(-1)


class SettingUI(QDialog):
    def __init__(self):
        super(SettingUI, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), "uis", "Setting.ui"), self)
        self.dict_pin_index = {2: 0, 5: 1}
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
        self.cb_drawer_pin.setCurrentIndex(
            self.dict_pin_index[self.serverSetting.DRAWER_PIN]
        )

        self.le_ip.setValidator(
            QRegExpValidator(
                QRegExp(
                    "(\\b25[0-5]|\\b2[0-4][0-9]|\\b[01]?[0-9][0-9]?)(\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}"
                )
            )
        )
        self.le_cashier_ip.setValidator(
            QRegExpValidator(
                QRegExp(
                    "(\\b25[0-5]|\\b2[0-4][0-9]|\\b[01]?[0-9][0-9]?)(\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}"
                )
            )
        )
        self.le_kitchen_ip.setValidator(
            QRegExpValidator(
                QRegExp(
                    "(\\b25[0-5]|\\b2[0-4][0-9]|\\b[01]?[0-9][0-9]?)(\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}"
                )
            )
        )
        self.le_pizza_ip.setValidator(
            QRegExpValidator(
                QRegExp(
                    "(\\b25[0-5]|\\b2[0-4][0-9]|\\b[01]?[0-9][0-9]?)(\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}"
                )
            )
        )
        self.le_bar_ip.setValidator(
            QRegExpValidator(
                QRegExp(
                    "(\\b25[0-5]|\\b2[0-4][0-9]|\\b[01]?[0-9][0-9]?)(\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}"
                )
            )
        )

    def validate_click(self):
        if len(self.le_ip.text()) > 0:
            self.serverSetting.IP = self.le_ip.text()
            self.serverSetting.PORT = self.sb_port.value()
            self.serverSetting.MAX_CLIENTS = self.sb_maxClients.value()
            self.serverSetting.CASHIER_IP = self.le_cashier_ip.text()
            self.serverSetting.KITCHEN_IP = self.le_kitchen_ip.text()
            self.serverSetting.PIZZA_IP = self.le_pizza_ip.text()
            self.serverSetting.BAR_IP = self.le_bar_ip.text()
            self.serverSetting.DRAWER_PIN = int(self.cb_drawer_pin.currentText())
            self.serverSetting.save()
            self.done(1)
        else:
            self.buttonBox.blockSignals(True)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No order to resume")
            msg.setInformativeText("Please select the order to resume")
            msg.setWindowTitle("Warning message")
            msg.exec_()


class PrinterProblem(QDialog):
    def __init__(self, tickets: list, places: list):
        super(PrinterProblem, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), "uis", "PrinterProblem.ui"), self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        for child in self.f_ticketProblem.findChildren(QFrame):
            child.deleteLater()
        for ticket, place in zip(tickets, places):
            self.f_ticketProblem.layout().addWidget(
                createTicketContainer(self.f_ticketProblem, ticket, place)
            )


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
    text_edit.setFont(QFont("Cascadia Code", 10))
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


def createProductContainer(parent, db, product: MenuItem, table_id, fc):
    frame = QFrame(parent=parent)
    frame.setFrameShape(QFrame.StyledPanel)
    frame.setLineWidth(1)
    frame.setLayout(QVBoxLayout())
    frame.setMaximumSize(200, 400)
    # Picture or name
    label = QLabel(parent=frame)
    label.setPixmap(QPixmap(os.path.join(os.getcwd(), "resource", "patus_logo.jpg")))
    label.setScaledContents(True)
    label.setAlignment(Qt.AlignHCenter)
    label.setMaximumSize(200, 150)
    frame.layout().addWidget(label)
    label = QLabel(parent=frame)
    label.setText(pretty_string(product.name, 20, "returnLine"))
    label.setAlignment(Qt.AlignHCenter)
    frame.layout().addWidget(label)
    label = QLabel(parent=frame)
    label.setText(f"{to_money(product.price)} / {product.quantity} ({product.unit})")
    label.setStyleSheet("font-size: 8pt;")
    label.setAlignment(Qt.AlignHCenter)
    frame.layout().addWidget(label)
    # Ranking system
    comboBox = QComboBox(parent=frame)
    for i in range(5):
        comboBox.insertItem(i, f"Group {i+1}")
    frame.layout().addWidget(comboBox)
    # Supp
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
    order_item = OrderItem(
        tableId=table_id,
        productId=product.id,
        productName=product.name,
        productCategory=product.category_id,
        productUnit=product.unit,
        orderItemQuantity=product.quantity,
        orderItemTotal=product.price,
        orderItemSupplements=[],
        group_id=0,
        nb_covers=1,
        ready=0,
        served=0,
    )
    order_item_ = OrderItem(
        tableId=table_id,
        productId=product.id,
        productName=product.name,
        productUnit=product.unit,
        productCategory=product.category_id,
        orderItemQuantity=-product.quantity,
        orderItemTotal=-product.price,
        orderItemSupplements=[],
        group_id=0,
        nb_covers=1,
        ready=0,
        served=0,
    )
    add_button.clicked.connect(partial(fc, order_item, supp_list, comboBox))
    remove_button.clicked.connect(partial(fc, order_item_, supp_list, comboBox))
    # Buttons add specific number
    add_button_s = QPushButton(parent=btn_layout, text="++")
    remove_button_s = QPushButton(parent=btn_layout, text="--")
    order_item_s = OrderItem(
        tableId=table_id,
        productId=product.id,
        productName=product.name,
        productCategory=product.category_id,
        productUnit=product.unit,
        orderItemQuantity=product.quantity,
        orderItemTotal=product.price,
        orderItemSupplements=[],
        group_id=0,
        nb_covers=1,
        ready=0,
        served=0,
    )
    order_item__s = OrderItem(
        tableId=table_id,
        productId=product.id,
        productName=product.name,
        productCategory=product.category_id,
        productUnit=product.unit,
        orderItemQuantity=-product.quantity,
        orderItemTotal=-product.price,
        orderItemSupplements=[],
        group_id=0,
        nb_covers=1,
        ready=0,
        served=0,
    )

    add_button_s.clicked.connect(
        partial(custom_quantity, fc, order_item_s, supp_list, comboBox)
    )
    remove_button_s.clicked.connect(
        partial(custom_quantity, fc, order_item__s, supp_list, comboBox)
    )

    btn_layout.layout().addWidget(add_button_s)
    btn_layout.layout().addWidget(add_button)
    btn_layout.layout().addWidget(remove_button)
    btn_layout.layout().addWidget(remove_button_s)

    frame.layout().addWidget(btn_layout)

    return frame


def custom_quantity(fc, order_item, supp_list, comboBox):
    custom_quantity = CustomQuantity(fc, order_item, supp_list, comboBox)
    custom_quantity.show()
    custom_quantity.exec_()


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
    label.setFont(QFont("Times", 20))
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
    message_button.clicked.connect(partial(fc_message, client, text_edit))
    # message_button.clicked.connect(text_edit.clear)
    btn_layout.layout().addWidget(message_button)
    # buttons
    frame.layout().addWidget(btn_layout)
    return frame


def pretty_string(text: str, size: int = 20, mode: str = "strip") -> str:
    if mode == "strip":
        return text[:size]
    else:
        old_text = text
        new_test = ""
        for i in range(0, len(text), size):
            new_test += old_text[i : i + size] + "\n"
        return fr"{new_test}"


def prepareTicketForReceipt(
    worker_name: str, order_items: list, tax: float, comment: str, ticket_number: int
):
    total = 0
    ticket_txt = ""
    ticket_txt += "=" * 46 + " \n"
    ticket_txt += f"Ticket Number : {ticket_number:>30}\n"
    ticket_txt += f"Worker Name : {worker_name:>32}\n"
    ticket_txt += (
        f'Date and time : {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):>30}\n'
    )
    ticket_txt += "-" * 46 + " \n"
    if order_items[0].tableId is not None:
        ticket_txt += f"Table {order_items[0].tableId:>30}\n"
    else:
        ticket_txt += "Take away \n"
    ticket_txt += "-" * 46 + " \n"
    ticket_txt += f"{'ITEM':<20}{'QUANTITY':^13}{'PRICE':^13}\n"
    ticket_txt += "-" * 46 + " \n"
    for order_item in order_items:
        # if group != order_item.group_id:
        #     ticket_txt += f"{'*' * 46}\n"
        #     group = order_item.group_id
        total += order_item.orderItemTotal
        if (
            order_item.productUnit.strip().lower() == "g"
            or order_item.productUnit.strip().lower() == "kg"
        ):
            ticket_txt += f"{pretty_string(order_item.productName):<20}{f'{order_item.orderItemQuantity} {order_item.productUnit.strip().lower()}':^13}{to_money(order_item.orderItemTotal):^13}\n"
        else:
            ticket_txt += f"{pretty_string(order_item.productName):<20}{order_item.orderItemQuantity:^13}{to_money(order_item.orderItemTotal):^13}\n"
        for supp in order_item.orderItemSupplements:
            if (
                order_item.productUnit.strip().lower() == "g"
                or order_item.productUnit.strip().lower() == "kg"
            ):
                ticket_txt += (
                    f"+ {pretty_string(supp.name, 31):<31}{to_money(supp.price):^13}\n"
                )
                total += supp.price
            else:
                ticket_txt += f"+ {pretty_string(supp.name, 31):<31}{to_money(order_item.orderItemQuantity * supp.price):^13}\n"
                total += order_item.orderItemQuantity * supp.price

    if len(comment) > 0:
        ticket_txt += "-" * 46 + " \n"
        ticket_txt += comment + " \n"
    ticket_txt += "-" * 46 + " \n"
    ticket_txt += f"{'TOTAL':<33}{to_money(total):^13}\n"
    ticket_txt += f"{'REDUCTION':<33}{to_money(tax):^13}\n"
    ticket_txt += f"{'TOTAL TO PAY':<33}{to_money(total - tax):^13}\n"
    ticket_txt += "=" * 46 + " \n"
    return ticket_txt


def prepareTicketForCashier(
    worker_name: str,
    order_items: list,
    tax: float,
    comment: str,
    ticket_number: int,
    given: float,
    time_date: datetime.datetime = None,
):
    total = 0
    ticket_txt = ""
    ticket_txt += "=" * 46 + " \n"
    ticket_txt += f"Ticket Number : {ticket_number:>30}\n"
    ticket_txt += f"Worker Name : {worker_name:>32}\n"
    if time_date is None:
        ticket_txt += f'Date and time : {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):>30}\n'
    else:
        ticket_txt += f"Date and time : {time_date:>30}\n"
    ticket_txt += "-" * 46 + " \n"
    if order_items[0].tableId is not None:
        ticket_txt += f"Table {order_items[0].tableId:>30}\n"
    else:
        ticket_txt += "Take away \n"
    ticket_txt += "-" * 46 + " \n"
    ticket_txt += f"{'ITEM':<20}{'QUANTITY':^13}{'PRICE':^13}\n"
    ticket_txt += "-" * 46 + " \n"
    for order_item in order_items:
        # if group != order_item.group_id:
        #     ticket_txt += f"{'*' * 46}\n"
        #     group = order_item.group_id
        total += order_item.orderItemTotal

        if (
            order_item.productUnit.strip().lower() == "g"
            or order_item.productUnit.strip().lower() == "kg"
        ):
            ticket_txt += f"{pretty_string(order_item.productName):<20}{f'{order_item.orderItemQuantity} {order_item.productUnit.strip().lower()}':^13}{to_money(order_item.orderItemTotal):^13}\n"
        else:
            ticket_txt += f"{pretty_string(order_item.productName):<20}{order_item.orderItemQuantity:^13}{to_money(order_item.orderItemTotal):^13}\n"
        for supp in order_item.orderItemSupplements:
            if (
                order_item.productUnit.strip().lower() == "g"
                or order_item.productUnit.strip().lower() == "kg"
            ):
                ticket_txt += (
                    f"+ {pretty_string(supp.name, 31):<31}{to_money(supp.price):^13}\n"
                )
                total += supp.price
            else:
                ticket_txt += f"+ {pretty_string(supp.name, 31):<31}{to_money(order_item.orderItemQuantity * supp.price):^13}\n"
                total += order_item.orderItemQuantity * supp.price
    if len(comment) > 0:
        ticket_txt += "-" * 46 + " \n"
        ticket_txt += comment + " \n"
    ticket_txt += "-" * 46 + " \n"
    ticket_txt += f"{'TOTAL':<33}{to_money(total):^13}\n"
    ticket_txt += f"{'REDUCTION':<33}{to_money(tax):^13}\n"
    ticket_txt += f"{'TOTAL TO PAY':<33}{to_money(total - tax):^13}\n"
    ticket_txt += "=" * 46 + " \n"
    ticket_txt += f"{'RECEIVED':<33}{to_money(given):^13}\n"
    ticket_txt += f"{'RETURNED':<33}{to_money(given - total):^13}\n"
    ticket_txt += "=" * 46 + " \n"
    ticket_txt += f"{'PATUS vous remercie pour votre visite':^46}\n"
    ticket_txt += "=" * 46 + " \n"

    return ticket_txt


def prepareTicketForOrder(
    worker_name: str,
    order_items: List[OrderItem],
    comment: str,
    ticket_number: int,
    old: bool,
    cancel: bool = False,
    fr: bool = True,
) -> Union[str, str, str, int, int, int]:
    db = DBHelper()
    kitchen_count, pizza_count, drink_count = 0, 0, 0
    kitchen_group, pizza_group, drink_group = 0, 0, 0

    ticket_kitchen_txt = ""
    ticket_pizza_txt = ""
    ticket_bar_txt = ""

    now = datetime.datetime.now()
    if old:
        ticket_kitchen_txt += "=" * 46 + " \n"
        ticket_pizza_txt += "=" * 46 + " \n"
        ticket_bar_txt += "=" * 46 + " \n"

        if fr:
            ticket_kitchen_txt += f"{'MISE A JOUR':^46}" + " \n"
            ticket_pizza_txt += f"{'MISE A JOUR':^46}" + " \n"
            ticket_bar_txt += f"{'MISE A JOUR':^46}" + " \n"
        else:
            ticket_kitchen_txt += f"{'UPDATE':^46}" + " \n"
            ticket_pizza_txt += f"{'UPDATE':^46}" + " \n"
            ticket_bar_txt += f"{'UPDATE':^46}" + " \n"

    if cancel:
        ticket_kitchen_txt += "=" * 46 + " \n"
        ticket_pizza_txt += "=" * 46 + " \n"
        ticket_bar_txt += "=" * 46 + " \n"

        if fr:
            ticket_kitchen_txt += f"{'ANNULATION':^46}" + " \n"
            ticket_pizza_txt += f"{'ANNULATION':^46}" + " \n"
            ticket_bar_txt += f"{'ANNULATION':^46}" + " \n"
        else:
            ticket_kitchen_txt += f"{'CANCEL':^46}" + " \n"
            ticket_pizza_txt += f"{'CANCEL':^46}" + " \n"
            ticket_bar_txt += f"{'CANCEL':^46}" + " \n"

    # chef
    ticket_kitchen_txt += "=" * 46 + " \n"
    ticket_kitchen_txt += f"Ticket Number : {ticket_number:>30}\n"
    ticket_kitchen_txt += f"Worker Name : {worker_name:>32}\n"
    ticket_kitchen_txt += f'Date and time : {now.strftime("%Y-%m-%d %H:%M:%S"):>30}\n'
    ticket_kitchen_txt += "-" * 46 + " \n"
    if order_items[0].tableId is not None:
        ticket_kitchen_txt += f"Table {order_items[0].tableId:>40}\n"
    else:
        if fr:
            ticket_pizza_txt += "à emporter \n"
        else:
            ticket_pizza_txt += "Take away \n"

    # pizza yolo
    ticket_pizza_txt += "=" * 46 + " \n"
    ticket_pizza_txt += f"Ticket Number : {ticket_number:>30}\n"
    ticket_pizza_txt += f"Worker Name : {worker_name:>32}\n"
    ticket_pizza_txt += f'Date and time : {now.strftime("%Y-%m-%d %H:%M:%S"):>30}\n'
    ticket_pizza_txt += "-" * 46 + " \n"
    if order_items[0].tableId is not None:
        ticket_pizza_txt += f"Table {order_items[0].tableId:>40}\n"
    else:
        if fr:
            ticket_pizza_txt += "à emporter \n"
        else:
            ticket_pizza_txt += "Take away \n"

    # bar
    ticket_bar_txt += "=" * 46 + " \n"
    ticket_bar_txt += f"Ticket Number : {ticket_number:>30}\n"
    ticket_bar_txt += f"Worker Name : {worker_name:>32}\n"
    ticket_bar_txt += f'Date and time : {now.strftime("%Y-%m-%d %H:%M:%S"):>30}\n'
    ticket_bar_txt += "-" * 46 + " \n"
    if order_items[0].tableId is not None:
        ticket_bar_txt += f"Table {order_items[0].tableId:>40}\n"
    else:
        if fr:
            ticket_pizza_txt += "à emporter \n"
        else:
            ticket_pizza_txt += "Take away \n"

    # chef
    ticket_kitchen_txt += "-" * 46 + " \n"
    ticket_kitchen_txt += f"{'ITEM':<23}{'QUANTITY':^23}\n"
    ticket_kitchen_txt += "-" * 46 + " \n"

    # pizza yolo
    ticket_pizza_txt += "-" * 46 + " \n"
    ticket_pizza_txt += f"{'ITEM':<23}{'QUANTITY':^23}\n"
    ticket_pizza_txt += "-" * 46 + " \n"

    # bar
    ticket_bar_txt += "-" * 46 + " \n"
    ticket_bar_txt += f"{'ITEM':<23}{'QUANTITY':^23}\n"
    ticket_bar_txt += "-" * 46 + " \n"
    order_items.sort(key=lambda x: x.group_id)

    for order_item in order_items:
        if not bool(order_item.ready):
            if db.getMenuCategoryById(order_item.productCategory).printing_place == 2:
                if drink_group != order_item.group_id:
                    ticket_bar_txt += (
                        f"{'*' * 15}{f'Group {order_item.group_id}':^16}{'*' * 15}\n"
                    )
                    drink_group = order_item.group_id
                ticket_bar_txt += f"{pretty_string(order_item.productName, 23):<23} {order_item.orderItemQuantity:^23}\n"
                for supp in order_item.orderItemSupplements:
                    ticket_bar_txt += f"+ {pretty_string(supp.name, 23):<23}\n"
                drink_count += 1
            else:
                if kitchen_group != order_item.group_id:
                    ticket_kitchen_txt += (
                        f"{'*' * 15}{f'Group {order_item.group_id}':^16}{'*' * 15}\n"
                    )
                    kitchen_group = order_item.group_id
                if (
                    order_item.productUnit.strip().lower() == "g"
                    or order_item.productUnit.strip().lower() == "kg"
                ):
                    ticket_kitchen_txt += f"{pretty_string(order_item.productName, 23):<23} {f'{order_item.orderItemQuantity} {order_item.productUnit.strip().lower()}':^23}\n"
                else:
                    ticket_kitchen_txt += f"{pretty_string(order_item.productName, 23):<23} {order_item.orderItemQuantity:^23}\n"
                kitchen_count += 1
                for supp in order_item.orderItemSupplements:
                    ticket_kitchen_txt += f"+ {pretty_string(supp.name, 23):<23}\n"
                if (
                    db.getMenuCategoryById(order_item.productCategory).printing_place
                    == 1
                ):
                    if pizza_group != order_item.group_id:
                        ticket_pizza_txt += f"{'*' * 15}{f'Group {order_item.group_id}':^16}{'*' * 15}\n"
                        pizza_group = order_item.group_id
                    ticket_pizza_txt += f"{pretty_string(order_item.productName, 23):<23} {order_item.orderItemQuantity:^23}\n"
                    for supp in order_item.orderItemSupplements:
                        ticket_pizza_txt += f"+ {pretty_string(supp.name, 23):<23}\n"
                    pizza_count += 1

    if len(comment) > 0:
        ticket_kitchen_txt += "-" * 46 + " \n"
        ticket_pizza_txt += "-" * 46 + " \n"
        ticket_bar_txt += "-" * 46 + " \n"

        ticket_kitchen_txt += comment + " \n"
        ticket_pizza_txt += comment + " \n"
        ticket_bar_txt += comment + " \n"

    ticket_kitchen_txt += "=" * 46 + " \n"
    ticket_pizza_txt += "=" * 46 + " \n"
    ticket_bar_txt += "=" * 46 + " \n"

    return (
        ticket_kitchen_txt,
        ticket_pizza_txt,
        ticket_bar_txt,
        kitchen_count,
        pizza_count,
        drink_count,
    )


class MovableButton(QPushButton):
    drag_initiated = pyqtSignal(QPushButton)

    def __init__(self, **args):
        super(MovableButton, self).__init__(**args)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.RightButton:
            mimeData = QMimeData()
            drag = QDrag(self)
            drag.setMimeData(mimeData)
            self.drag_initiated.emit(self)
            drag.exec_(Qt.MoveAction)


class CustomTablesWidget(QWidget):
    def __init__(self, **args):
        super(CustomTablesWidget, self).__init__(objectName="w_tables", **args)
        self.setAcceptDrops(True)
        self.moving_btn = None
        self.settings = QSettings("Patus", "Tables")

    @pyqtSlot(QPushButton)
    def btn_moving(self, btn):
        self.moving_btn = btn

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        position = event.pos()
        if self.moving_btn:
            position.setX(position.x() - 60)
            position.setY(position.y() - 30)
            self.moving_btn.move(position)
            self.settings.setValue(f"table_{self.moving_btn.objectName()}", position)
        event.accept()


class CustomQuantity(QDialog):
    def __init__(self, fc, order_item: OrderItem, supp_list: list, comboBox: QComboBox):
        super(CustomQuantity, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), "uis", "customQuantity.ui"), self)
        self.le_quantity.setPlaceholderText(f"Quantity ({order_item.productUnit})")
        self.le_quantity.setValidator(QDoubleValidator())
        self.buttonBox.accepted.connect(self.validate_print)
        self.buttonBox.rejected.connect(self.reject)
        self.fc = fc
        self.order_item = order_item
        self.supp_list = supp_list
        self.comboBox = comboBox

    def validate_print(self):
        try:
            quantity = float(self.le_quantity.text())
            try:

                if self.order_item.orderItemQuantity < 0:
                    self.order_item.orderItemTotal = -self.order_item.orderItemTotal * (
                        quantity / self.order_item.orderItemQuantity
                    )
                    self.order_item.orderItemQuantity = -quantity
                else:
                    self.order_item.orderItemTotal = self.order_item.orderItemTotal * (
                        quantity / self.order_item.orderItemQuantity
                    )
                    self.order_item.orderItemQuantity = quantity
                self.fc(self.order_item, self.supp_list, self.comboBox)
                self.accept()
            except Exception as e:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Printer problem")
                msg.setInformativeText("Check if the cashier printer is connected")
                msg.setDetailedText(str(e))
                msg.setWindowTitle("Warning message")
                msg.exec_()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Quantity error")
            msg.setInformativeText("Quantity should not be empty")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()


def to_money(total: float, currency: str = "DA") -> str:
    return f"{total:,.2f} {currency}"


def addNewNotification(parent: QWidget, message: str) -> None:
    frame = QFrame(parent=parent)
    frame.setFrameShape(QFrame.StyledPanel)
    frame.setLineWidth(1)
    frame.setLayout(QHBoxLayout())
    frame.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum))

    label = QLabel()
    label.setText(datetime.datetime.now().strftime("%H:%M:%S"))
    label.setAlignment(Qt.AlignHCenter)
    frame.layout().addWidget(label)

    label = QLabel()
    label.setText(message)
    label.setAlignment(Qt.AlignHCenter)
    frame.layout().addWidget(label)

    parent.layout().addWidget(frame)


def getTicketDifference(
    old_orders: List[OrderItem], new_orders: List[OrderItem]
) -> List[OrderItem]:
    results = []
    # Check for updates
    for new_order in new_orders:
        new = None
        found = False
        for old_order in old_orders:
            if old_order.compare(new_order):
                found = True
                if new_order.isChanged(old_order):
                    new = new_order.getDiff(old_order)
                    break
        if not found:
            new = new_order
        if new is not None:
            results.append(new)

    # Check for deleted orders
    for old_order in old_orders:
        found = False
        for new_order in new_orders:
            if old_order.productId == new_order.productId:
                found = True
        if not found:
            results.append(old_order.getDeleted())
    return results
