from DB.DBHandler import DBHelper
from DB.DbTables import *
from Threads import *

from Utilities.UiUtilities import *
from resource import resource_rc

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from functools import partial
from PyQt5 import uic
import threading
import datetime
import hashlib
import Threads
import time
import copy
import sys
import os


class PatusMainUI(QMainWindow):
    def __init__(self, **kwargs):
        super(PatusMainUI, self).__init__(**kwargs)
        uic.loadUi(os.path.join(os.getcwd(), 'uis', 'PatusInterface.ui'), self)
        self.DB = DBHelper()
        self.sw_content.setCurrentIndex(0)
        try:
            self.serverThread = ServerThread()
        except Exception as e:
            print(f"Server not running --> {e}")
            self.serverThread = None
        self.infoThread = InfoThread()
        # db current item selected
        self.currentPointer = None
        self.currentSell = None
        self.currentWorker = None
        self.current = None
        self.current_table = None
        self.currentOrder = []
        self.tax = 0.15
        self.categoryDict, self.workerDict, self.customerDict = {}, {}, {}
        self.categoryDictId, self.workerDictId, self.customerDictId = {}, {}, {}

        # Side panel menu
        self.btn_sideBar.clicked.connect(self.showHideSideBar)
        self.btn_logInOut.clicked.connect(
            lambda: self.sw_content.setCurrentIndex(1))
        self.btn_tables.clicked.connect(
            lambda: self.sw_content.setCurrentIndex(2))
        self.btn_tables.clicked.connect(self.populateTables)
        self.btn_cashRegister.clicked.connect(
            lambda: self.sw_content.setCurrentIndex(3))
        self.btn_database.clicked.connect(
            lambda: self.sw_content.setCurrentIndex(4))
        self.btn_database.clicked.connect(self.twDbHandler)
        self.btn_exit.clicked.connect(self.logout)

        # Login
        self.btn_loginConfirm.clicked.connect(self.login)

        # Cash Register
        self.populateProducts()
        self.btn_cashRegisterPay.clicked.connect(self.pay)
        self.btn_cashRegisterClear.clicked.connect(self.clearCashRegister)
        self.btn_cashRegisterHold.clicked.connect(self.holdOrder)
        self.btn_cashRegisterResume.clicked.connect(self.resumeOrder)
        self.btn_cashRegisterTicket.clicked.connect(lambda: printTicket(self.currentWorker.name, self.currentOrder,
                                                                        self.tax))
        self.btn_cashRegisterTicket.clicked.connect(
            lambda: kitchenTicket(self.currentWorker.name, self.currentOrder))

        # Database
        self.tw_database.currentChanged.connect(self.twDbHandler)
        self.populateCb()
        # Finish Product
        self.btn_finishProductAdd.clicked.connect(self.addFinishProduct)
        self.btn_finishProductEdit.clicked.connect(self.editFinishProduct)
        self.btn_finishProductDelete.clicked.connect(self.deleteFinishProduct)
        self.btn_finishProductClear.clicked.connect(
            lambda: self.btn_finishProductAdd.setEnabled(True))
        self.btn_finishProductClear.clicked.connect(
            lambda: self.btn_finishProductEdit.setEnabled(False))
        self.btn_finishProductClear.clicked.connect(
            lambda: self.btn_finishProductDelete.setEnabled(False))
        self.btn_finishProductClear.clicked.connect(
            lambda: self.le_finishProductName.clear())
        self.btn_finishProductClear.clicked.connect(
            lambda: self.le_finishProductQuantity.clear())
        self.btn_finishProductClear.clicked.connect(
            lambda: self.le_finishProductPrice.clear())
        self.btn_finishProductClear.clicked.connect(
            lambda: self.l_finishProductPicture.clear())
        self.btn_finishProductClear.clicked.connect(
            lambda: self.cb_finishProductCategory.setCurrentIndex(0))
        self.btn_finishProductPictureClear.clicked.connect(
            lambda: self.l_finishProductPicture.clear())
        self.btn_finishProductPicture.clicked.connect(
            lambda: self.pictureSelector(self.l_finishProductPicture))
        self.tw_finishProduct.doubleClicked.connect(self.loadFinishProduct)
        self.le_finishProductPrice.setValidator(QDoubleValidator())
        self.le_finishProductQuantity.setValidator(QDoubleValidator())
        self.finishProductDict = {
            "Salade": 0, "Meal": 1, "Pizza": 2, "Cold Drink": 3, "Hot Drink": 4, "Dessert": 5}
        # Raw Product
        self.rawProductDict = {"Vegetable": 0,
                               "Meat": 1, "Drink": 2, "Powder": 3, "Fruit": 4}
        self.btn_rawProductAdd.clicked.connect(self.addRawProduct)
        self.btn_rawProductEdit.clicked.connect(self.editRawProduct)
        self.btn_rawProductDelete.clicked.connect(self.deleteRawProduct)
        self.btn_rawProductClear.clicked.connect(
            lambda: self.btn_rawProductAdd.setEnabled(True))
        self.btn_rawProductClear.clicked.connect(
            lambda: self.btn_rawProductEdit.setEnabled(False))
        self.btn_rawProductClear.clicked.connect(
            lambda: self.btn_rawProductDelete.setEnabled(False))
        self.btn_rawProductClear.clicked.connect(
            lambda: self.le_rawProductName.clear())
        self.btn_rawProductClear.clicked.connect(
            lambda: self.le_rawProductQuantity.clear())
        self.btn_rawProductClear.clicked.connect(
            lambda: self.le_rawProductPrice.clear())
        self.btn_rawProductClear.clicked.connect(
            lambda: self.cb_rawProductCategory.setCurrentIndex(0))
        self.tw_rawProduct.doubleClicked.connect(self.loadRawProduct)
        self.le_rawProductQuantity.setValidator(QDoubleValidator())
        self.le_rawProductPrice.setValidator(QDoubleValidator())
        # Customer
        self.btn_customerAdd.clicked.connect(self.addCustomer)
        self.btn_customerEdit.clicked.connect(self.editCustomer)
        self.btn_customerDelete.clicked.connect(self.deleteCustomer)
        self.btn_customerClear.clicked.connect(
            lambda: self.btn_customerAdd.setEnabled(True))
        self.btn_customerClear.clicked.connect(
            lambda: self.btn_customerEdit.setEnabled(False))
        self.btn_customerClear.clicked.connect(
            lambda: self.btn_customerDelete.setEnabled(False))
        self.btn_customerClear.clicked.connect(
            lambda: self.le_customerName.clear())
        self.btn_customerClear.clicked.connect(
            lambda: self.le_customerPhone.clear())
        self.btn_customerClear.clicked.connect(
            lambda: self.le_customerAddress.clear())
        self.btn_customerClear.clicked.connect(
            lambda: self.l_customerPicture.clear())
        self.btn_customerClear.clicked.connect(
            lambda: self.le_customerScore.clear())
        self.btn_customerPictureClear.clicked.connect(
            lambda: self.l_customerPicture.clear())
        self.btn_customerPicture.clicked.connect(
            lambda: self.pictureSelector(self.l_customerPicture))
        self.tw_customer.doubleClicked.connect(self.loadCustomer)
        self.le_customerScore.setValidator(QDoubleValidator())
        # Worker
        self.btn_workerAdd.clicked.connect(self.addWorker)
        self.btn_workerEdit.clicked.connect(self.editWorker)
        self.btn_workerDelete.clicked.connect(self.deleteWorker)
        self.btn_workerClear.clicked.connect(
            lambda: self.btn_workerAdd.setEnabled(True))
        self.btn_workerClear.clicked.connect(
            lambda: self.btn_workerEdit.setEnabled(False))
        self.btn_workerClear.clicked.connect(
            lambda: self.btn_workerDelete.setEnabled(False))
        self.btn_workerClear.clicked.connect(
            lambda: self.le_workerName.clear())
        self.btn_workerClear.clicked.connect(
            lambda: self.le_workerUsername.clear())
        self.btn_workerClear.clicked.connect(
            lambda: self.le_workerPassword.clear())
        self.btn_workerClear.clicked.connect(
            lambda: self.le_workerPhone.clear())
        self.btn_workerClear.clicked.connect(
            lambda: self.le_workerAddress.clear())
        self.btn_workerClear.clicked.connect(
            lambda: self.l_workerPicture.clear())
        self.btn_workerClear.clicked.connect(
            lambda: self.le_workerScore.clear())
        self.btn_workerClear.clicked.connect(
            lambda: self.cb_workerCategory.setCurrentIndex(0))
        self.btn_workerPictureClear.clicked.connect(
            lambda: self.l_workerPicture.clear())
        self.btn_workerPicture.clicked.connect(
            lambda: self.pictureSelector(self.l_workerPicture))
        self.tw_worker.doubleClicked.connect(self.loadWorker)
        self.le_workerScore.setValidator(QDoubleValidator())
        # Sell
        self.btn_sellAdd.clicked.connect(self.addSell)
        self.btn_sellEdit.clicked.connect(self.editSell)
        self.btn_sellDelete.clicked.connect(self.deleteSell)
        self.btn_sellClear.clicked.connect(
            lambda: self.btn_sellAdd.setEnabled(True))
        self.btn_sellClear.clicked.connect(
            lambda: self.btn_sellEdit.setEnabled(False))
        self.btn_sellClear.clicked.connect(
            lambda: self.btn_sellDelete.setEnabled(False))
        self.btn_sellClear.clicked.connect(lambda: self.le_sellTotal.clear())
        self.btn_sellClear.clicked.connect(
            lambda: self.cb_sellIdWorker.setCurrentIndex(0))
        self.btn_sellClear.clicked.connect(
            lambda: self.cb_sellIdCustomer.setCurrentIndex(0))
        self.tw_sell.doubleClicked.connect(self.loadSell)
        self.le_sellTotal.setValidator(QDoubleValidator())
        # Table
        self.btn_tableAdd.clicked.connect(self.addTable)
        self.btn_tableEdit.clicked.connect(self.editTable)
        self.btn_tableDelete.clicked.connect(self.deleteTable)
        self.btn_tableClear.clicked.connect(
            lambda: self.btn_tableAdd.setEnabled(True))
        self.btn_tableClear.clicked.connect(
            lambda: self.btn_tableEdit.setEnabled(False))
        self.btn_tableClear.clicked.connect(
            lambda: self.btn_tableDelete.setEnabled(False))
        self.btn_tableClear.clicked.connect(lambda: self.le_tableName.clear())
        self.btn_tableClear.clicked.connect(lambda: self.le_tableId.clear())
        self.btn_tableClear.clicked.connect(lambda: self.le_tableSeats.clear())
        self.tw_table.doubleClicked.connect(self.loadTable)
        self.le_tableId.setValidator(QIntValidator())
        self.le_tableSeats.setValidator(QIntValidator())
        # Category
        self.btn_categoryAdd.clicked.connect(self.addCategory)
        self.btn_categoryEdit.clicked.connect(self.editCategory)
        self.btn_categoryDelete.clicked.connect(self.deleteCategory)
        self.btn_categoryClear.clicked.connect(
            lambda: self.btn_categoryAdd.setEnabled(True))
        self.btn_categoryClear.clicked.connect(
            lambda: self.btn_categoryEdit.setEnabled(False))
        self.btn_categoryClear.clicked.connect(
            lambda: self.btn_categoryDelete.setEnabled(False))
        self.btn_categoryClear.clicked.connect(
            lambda: self.le_categoryName.clear())
        self.btn_categoryClear.clicked.connect(
            lambda: self.cb_categoryLevel.setCurrentIndex(0))
        self.tw_category.doubleClicked.connect(self.loadCategory)
        # Pointer
        self.btn_pointerAdd.clicked.connect(self.addPointer)
        self.btn_pointerEdit.clicked.connect(self.editPointer)
        self.btn_pointerDelete.clicked.connect(self.deletePointer)
        self.btn_pointerClear.clicked.connect(
            lambda: self.btn_pointerAdd.setEnabled(True))
        self.btn_pointerClear.clicked.connect(
            lambda: self.btn_pointerEdit.setEnabled(False))
        self.btn_pointerClear.clicked.connect(
            lambda: self.btn_pointerDelete.setEnabled(False))
        self.btn_pointerClear.clicked.connect(
            lambda: self.cb_pointerIdWorker.setCurrentIndex(0))
        self.tw_pointer.doubleClicked.connect(self.loadPointer)

        # Main Window
        self.btn_fullScreen.clicked.connect(self.fullScreen)
        self.btn_setting.clicked.connect(self.changeSettings)
        self.show()
        self.homeScreen()
        self.infoThread.start()
        self.infoThread.UpdateInfo.connect(self.updateInfo)
        if self.serverThread is not None:
            self.serverThread.start()

    """Server Main"""

    def startServer(self):
        try:
            if self.serverThread is None:
                self.serverThread = Threads.ServerThread()
                self.serverThread.STOPPED.connect(self.stoppedServerThread)
                self.serverThread.start()
            else:
                self.serverThread.stop()
        except Exception as e:
            print(f"Main window start threads {e}")

    def stoppedServerThread(self):
        self.serverThread = None

    """SideBarMenu"""

    def showHideSideBar(self):
        if self.f_sideBar.isVisible():
            self.f_sideBar.setVisible(False)
        else:
            self.f_sideBar.setVisible(True)

    """Home screen"""

    def homeScreen(self):
        def homeThread():
            while self.sw_content.currentIndex() == 0 and self:
                current_datetime = datetime.datetime.now()
                self.l_time.setText(
                    f'{current_datetime.hour:02d}:{current_datetime.minute:02d}:{current_datetime.second:02d}')
                self.l_date.setText(f'{current_datetime.date()}')
                time.sleep(1)
        home_thread = threading.Thread(target=homeThread)
        home_thread.start()

    """Main Window"""

    def fullScreen(self):
        if self.isFullScreen():
            self.showMaximized()
        else:
            self.showFullScreen()

    """Database"""

    def pictureSelector(self, holder):
        try:
            file_name = QFileDialog.getOpenFileName(self, "Choose a picture", os.getcwd(), "JPG Files (*.jpg);;"
                                                    "PNG Files (*.png);;JPEG Files (*.jpeg);;SVG Files (*.svg)")[0]
            print(file_name)
            if os.path.isfile(file_name):
                # pickle.dump(self.picture, open("pic_compress.p", "wb"))
                pic_pixmap = QPixmap(file_name)
                holder.clear()
                holder.setPixmap(pic_pixmap)
        except Exception as e:
            print(e)

    def twDbHandler(self):
        try:
            if self.tw_database.currentIndex() == 0:
                all_data = self.DB.getAllFinishProducts()
                displayDbData(self.tw_finishProduct, all_data)
            elif self.tw_database.currentIndex() == 1:
                all_data = self.DB.getAllRawProducts()
                displayDbData(self.tw_rawProduct, all_data)
            elif self.tw_database.currentIndex() == 2:
                all_data = self.DB.getAllCustomers()
                displayDbData(self.tw_customer, all_data)
            elif self.tw_database.currentIndex() == 3:
                all_data = self.DB.getAllWorkers()
                displayDbData(self.tw_worker, all_data)
            elif self.tw_database.currentIndex() == 4:
                all_data = self.DB.getAllSells()
                displayDbData(self.tw_sell, all_data)
            elif self.tw_database.currentIndex() == 5:
                all_data = self.DB.getAllTables()
                displayDbData(self.tw_table, all_data)
            elif self.tw_database.currentIndex() == 6:
                all_data = self.DB.getAllCategories()
                displayDbData(self.tw_category, all_data)
            else:
                all_data = self.DB.getAllPointers()
                displayDbData(self.tw_pointer, all_data)
        except Exception as e:
            print(e)

    def populateCb(self):
        self.cb_workerCategory.clear()
        self.cb_sellIdWorker.clear()
        self.cb_pointerIdWorker.clear()
        self.cb_orderCustomer.clear()
        self.cb_sellIdCustomer.clear()
        for i, category in enumerate(self.DB.getAllCategories()):
            self.categoryDict[i] = category.id
            self.categoryDictId[category.id] = i
            self.cb_workerCategory.insertItem(i, category.name)
        for i, worker in enumerate(self.DB.getAllWorkers()):
            self.workerDict[i] = worker.id
            self.workerDictId[worker.id] = i
            self.cb_sellIdWorker.insertItem(i, worker.name)
            self.cb_pointerIdWorker.insertItem(i, worker.name)
        for i, customer in enumerate(self.DB.getAllCustomers()):
            self.customerDict[i] = customer.id
            self.customerDictId[customer.id] = i
            self.cb_orderCustomer.insertItem(i, customer.name)
            self.cb_sellIdCustomer.insertItem(i, customer.name)

    # Finish Product
    def loadFinishProduct(self):
        self.current = self.DB.getFinishProductById(int(self.tw_finishProduct.item(self.tw_finishProduct.currentRow(),
                                                                                   self.tw_finishProduct.columnCount()
                                                                                   - 1).text()))
        self.le_finishProductName.setText(self.current.name)
        self.le_finishProductQuantity.setText(str(self.current.quantity))
        self.le_finishProductPrice.setText(str(self.current.price))
        self.l_finishProductPicture.setText(self.current.picture)
        self.cb_finishProductCategory.setCurrentIndex(
            self.finishProductDict[self.current.category])
        self.btn_finishProductAdd.setEnabled(False)
        self.btn_finishProductEdit.setEnabled(True)
        self.btn_finishProductDelete.setEnabled(True)

    def addFinishProduct(self):
        try:
            # pic = self.l_finishProductPicture.pixmap().toImage()
            finish_product = FinishProduct(self.le_finishProductName.text(),
                                           self.cb_finishProductCategory.currentText(),
                                           float(
                                               self.le_finishProductQuantity.text()),
                                           float(self.le_finishProductPrice.text()), self.l_finishProductPicture.text())
            self.DB.insertFinishProduct(finish_product)
            # clear all
            self.le_finishProductName.clear()
            self.le_finishProductQuantity.clear()
            self.le_finishProductPrice.clear()
            self.l_finishProductPicture.clear()
            self.cb_finishProductCategory.setCurrentIndex(0)
            self.twDbHandler()
            self.populateProducts()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Check your fields')
            msg.setInformativeText("Finish Product not added")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def editFinishProduct(self):
        try:
            assert isinstance(self.current, FinishProduct)
            self.current.name = self.le_finishProductName.text()
            self.current.category = self.cb_finishProductCategory.currentText()
            self.current.quantity = float(self.le_finishProductQuantity.text())
            self.current.price = float(self.le_finishProductPrice.text())
            self.current.picture = self.l_finishProductPicture.text()
            self.DB.updateFinishProduct(self.current)
            # clear all
            self.le_finishProductName.clear()
            self.le_finishProductQuantity.clear()
            self.le_finishProductPrice.clear()
            self.l_finishProductPicture.clear()
            self.cb_finishProductCategory.setCurrentIndex(0)
            self.btn_finishProductAdd.setEnabled(True)
            self.btn_finishProductEdit.setEnabled(False)
            self.btn_finishProductDelete.setEnabled(False)
            self.twDbHandler()
            self.populateProducts()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Check your fields')
            msg.setInformativeText("Raw Product not updated")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def deleteFinishProduct(self):
        try:
            assert isinstance(self.current, FinishProduct)
            self.DB.deleteFinishProduct(self.current.id)
            # clear all
            self.le_finishProductName.clear()
            self.le_finishProductQuantity.clear()
            self.le_finishProductPrice.clear()
            self.l_finishProductPicture.clear()
            self.cb_finishProductCategory.setCurrentIndex(0)
            self.btn_finishProductAdd.setEnabled(True)
            self.btn_finishProductEdit.setEnabled(False)
            self.btn_finishProductDelete.setEnabled(False)
            self.twDbHandler()
            self.populateProducts()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Check your fields')
            msg.setInformativeText("Finish Product not deleted")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    # Raw Product
    def loadRawProduct(self):
        self.current = self.DB.getRawProductById(int(self.tw_rawProduct.item(self.tw_rawProduct.currentRow(),
                                                                             self.tw_rawProduct.columnCount()
                                                                             - 1).text()))
        self.le_rawProductName.setText(self.current.name)
        self.le_rawProductQuantity.setText(str(self.current.quantity))
        self.le_rawProductPrice.setText(str(self.current.price))
        self.cb_rawProductCategory.setCurrentIndex(
            self.rawProductDict[self.current.category])
        self.btn_rawProductAdd.setEnabled(False)
        self.btn_rawProductEdit.setEnabled(True)
        self.btn_rawProductDelete.setEnabled(True)

    def addRawProduct(self):
        try:
            raw_product = RawProduct(self.le_rawProductName.text(), self.cb_rawProductCategory.currentText(),
                                     float(self.le_rawProductQuantity.text()),
                                     float(self.le_rawProductPrice.text()))
            self.DB.insertRawProduct(raw_product)
            # clear all
            self.le_rawProductName.clear()
            self.le_rawProductQuantity.clear()
            self.le_rawProductPrice.clear()
            self.cb_rawProductCategory.setCurrentIndex(0)
            self.twDbHandler()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Check your fields')
            msg.setInformativeText("Raw Product not added")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def editRawProduct(self):
        try:
            assert isinstance(self.current, RawProduct)
            self.current.name = self.le_rawProductName.text()
            self.current.quantity = float(self.le_rawProductQuantity.text())
            self.current.category = self.cb_rawProductCategory.currentText()
            self.current.price = float(self.le_rawProductPrice.text())
            self.DB.updateRawProduct(self.current)
            # clear all
            self.le_rawProductName.clear()
            self.le_rawProductQuantity.clear()
            self.le_rawProductPrice.clear()
            self.cb_rawProductCategory.setCurrentIndex(0)
            self.btn_rawProductAdd.setEnabled(True)
            self.btn_rawProductEdit.setEnabled(False)
            self.btn_rawProductDelete.setEnabled(False)
            self.twDbHandler()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Check your fields')
            msg.setInformativeText("Raw Product not updated")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def deleteRawProduct(self):
        try:
            assert isinstance(self.current, RawProduct)
            self.DB.deleteRawProduct(self.current.id)
            # clear all
            self.le_rawProductName.clear()
            self.le_rawProductQuantity.clear()
            self.le_rawProductPrice.clear()
            self.cb_rawProductCategory.setCurrentIndex(0)
            self.btn_rawProductAdd.setEnabled(True)
            self.btn_rawProductEdit.setEnabled(False)
            self.btn_rawProductDelete.setEnabled(False)
            self.twDbHandler()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Check your fields')
            msg.setInformativeText("Raw Product not deleted")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    # Customer
    def loadCustomer(self):
        self.current = self.DB.getCustomerById(int(self.tw_customer.item(self.tw_customer.currentRow(),
                                                                         self.tw_customer.columnCount() - 1).text()))
        self.le_customerName.setText(self.current.name)
        self.le_customerPhone.setText(str(self.current.phone))
        self.le_customerAddress.setText(self.current.address)
        self.le_customerScore.setText(str(self.current.score))
        self.l_customerPicture.setText(str(self.current.picture))
        self.btn_customerAdd.setEnabled(False)
        self.btn_customerEdit.setEnabled(True)
        self.btn_customerDelete.setEnabled(True)

    def addCustomer(self):
        try:
            customer = Customer(self.le_customerName.text(), self.le_customerPhone.text(), self.le_customerAddress.text(),
                                float(self.le_customerScore.text()), self.l_customerPicture.text(), None)
            self.DB.insertCustomer(customer)
            # clear all
            self.le_customerName.clear()
            self.le_customerPhone.clear()
            self.le_customerAddress.clear()
            self.le_customerScore.clear()
            self.l_customerPicture.clear()
            self.twDbHandler()
            self.populateCb()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Check your fields')
            msg.setInformativeText("Customer not added")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def editCustomer(self):
        try:
            assert isinstance(self.current, Customer)
            self.current.name = self.le_customerName.text()
            self.current.phone = self.le_customerPhone.text()
            self.current.address = self.le_customerAddress.text()
            self.current.score = float(self.le_customerScore.text())
            self.current.picture = None
            self.current.face = None
            self.DB.updateCustomer(self.current)
            # clear all
            self.le_customerName.clear()
            self.le_customerPhone.clear()
            self.le_customerAddress.clear()
            self.le_customerScore.clear()
            self.l_customerPicture.clear()
            self.btn_customerAdd.setEnabled(True)
            self.btn_customerEdit.setEnabled(False)
            self.btn_customerDelete.setEnabled(False)
            self.twDbHandler()
            self.populateCb()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Check your fields')
            msg.setInformativeText("Customer not updated")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def deleteCustomer(self):
        try:
            assert isinstance(self.current, Customer)
            self.DB.deleteCustomer(self.current.id)
            # clear all
            self.le_customerName.clear()
            self.le_customerPhone.clear()
            self.le_customerAddress.clear()
            self.le_customerScore.clear()
            self.l_customerPicture.clear()
            self.btn_customerAdd.setEnabled(True)
            self.btn_customerEdit.setEnabled(False)
            self.btn_customerDelete.setEnabled(False)
            self.twDbHandler()
            self.populateCb()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Check your fields')
            msg.setInformativeText("Customer not deleted")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    # Worker
    def loadWorker(self):
        self.current = self.DB.getWorkerById(int(self.tw_worker.item(self.tw_worker.currentRow(),
                                                                     self.tw_worker.columnCount() - 1).text()))
        self.le_workerName.setText(self.current.name)
        self.le_workerUsername.setText(self.current.username)
        self.le_workerPhone.setText(str(self.current.phone))
        self.le_workerAddress.setText(str(self.current.address))
        self.le_workerScore.setText(str(self.current.score))
        self.l_workerPicture.setText(str(self.current.picture))
        self.btn_workerAdd.setEnabled(False)
        self.btn_workerEdit.setEnabled(True)
        self.btn_workerDelete.setEnabled(True)
        if self.current.id_category is not None and isinstance(self.current.id_category, int):
            self.cb_workerCategory.setCurrentIndex(
                self.categoryDictId[self.current.id_category])

    def addWorker(self):
        try:
            worker = Worker(self.le_workerName.text(), self.le_workerUsername.text(),
                            hashlib.sha3_512(
                                self.le_workerPassword.text().encode()).hexdigest(),
                            self.le_workerPhone.text(
            ), self.categoryDict[self.cb_workerCategory.currentIndex()],
                self.le_workerAddress.text(), float(self.le_workerScore.text()),
                self.l_workerPicture.text(), None)
            self.DB.insertWorker(worker)
            # clear all
            self.le_workerName.clear()
            self.le_workerUsername.clear()
            self.le_workerPassword.clear()
            self.le_workerPhone.clear()
            self.le_workerAddress.clear()
            self.le_workerScore.clear()
            self.l_workerPicture.clear()
            self.cb_workerCategory.setCurrentIndex(0)
            self.twDbHandler()
            self.populateCb()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Check your fields')
            msg.setInformativeText("Worker not added")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def editWorker(self):
        try:
            assert isinstance(self.current, Worker)
            self.current.name = self.le_workerName.text()
            self.current.username = self.le_workerUsername.text()
            self.current.password = hashlib.sha3_512(
                self.le_workerPassword.text().encode()).hexdigest()
            self.current.phone = self.le_workerPhone.text()
            self.current.id_category = self.categoryDict[self.cb_workerCategory.currentIndex(
            )]
            self.current.address = self.le_workerAddress.text()
            self.current.score = float(self.le_workerScore.text())
            self.current.picture = None
            self.current.face = None
            self.DB.updateWorker(self.current)
            # clear all
            self.le_workerName.clear()
            self.le_workerUsername.clear()
            self.le_workerPassword.clear()
            self.le_workerPhone.clear()
            self.le_workerAddress.clear()
            self.le_workerScore.clear()
            self.l_workerPicture.clear()
            self.cb_workerCategory.setCurrentIndex(0)
            self.btn_workerAdd.setEnabled(True)
            self.btn_workerEdit.setEnabled(False)
            self.btn_workerDelete.setEnabled(False)
            self.twDbHandler()
            self.populateCb()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Check your fields')
            msg.setInformativeText("Worker not updated")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def deleteWorker(self):
        try:
            assert isinstance(self.current, Worker)
            self.DB.deleteWorker(self.current.id)
            # clear all
            self.le_workerName.clear()
            self.le_workerUsername.clear()
            self.le_workerPassword.clear()
            self.le_workerPhone.clear()
            self.le_workerAddress.clear()
            self.le_workerScore.clear()
            self.l_workerPicture.clear()
            self.cb_workerCategory.setCurrentIndex(0)
            self.btn_workerAdd.setEnabled(True)
            self.btn_workerEdit.setEnabled(False)
            self.btn_workerDelete.setEnabled(False)
            self.twDbHandler()
            self.populateCb()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Check your fields')
            msg.setInformativeText("Worker not deleted")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    # Sell
    def loadSell(self):
        self.current = self.DB.getSellById(int(self.tw_sell.item(self.tw_sell.currentRow(), self.tw_sell.columnCount()
                                                                 - 1).text()))
        self.dte_sellDate.setDateTime(QDateTime.fromString(
            self.current.date, "yyyy-MM-dd HH:mm:ss"))
        self.le_sellTotal.setText(str(self.current.total))
        self.cb_sellIdWorker.setCurrentIndex(self.current.id_worker)
        self.cb_sellIdCustomer.setCurrentIndex(self.current.id_customer)
        self.btn_sellAdd.setEnabled(False)
        self.btn_sellEdit.setEnabled(True)
        self.btn_sellDelete.setEnabled(True)

    def addSell(self):
        try:
            sell = Sell(self.cb_sellIdWorker.currentIndex(), self.cb_sellIdCustomer.currentIndex(),
                        self.dte_sellDate.dateTime().toString("yyyy-MM-dd HH:mm:ss"), float(self.le_sellTotal.text()))
            self.DB.insertSell(sell)
            # clear all
            self.le_sellTotal.clear()
            self.cb_sellIdWorker.setCurrentIndex(0)
            self.cb_sellIdCustomer.setCurrentIndex(0)
            self.twDbHandler()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Check your fields')
            msg.setInformativeText("Sell not added")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def editSell(self):
        try:
            assert isinstance(self.current, Sell)
            self.current.id_worker = self.cb_sellIdWorker.currentIndex()
            self.current.id_customer = self.cb_sellIdCustomer.currentIndex()
            self.current.date = self.dte_sellDate.dateTime().toString("yyyy-MM-dd HH:mm:ss")
            self.current.total = float(self.le_sellTotal.text())
            self.DB.updateSell(self.current)
            # clear all
            self.le_sellTotal.clear()
            self.cb_sellIdWorker.setCurrentIndex(0)
            self.cb_sellIdCustomer.setCurrentIndex(0)
            self.btn_sellAdd.setEnabled(True)
            self.btn_sellEdit.setEnabled(False)
            self.btn_sellDelete.setEnabled(False)
            self.twDbHandler()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Check your fields')
            msg.setInformativeText("Sell not updated")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def deleteSell(self):
        try:
            assert isinstance(self.current, Sell)
            self.DB.deleteSell(self.current.id)
            self.DB.deleteAllRelatedSellItems(self.current.id)
            # clear all
            self.le_sellTotal.clear()
            self.cb_sellIdWorker.setCurrentIndex(0)
            self.cb_sellIdCustomer.setCurrentIndex(0)
            self.btn_sellAdd.setEnabled(True)
            self.btn_sellEdit.setEnabled(False)
            self.btn_sellDelete.setEnabled(False)
            self.twDbHandler()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Check your fields')
            msg.setInformativeText("Sell not deleted")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    # Table
    def loadTable(self):
        self.current = self.DB.getTableById(
            int(self.tw_table.item(self.tw_table.currentRow(), 0).text()))
        self.le_tableName.setText(self.current.name)
        self.le_tableId.setText(str(self.current.id))
        self.le_tableSeats.setText(str(self.current.seats))
        self.btn_tableAdd.setEnabled(False)
        self.btn_tableEdit.setEnabled(True)
        self.btn_tableDelete.setEnabled(True)

    def addTable(self):
        try:
            table = Table(int(self.le_tableId.text()), self.le_tableName.text(), int(
                self.le_tableSeats.text()))
            self.DB.insertTable(table)
            # clear all
            self.le_tableName.clear()
            self.le_tableId.clear()
            self.le_tableSeats.clear()
            self.twDbHandler()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Check your fields')
            msg.setInformativeText("Table not added")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def editTable(self):
        try:
            assert isinstance(self.current, Table)
            self.current.name = str(self.le_tableName.text())
            self.current.id = int(self.le_tableId.text())
            self.current.seats = int(self.le_tableSeats.text())
            # clear all
            self.le_tableName.clear()
            self.le_tableId.clear()
            self.le_tableSeats.clear()
            self.btn_tableAdd.setEnabled(True)
            self.btn_tableEdit.setEnabled(False)
            self.btn_tableDelete.setEnabled(False)
            self.DB.updateTable(self.current)
            self.twDbHandler()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Check your fields')
            msg.setInformativeText("Table not updated")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def deleteTable(self):
        try:
            assert isinstance(self.current, Table)
            self.DB.deleteTable(self.current.id)
            # clear all
            self.le_tableName.clear()
            self.le_tableId.clear()
            self.le_tableSeats.clear()
            self.btn_tableAdd.setEnabled(True)
            self.btn_tableEdit.setEnabled(False)
            self.btn_tableDelete.setEnabled(False)
            self.twDbHandler()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Check your fields')
            msg.setInformativeText("Table not deleted")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    # Category
    def loadCategory(self):
        self.current = self.DB.getCategoryById(int(self.tw_category.item(self.tw_category.currentRow(),
                                                                         self.tw_category.columnCount() - 1).text()))
        self.le_categoryName.setText(self.current.name)
        self.cb_categoryLevel.setCurrentIndex(self.current.level)
        self.btn_categoryAdd.setEnabled(False)
        self.btn_categoryEdit.setEnabled(True)
        self.btn_categoryDelete.setEnabled(True)

    def addCategory(self):
        try:
            category = Category(self.le_categoryName.text(),
                                self.cb_categoryLevel.currentIndex())
            self.DB.insertCategory(category)
            # clear all
            self.le_categoryName.clear()
            self.cb_categoryLevel.setCurrentIndex(0)
            self.twDbHandler()
            self.populateCb()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Check your fields')
            msg.setInformativeText("Worker category not added")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def editCategory(self):
        try:
            assert isinstance(self.current, Category)
            self.current.name = self.le_categoryName.text()
            self.current.level = self.cb_categoryLevel.currentIndex()
            self.current.id_worker = self.workerDict[self.cb_pointerIdWorker.currentIndex(
            )]
            # clear all
            self.le_categoryName.clear()
            self.cb_categoryLevel.setCurrentIndex(0)
            self.btn_categoryAdd.setEnabled(True)
            self.btn_categoryEdit.setEnabled(False)
            self.btn_categoryDelete.setEnabled(False)
            self.DB.updateCategory(self.current)
            self.twDbHandler()
            self.populateCb()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Check your fields')
            msg.setInformativeText("Worker category not updated")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def deleteCategory(self):
        try:
            assert isinstance(self.current, Category)
            self.DB.deleteCategory(self.current.id)
            # clear all
            self.le_categoryName.clear()
            self.cb_categoryLevel.setCurrentIndex(0)
            self.btn_categoryAdd.setEnabled(True)
            self.btn_categoryEdit.setEnabled(False)
            self.btn_categoryDelete.setEnabled(False)
            self.twDbHandler()
            self.populateCb()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Check your fields')
            msg.setInformativeText("Worker category not deleted")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    # Pointer
    def loadPointer(self):
        self.current = self.DB.getPointerById(int(self.tw_pointer.item(self.tw_pointer.currentRow(),
                                                                       self.tw_pointer.columnCount() - 1).text()))
        self.dte_pointerDateStart.setDateTime(QDateTime.fromString(
            self.current.date_start, "yyyy-MM-dd HH:mm:ss"))
        self.dte_pointerDateEnd.setDateTime(QDateTime.fromString(
            self.current.date_end, "yyyy-MM-dd HH:mm:ss"))
        self.cb_pointerIdWorker.setCurrentIndex(
            self.workerDict[self.current.id_worker])
        self.btn_pointerAdd.setEnabled(False)
        self.btn_pointerEdit.setEnabled(True)
        self.btn_pointerDelete.setEnabled(True)

    def addPointer(self):
        try:
            pointer = Pointer(self.dte_pointerDateStart.dateTime().toString("yyyy-MM-dd HH:mm:ss"),
                              self.dte_pointerDateEnd.dateTime().toString("yyyy-MM-dd HH:mm:ss"),
                              self.workerDict[self.cb_pointerIdWorker.currentIndex()])
            self.DB.insertPointer(pointer)
            # clear all
            self.cb_pointerIdWorker.setCurrentIndex(0)
            self.twDbHandler()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Check your fields')
            msg.setInformativeText("Pointer not added")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def editPointer(self):
        try:
            assert isinstance(self.current, Pointer)
            self.current.date_start = self.dte_pointerDateStart.dateTime().toString(
                "yyyy-MM-dd HH:mm:ss")
            self.current.date_end = self.dte_pointerDateEnd.dateTime().toString(
                "yyyy-MM-dd HH:mm:ss")
            self.current.id_worker = self.workerDict[self.cb_pointerIdWorker.currentIndex(
            )]
            # clear all
            self.cb_pointerIdWorker.setCurrentIndex(0)
            self.btn_pointerAdd.setEnabled(True)
            self.btn_pointerEdit.setEnabled(False)
            self.btn_pointerDelete.setEnabled(False)
            self.DB.updatePointer(self.current)
            self.twDbHandler()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Check your fields')
            msg.setInformativeText("Pointer not updated")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def deletePointer(self):
        try:
            assert isinstance(self.current, Pointer)
            self.DB.deletePointer(self.current.id)
            # clear all
            self.cb_pointerIdWorker.setCurrentIndex(0)
            self.btn_pointerAdd.setEnabled(True)
            self.btn_pointerEdit.setEnabled(False)
            self.btn_pointerDelete.setEnabled(False)
            self.twDbHandler()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Check your fields')
            msg.setInformativeText("Pointer not deleted")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    """Tables"""

    def clearAllTables(self):
        for b in self.w_tables.findChildren(QPushButton):
            b.deleteLater()

    def populateTables(self):
        self.clearAllTables()
        all_tables = self.DB.getAllTables()
        for table in all_tables:
            table_button = QPushButton(parent=self.w_tables, text=table.name)
            table_button.setObjectName(f"{table.id}")
            table_button.setMinimumSize(200, 200)
            table_button.setSizePolicy(
                QSizePolicy.Preferred, QSizePolicy.Preferred)
            if table.id_sell is not None:
                table_button.setStyleSheet('color: rgb(165, 0, 0);')
            else:
                table_button.setStyleSheet('color: rgb(20, 150, 0);')
            self.w_tables.layout().addWidget(table_button)
            table_button.clicked.connect(
                partial(self.loadTableContent, table_button.objectName()))

    def loadTableContent(self, table_id):
        self.clearCashRegister()
        self.sw_content.setCurrentIndex(3)
        self.rb_onTable.setChecked(True)
        try:
            self.currentOrder, total = self.DB.getTableContent(table_id)
            displayDbData(self.tw_orderList, self.currentOrder)
            self.current_table = table_id
            self.lcdN_totalHtt.setProperty("value", total)
            self.lcdN_tax.setProperty("value", total * self.tax)
            self.lcdN_totalTtc.setProperty("value", total + (total * self.tax))
        except Exception as e:
            self.current_table = table_id
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText('Table empty')
            msg.setInformativeText(
                "This is an empty table you should use the phone app")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    """Cash Register"""

    def clearAllProducts(self):
        parents = [self.w_salade, self.w_meal, self.w_pizza, self.w_hotDrink, self.w_hotDrink, self.w_coldDrink,
                   self.w_dessert]
        for parent in parents:
            for child in parent.findChildren(QFrame):
                child.deleteLater()

    def populateProducts(self):
        self.clearAllProducts()
        all_finish_product = self.DB.getAllFinishProducts()
        for finish_product in all_finish_product:
            if finish_product.category == "Salade":
                parent = self.w_salade
            elif finish_product.category == "Meal":
                parent = self.w_meal
            elif finish_product.category == "Pizza":
                parent = self.w_pizza
            elif finish_product.category == "Hot Drink":
                parent = self.w_hotDrink
            elif finish_product.category == "Cold Drink":
                parent = self.w_coldDrink
            else:
                parent = self.w_dessert
            parent.layout().addWidget(createProductContainer(parent=parent, product=finish_product,
                                                             table_id=self.current_table, fc=self.addOrderItem))

    def addOrderItem(self, order_item):
        tag = True
        order_item = copy.deepcopy(order_item)
        order_item.tableId = self.current_table
        total = 0
        for order in self.currentOrder:
            if order_item.productId == order.productId:
                tag = False
                order.orderItemQuantity += order_item.orderItemQuantity
                order.orderItemTotal += order_item.orderItemTotal
                total += order.orderItemTotal
                if order.orderItemQuantity == 0:
                    self.currentOrder.remove(order)
        if tag and order_item.orderItemQuantity > 0:
            total += order_item.orderItemTotal
            self.currentOrder.append(order_item)
        displayDbData(self.tw_orderList, self.currentOrder)
        self.lcdN_totalHtt.setProperty("value", total)
        self.lcdN_tax.setProperty("value", total * self.tax)
        self.lcdN_totalTtc.setProperty("value", total + (total * self.tax))

    def clearCashRegister(self):
        self.tw_orderList.clear()
        self.tw_orderList.setRowCount(0)
        self.tw_orderList.setColumnCount(0)
        self.cb_orderCustomer.setCurrentIndex(0)
        self.rb_takeAway.setChecked(True)
        self.currentOrder = []
        self.current_table = None
        self.lcdN_totalHtt.setProperty("value", 0)
        self.lcdN_tax.setProperty("value", 0)
        self.lcdN_totalTtc.setProperty("value", 0)

    def pay(self):
        try:
            assert len(self.currentOrder) > 0
            total = 0
            for order in self.currentOrder:
                total += order.orderItemTotal
            printTicket(self.currentWorker.name, self.currentOrder, self.tax)
            pay_dialog = Pay(total)
            pay_dialog.show()
            rsp = pay_dialog.exec_()
            if rsp:
                if self.current_table is not None:
                    table = self.DB.getTableById(self.current_table)
                    table.id_sell = None
                    self.DB.updateTable(table)
                    print("table updated")
                if self.currentSell is not None:
                    print("old")
                    self.currentSell.completed = 1
                    self.currentSell.id_customer = self.customerDict[self.cb_orderCustomer.currentIndex(
                    )]
                    self.DB.updateSell(self.currentSell)
                else:
                    print("new")
                    self.DB.insertOrder(self.currentOrder, total, self.currentWorker.id,
                                        self.customerDict[self.cb_orderCustomer.currentIndex()], 1)
                self.clearCashRegister()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('No items to pay')
            msg.setInformativeText("The list of items is empty")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def holdOrder(self):
        try:
            assert len(self.currentOrder)
            self.DB.insertOrder(self.currentOrder, float(self.lcdN_totalHtt.property("value")),
                                self.currentWorker.id, self.customerDict[self.cb_orderCustomer.currentIndex()])
            self.clearCashRegister()
            self.currentOrder = []
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Nothing to holding!')
            msg.setInformativeText("Please fill the order in order to hold it")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def resumeOrder(self):
        try:
            hold_dialog = Holder()
            hold_dialog.show()
            rsp = hold_dialog.exec_()
            if rsp:
                self.clearCashRegister()
                self.currentSell = self.DB.getSellById(rsp)
                self.currentOrder, total = self.DB.getUncompletedOrdersBySellId(
                    rsp)
                displayDbData(self.tw_orderList, self.currentOrder)
                self.lcdN_totalHtt.setProperty("value", total)
                self.lcdN_tax.setProperty("value", total * self.tax)
                self.lcdN_totalTtc.setProperty(
                    "value", total + (total * self.tax))
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('No holding order !')
            msg.setInformativeText(
                "The holding order list is empty nothing to resume")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    """Utility functions"""

    def updateInfo(self, nb_free_tables, nb_busy_tables, nb_month_sells, nb_day_sells):
        self.l_freeTables.setText(f"Free tables: {nb_free_tables}")
        self.l_busyTables.setText(f"Busy tables: {nb_busy_tables}")
        self.l_monthSells.setText(
            f"Number of sells this month: {nb_month_sells}")
        self.l_daySells.setText(f"Number of sells today: {nb_day_sells}")

    def login(self):
        worker = self.DB.getWorkerByUsername(self.le_username.text())
        if isinstance(worker, Worker) and \
                hashlib.sha3_512(self.le_password.text().encode()).hexdigest() == worker.password and \
                isinstance(worker.id_category, int):
            self.le_username.clear()
            level = self.DB.getCategoryById(worker.id_category).level
            self.btn_logInOut.setEnabled(False)
            self.btn_tables.setEnabled(True)
            self.btn_exit.setEnabled(True)
            if level <= 1:
                self.btn_database.setEnabled(True)
            if level <= 2:
                self.btn_cashRegister.setEnabled(True)
            self.currentWorker = worker
            self.currentPointer = Pointer(date_start=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                          date_end=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                          id_worker=self.currentWorker.id)
            self.btn_tables.click()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText('Check your fields')
            msg.setInformativeText("Username or password not correct")
            msg.setWindowTitle("Warning message")
            msg.exec_()
        self.le_password.clear()

    def logout(self):
        self.sw_content.setCurrentIndex(0)
        self.homeScreen()
        self.btn_tables.setEnabled(False)
        self.btn_cashRegister.setEnabled(False)
        self.btn_database.setEnabled(False)
        self.btn_exit.setEnabled(False)
        self.btn_logInOut.setEnabled(True)
        if self.currentPointer is not None:
            self.currentPointer.date_end = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.DB.insertPointer(self.currentPointer)

    def changeSettings(self):
        try:
            setting = SettingUI()
            setting.show()
            rsp = setting.exec_()
            if rsp:
                print(f"restart server with new settings...")
                if self.serverThread is not None:
                    self.serverThread.stop()
                self.serverThread = ServerThread()
                self.serverThread.start()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('No settings !')
            msg.setInformativeText(
                "The setting file is missing")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    # On close work

    def closeEvent(self, event):
        self.sw_content.setCurrentIndex(1)
        if self.currentPointer is not None:
            self.currentPointer.date_end = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.DB.insertPointer(self.currentPointer)
        if self.serverThread is not None:
            self.serverThread.stop()
        if self.infoThread is not None:
            self.infoThread.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PatusMainUI()
    sys.exit(app.exec_())
