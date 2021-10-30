from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import datetime
import os
from DB.DBHandler import DBHelper
from DB.DbTables import *
from functools import partial
import json
from Setting.Setting import ServerSetting


class Pay(QDialog):
    def __init__(self, total):
        super(Pay, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), 'uis', 'pay.ui'), self)
        self.lcdN_total.setProperty("value", total)
        self.le_givenAmount.setValidator(QDoubleValidator())
        self.le_givenAmount.textChanged.connect(self.calculator)
        self.buttonBox.accepted.connect(self.validate_print)
        self.buttonBox.rejected.connect(self.reject)

    def calculator(self):
        if self.buttonBox.signalsBlocked():
            self.buttonBox.blockSignals(False)
        try:
            total = float(self.le_givenAmount.text()) - self.lcdN_total.value()
            self.lcdN_return.setProperty("value", total)
        except Exception as e:
            print(e)
            self.lcdN_return.setProperty("value", 0)

    def validate_print(self):
        try:
            file = open('Receipt.txt', 'a')
            file.writelines('{0:25}{1:15}\n'.format(
                'RECEIVED', float(self.le_givenAmount.text())))
            file.writelines('{0:25}{1:15}\n'.format('RETURNED', float(self.le_givenAmount.text()) -
                                                    self.lcdN_total.value()))
            file.writelines('-' * 42 + ' \n')
            file.writelines('PATUS vous remercie pour votre visite')
            file.close()
            self.accept()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Received money error')
            msg.setInformativeText("Received money should not be empty")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()
            self.buttonBox.blockSignals(True)


class Holder(QDialog):
    def __init__(self):
        super(Holder, self).__init__()
        uic.loadUi(os.path.join(os.getcwd(), 'uis', 'holder.ui'), self)
        self.buttonBox.accepted.connect(self.validate_click)
        self.buttonBox.rejected.connect(self.reject)
        self.tw_orderHold.clear()
        self.DB = DBHelper()
        self.holdingOrders = self.DB.getAllHoldingSells()
        displayDbData(self.tw_orderHold, self.holdingOrders)

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

    def validate_click(self):
        if len(self.le_ip.text()) > 0:
            self.serverSetting.IP = self.le_ip.text()
            self.serverSetting.PORT = self.sb_port.value()
            self.serverSetting.MAX_CLIENTS = self.sb_maxClients.value()
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


def printTicket(worker_name: str, order_items: list, tax: float):
    try:
        total = 0
        file = open('Receipt.txt', 'wt')
        file.writelines('-' * 42 + ' \n')
        file.writelines('Worker Name:\t\t\t\t{} \n'.format(worker_name))
        file.writelines("Date and time : ")
        file.writelines(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        file.writelines('\n')
        file.writelines('-' * 42 + ' \n')
        if order_items[0].tableId is not None:
            file.writelines('Table {} \n'.format(order_items[0].tableId))
        else:
            file.writelines('Take away \n')
        file.writelines('-' * 42 + ' \n')
        file.writelines('{0:20}{1:15}{2:15}\n'.format(
            'ITEM', 'QUANTITY', 'PRICE'))
        file.writelines('-' * 42 + ' \n')
        for order_item in order_items:
            total += order_item.orderItemTotal * order_item.orderItemQuantity
            file.writelines('{0:{width}{base}}'.format(
                order_item.productName, base='s', width=25))
            file.writelines('{0:{width}{base}}'.format(
                int(order_item.orderItemQuantity), base='d', width=4))
            file.writelines('{0:{width}{base}}\n'.format(order_item.orderItemTotal * order_item.orderItemQuantity,
                                                         base='.2f', width=12))
        file.writelines('-' * 42 + ' \n')
        file.writelines('{0:25}{1:15}\n'.format('TOTAL', total))
        file.writelines('{0:25}{1:15}\n'.format('TOTAL TAX', total * tax))
        file.writelines('{0:25}{1:15}\n'.format(
            'TOTAL TO PAY', total + (total * tax)))
        file.writelines('-' * 42 + ' \n')
        file.close()
    except Exception as e:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText('No items to pay')
        msg.setInformativeText("The list of items is empty")
        msg.setDetailedText(str(e))
        msg.setWindowTitle("Warning message")
        msg.exec_()


def kitchenTicket(worker_name: str, order_items: list):
    try:
        pizza_count = 0
        file = open('chef.txt', 'wt')
        file_ = open('pizzaYolo.txt', 'wt')
        now = datetime.datetime.now()
        # chef
        file.writelines('-' * 42 + ' \n')
        file.writelines('Worker Name:\t\t\t\t{} \n'.format(worker_name))
        file.writelines("Date and time : ")
        file.writelines(now.strftime("%Y-%m-%d %H:%M:%S"))
        file.writelines('\n')
        file.writelines('-' * 42 + ' \n')
        # pizza yolo
        file_.writelines('-' * 42 + ' \n')
        file_.writelines('Worker Name:\t\t\t\t{} \n'.format(worker_name))
        file_.writelines("Date and time : ")
        file_.writelines(now.strftime("%Y-%m-%d %H:%M:%S"))
        file_.writelines('\n')
        file_.writelines('-' * 42 + ' \n')
        if order_items[0].tableId is not None:
            file.writelines('Table {} \n'.format(order_items[0].tableId))
            file_.writelines('Table {} \n'.format(order_items[0].tableId))
        else:
            file.writelines('Take away \n')
            file_.writelines('Take away \n')
        # chef
        file.writelines('-' * 42 + ' \n')
        file.writelines('{0:20}{1:15}\n'.format('ITEM', 'QUANTITY'))
        file.writelines('-' * 42 + ' \n')
        # pizza yolo
        file.writelines('-' * 42 + ' \n')
        file.writelines('{0:20}{1:15}\n'.format('ITEM', 'QUANTITY'))
        file.writelines('-' * 42 + ' \n')
        for order_item in order_items:
            file.writelines('{0:{width}{base}}'.format(
                order_item.productName, base='s', width=25))
            file.writelines('{0:{width}{base}}\n'.format(
                int(order_item.orderItemQuantity), base='d', width=4))
            if order_item.productCategory == "Pizza":
                pizza_count += 1
                file_.writelines('{0:{width}{base}}'.format(
                    order_item.productName, base='s', width=25))
                file_.writelines('{0:{width}{base}}\n'.format(
                    int(order_item.orderItemQuantity), base='d', width=4))
        file.writelines('-' * 42 + ' \n')
        file.close()
        file_.writelines('-' * 42 + ' \n')
        file_.close()
        return pizza_count
    except Exception as e:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText('No items to send to the kitchen')
        msg.setInformativeText("The list of items is empty")
        msg.setDetailedText(str(e))
        msg.setWindowTitle("Warning message")
        msg.exec_()
        return None


def createProductContainer(parent, product, table_id, fc):
    frame = QFrame(parent=parent)
    frame.setFrameShape(QFrame.StyledPanel)
    frame.setLineWidth(1)
    frame.setLayout(QVBoxLayout())
    frame.setMaximumSize(200, 300)
    # Picture or name
    label = QLabel()
    label.setPixmap(QPixmap("patus_logo.jpg"))
    label.setScaledContents(True)
    label.setAlignment(Qt.AlignHCenter)
    label.setMaximumSize(200, 200)
    frame.layout().addWidget(label)
    label = QLabel()
    label.setText(product.name)
    label.setAlignment(Qt.AlignHCenter)
    frame.layout().addWidget(label)
    # Add and Reduce
    btn_layout = QFrame(parent=frame)
    btn_layout.setLayout(QHBoxLayout())
    btn_layout.setMaximumSize(200, 200)
    add_button = QPushButton(parent=btn_layout, text="+")
    remove_button = QPushButton(parent=btn_layout, text="-")
    order_item = OrderItem(table_id, product.id, product.name,
                           product.category, 1, product.price)
    order_item_ = OrderItem(table_id, product.id,
                            product.name, product.category, -1, -product.price)
    add_button.clicked.connect(partial(fc, order_item))
    remove_button.clicked.connect(partial(fc, order_item_))
    btn_layout.layout().addWidget(add_button)
    btn_layout.layout().addWidget(remove_button)
    # buttons
    frame.layout().addWidget(btn_layout)
    return frame
