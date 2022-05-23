import logging

from Utilities.UiUtilities import *
from DB.DBHandler import DBHelper
from Utilities import Utility
from DB.DbTables import *
from Utilities.Threads import *
from Utilities.LicenseChecker import *
from Utilities.DashBoardShow import DashBoard
from resource import resource_rc
from Utilities import Threads

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from functools import partial
from PyQt5 import uic
import threading
import datetime
import hashlib
import time
import copy
import sys
import os


class PatusMainUI(QMainWindow):
    def __init__(self, **kwargs):
        super(PatusMainUI, self).__init__(**kwargs)
        uic.loadUi(os.path.join(os.getcwd(), "uis", "PatusInterface.ui"), self)
        self.tables_settings = QSettings("Patus", "Tables")
        self.DB = DBHelper()
        self.sw_content.setCurrentIndex(0)
        self.infoThread = None
        self.serverThread = None
        self.printerThread = None
        # db current item selected
        self.currentPointer = None
        self.currentSell = None
        self.currentWorker = None
        self.currentWorkerCat = None
        self.current = None
        self.current_table = None
        self.currentNbCovers = 1
        self.currentOrder = []
        self.tax = 0.0
        self.fileDescription = None
        (
            self.categoryDict,
            self.workerDict,
            self.customerDict,
            self.menuItemNameDict,
            self.expenseCategoryNameDict,
            self.supplierNameDict,
            self.menuCustomCategoryNameDict,
            self.ingredientItemNameDict,
            self.tableDict,
        ) = ({}, {}, {}, {}, {}, {}, {}, {}, {})
        (
            self.categoryDictId,
            self.workerDictId,
            self.customerDictId,
            self.menuItemNameDictId,
            self.expenseCategoryNameDictId,
            self.supplierNameDictId,
            self.menuCustomCategoryNameDictId,
            self.ingredientItemDictId,
            self.tableDictId,
        ) = ({}, {}, {}, {}, {}, {}, {}, {}, {})
        self.prepareLogFile()
        self.check_me(load_current_license())

        self.infoThread = InfoThread()
        try:
            self.serverThread = ServerThread()
            self.serverThread.addClient.connect(self.addClientDashboard)
            self.serverThread.removeClient.connect(self.removeClientDashboard)
            self.serverThread.logUpdater.connect(self.callLog)
            # self.serverThread.logUpdater.connect(print)
            self.serverThread.tablesUpdated.connect(self.populateTables)
            self.serverThread.updateServerStatus.connect(self.updateServerStatus)
            self.serverThread.printerCall.connect(self.printerCall)
            self.serverThread.notificationCall.connect(self.notifySelf)
        except Exception as e:
            logging.error(f"Server not running --> {e}")
            self.serverThread = None

        # Notifications
        self.btn_notification_clear.clicked.connect(self.clearAllNotifications)
        self.btn_notification.clicked.connect(self.showHideNotification)
        self.f_notification.setVisible(False)

        # Side panel menu
        self.btn_sideBar.clicked.connect(self.showHideSideBar)

        self.btn_logInOut.clicked.connect(lambda: self.sw_content.setCurrentIndex(1))
        self.btn_tables.clicked.connect(lambda: self.sw_content.setCurrentIndex(2))
        self.btn_tables.clicked.connect(self.populateTables)
        self.btn_cashRegister.clicked.connect(
            lambda: self.sw_content.setCurrentIndex(3)
        )
        self.btn_reservation.clicked.connect(lambda: self.sw_content.setCurrentIndex(4))
        self.btn_waste.clicked.connect(lambda: self.sw_content.setCurrentIndex(5))
        self.btn_databaseOverview.clicked.connect(
            lambda: self.sw_content.setCurrentIndex(6)
        )
        self.btn_productReceipt.clicked.connect(
            lambda: self.sw_content.setCurrentIndex(7)
        )
        self.btn_database.clicked.connect(lambda: self.sw_content.setCurrentIndex(8))
        self.btn_workerStatus.clicked.connect(
            lambda: self.sw_content.setCurrentIndex(9)
        )
        self.btn_statistic.clicked.connect(lambda: self.sw_content.setCurrentIndex(10))

        self.btn_database.clicked.connect(self.twDbHandler)
        self.btn_exit.clicked.connect(self.logout)
        self.btn_databaseOverview.clicked.connect(self.loadStock)
        self.btn_waste.clicked.connect(self.loadStock)
        self.btn_waste.clicked.connect(self.showWasteHistory)
        self.btn_reservation.clicked.connect(self.showTablesReservation)
        self.btn_reservation.clicked.connect(self.showReservation)
        self.btn_productReceipt.clicked.connect(self.loadMenuItemReceiptIngredients)

        # Login Window
        self.btn_loginConfirm.clicked.connect(self.login)

        # Tables window
        self.w_tables = CustomTablesWidget()
        self.page_tables.layout().addWidget(self.w_tables)

        # DashBoard window
        self.DashBoard = DashBoard()
        self.page_stats.layout().addWidget(self.DashBoard)

        # Cash Register Window
        self.populateMenu()
        self.btn_cashRegisterPay.clicked.connect(self.pay)
        self.btn_cashRegisterClear.clicked.connect(self.clearCashRegister)
        self.btn_cashRegisterDeleteCurrent.clicked.connect(self.deleteCurrent)
        self.btn_cashRegisterHold.clicked.connect(self.holdOrder)
        self.btn_cashRegisterResume.clicked.connect(self.resumeOrder)
        self.btn_cashRegisterChangeTable.clicked.connect(self.changeTable)
        self.tw_orderList.doubleClicked.connect(self.editOnFly)
        self.btn_cashRegisterTicket.clicked.connect(
            lambda: self.cashRegisterPrintFunction("Receipt", True)
        )
        self.btn_cashRegisterTicketKitchen.clicked.connect(
            lambda: self.cashRegisterPrintFunction("Kitchen", True)
        )
        # Database Window
        self.tw_database.currentChanged.connect(self.twDbHandler)
        self.populateCb()
        # Menu Item
        self.btn_menuItemAdd.clicked.connect(self.addMenuItem)
        self.btn_menuItemEdit.clicked.connect(self.editMenuItem)
        self.btn_menuItemDelete.clicked.connect(self.deleteMenuItem)
        self.btn_menuItemClear.clicked.connect(
            lambda: self.btn_menuItemAdd.setEnabled(True)
        )
        self.btn_menuItemClear.clicked.connect(
            lambda: self.btn_menuItemEdit.setEnabled(False)
        )
        self.btn_menuItemClear.clicked.connect(
            lambda: self.btn_menuItemDelete.setEnabled(False)
        )
        self.btn_menuItemClear.clicked.connect(lambda: self.le_menuItemName.clear())
        self.btn_menuItemClear.clicked.connect(lambda: self.le_menuItemUnit.clear())
        self.btn_menuItemClear.clicked.connect(
            lambda: self.le_menuItemUnitQuantity.clear()
        )
        self.btn_menuItemClear.clicked.connect(lambda: self.le_menuItemPrice.clear())
        self.btn_menuItemClear.clicked.connect(lambda: self.l_menuItemPicture.clear())
        self.btn_menuItemClear.clicked.connect(
            lambda: self.cb_menuItemCategory.setCurrentIndex(0)
        )
        self.btn_menuItemPictureClear.clicked.connect(
            lambda: self.l_menuItemPicture.clear()
        )
        self.btn_menuItemPicture.clicked.connect(
            lambda: self.pictureSelector(self.l_menuItemPicture)
        )
        self.tw_menuItem.doubleClicked.connect(self.loadMenuItem)
        self.le_menuItemPrice.setValidator(QDoubleValidator())
        self.le_menuItemUnitQuantity.setValidator(QDoubleValidator())
        self.menuItemDict = {
            "Salade": 0,
            "Meal": 1,
            "Pizza": 2,
            "Cold Drink": 3,
            "Hot Drink": 4,
            "Dessert": 5,
        }
        # Menu Custom Category
        self.btn_menuCategoryCustomAdd.clicked.connect(self.addMenuCategoryCustom)
        self.btn_menuCategoryCustomEdit.clicked.connect(self.editMenuCategoryCustom)
        self.btn_menuCategoryCustomDelete.clicked.connect(self.deleteMenuCategoryCustom)
        self.btn_menuCategoryCustomClear.clicked.connect(
            lambda: self.btn_menuCategoryCustomAdd.setEnabled(True)
        )
        self.btn_menuCategoryCustomClear.clicked.connect(
            lambda: self.btn_menuCategoryCustomEdit.setEnabled(False)
        )
        self.btn_menuCategoryCustomClear.clicked.connect(
            lambda: self.btn_menuCategoryCustomDelete.setEnabled(False)
        )
        self.btn_menuCategoryCustomClear.clicked.connect(
            lambda: self.le_menuCategoryCustomName.clear()
        )
        self.btn_menuCategoryCustomClear.clicked.connect(
            lambda: self.cb_menuCategoryCustomPrinting.setCurrentIndex(0)
        )
        self.tw_menuCategoryCustom.doubleClicked.connect(self.loadMenuCategoryCustom)
        # Supplement
        self.btn_supplementAdd.clicked.connect(self.addSupplement)
        self.btn_supplementEdit.clicked.connect(self.editSupplement)
        self.btn_supplementDelete.clicked.connect(self.deleteSupplement)
        self.btn_supplementClear.clicked.connect(
            lambda: self.btn_supplementAdd.setEnabled(True)
        )
        self.btn_supplementClear.clicked.connect(
            lambda: self.btn_supplementEdit.setEnabled(False)
        )
        self.btn_supplementClear.clicked.connect(
            lambda: self.btn_supplementDelete.setEnabled(False)
        )
        self.btn_supplementClear.clicked.connect(lambda: self.le_supplementName.clear())
        self.btn_supplementClear.clicked.connect(
            lambda: self.le_supplementQuantity.clear()
        )
        self.btn_supplementClear.clicked.connect(
            lambda: self.le_supplementPrice.clear()
        )
        self.btn_supplementClear.clicked.connect(
            lambda: self.cb_supplementProduct.setCurrentIndex(0)
        )
        self.tw_supplement.doubleClicked.connect(self.loadSupplement)
        self.le_supplementQuantity.setValidator(QDoubleValidator())
        self.le_supplementPrice.setValidator(QDoubleValidator())
        # Expense
        self.expenseSetUp()
        self.btn_expenseAdd.clicked.connect(self.addExpense)
        self.btn_expenseEdit.clicked.connect(self.editExpense)
        self.btn_expenseDelete.clicked.connect(self.deleteExpense)
        self.btn_expenseClear.clicked.connect(
            lambda: self.btn_expenseAdd.setEnabled(True)
        )
        self.btn_expenseClear.clicked.connect(
            lambda: self.btn_expenseEdit.setEnabled(False)
        )
        self.btn_expenseClear.clicked.connect(
            lambda: self.btn_expenseDelete.setEnabled(False)
        )
        self.btn_expenseClear.clicked.connect(
            lambda: self.cb_expensePayed.setChecked(True)
        )
        self.btn_expenseClear.clicked.connect(lambda: self.le_expenseName.clear())
        self.btn_expenseClear.clicked.connect(lambda: self.le_expenseQuantity.clear())
        self.btn_expenseClear.clicked.connect(lambda: self.le_expensePrice.clear())
        self.btn_expenseClear.clicked.connect(
            lambda: self.cb_expenseCategory.setCurrentIndex(0)
        )
        self.tw_expense.doubleClicked.connect(self.loadExpense)
        self.le_expenseQuantity.setValidator(QDoubleValidator())
        # self.le_expensePrice.setValidator(QDoubleValidator())
        # Expense Category
        self.btn_expenseCategoryAdd.clicked.connect(self.addExpenseCategory)
        self.btn_expenseCategoryEdit.clicked.connect(self.editExpenseCategory)
        self.btn_expenseCategoryDelete.clicked.connect(self.deleteExpenseCategory)
        self.btn_expenseCategoryClear.clicked.connect(
            lambda: self.btn_expenseCategoryAdd.setEnabled(True)
        )
        self.btn_expenseCategoryClear.clicked.connect(
            lambda: self.btn_expenseCategoryEdit.setEnabled(False)
        )
        self.btn_expenseCategoryClear.clicked.connect(
            lambda: self.btn_expenseCategoryDelete.setEnabled(False)
        )
        self.btn_expenseCategoryClear.clicked.connect(
            lambda: self.le_expenseCategoryName.clear()
        )
        self.btn_expenseCategoryClear.clicked.connect(
            lambda: self.cb_expenseCategorySaveToStock.setChecked(True)
        )
        self.btn_expenseCategoryClear.clicked.connect(
            lambda: self.cb_expenseCategoryIsIngredient.setChecked(True)
        )
        self.tw_expenseCategory.doubleClicked.connect(self.loadExpenseCategory)
        # Supplier
        self.btn_supplierAdd.clicked.connect(self.addSupplier)
        self.btn_supplierEdit.clicked.connect(self.editSupplier)
        self.btn_supplierDelete.clicked.connect(self.deleteSupplier)
        self.btn_supplierClear.clicked.connect(
            lambda: self.btn_supplierAdd.setEnabled(True)
        )
        self.btn_supplierClear.clicked.connect(
            lambda: self.btn_supplierEdit.setEnabled(False)
        )
        self.btn_supplierClear.clicked.connect(
            lambda: self.btn_supplierDelete.setEnabled(False)
        )
        self.btn_supplierClear.clicked.connect(lambda: self.le_supplierName.clear())
        self.btn_supplierClear.clicked.connect(lambda: self.le_supplierPhone.clear())
        self.btn_supplierClear.clicked.connect(lambda: self.le_supplierAddress.clear())
        self.btn_supplierClear.clicked.connect(lambda: self.le_supplierMail.clear())
        self.tw_supplier.doubleClicked.connect(self.loadSupplier)
        # Customer
        self.btn_customerAdd.clicked.connect(self.addCustomer)
        self.btn_customerEdit.clicked.connect(self.editCustomer)
        self.btn_customerDelete.clicked.connect(self.deleteCustomer)
        self.btn_customerClear.clicked.connect(
            lambda: self.btn_customerAdd.setEnabled(True)
        )
        self.btn_customerClear.clicked.connect(
            lambda: self.btn_customerEdit.setEnabled(False)
        )
        self.btn_customerClear.clicked.connect(
            lambda: self.btn_customerDelete.setEnabled(False)
        )
        self.btn_customerClear.clicked.connect(lambda: self.le_customerName.clear())
        self.btn_customerClear.clicked.connect(lambda: self.le_customerPhone.clear())
        self.btn_customerClear.clicked.connect(lambda: self.le_customerAddress.clear())
        self.btn_customerClear.clicked.connect(lambda: self.l_customerPicture.clear())
        self.btn_customerClear.clicked.connect(lambda: self.le_customerScore.clear())
        self.btn_customerPictureClear.clicked.connect(
            lambda: self.l_customerPicture.clear()
        )
        self.btn_customerPicture.clicked.connect(
            lambda: self.pictureSelector(self.l_customerPicture)
        )
        self.tw_customer.doubleClicked.connect(self.loadCustomer)
        self.le_customerScore.setValidator(QDoubleValidator())
        # Worker
        self.btn_workerAdd.clicked.connect(self.addWorker)
        self.btn_workerEdit.clicked.connect(self.editWorker)
        self.btn_workerDelete.clicked.connect(self.deleteWorker)
        self.btn_workerAddCv.clicked.connect(
            lambda: self.fileSelector(self.le_workerCv)
        )
        self.btn_workerClearCv.clicked.connect(
            lambda: self.clearFileDescription(self.le_workerCv)
        )
        self.btn_workerOpenCv.clicked.connect(
            lambda: Utility.loadConvertOpenFile(self.fileDescription)
        )
        self.btn_workerClear.clicked.connect(
            lambda: self.btn_workerAdd.setEnabled(True)
        )
        self.btn_workerClear.clicked.connect(
            lambda: self.btn_workerEdit.setEnabled(False)
        )
        self.btn_workerClear.clicked.connect(
            lambda: self.btn_workerDelete.setEnabled(False)
        )
        self.btn_workerClear.clicked.connect(self.clearFileDescription)
        self.btn_workerClear.clicked.connect(lambda: self.le_workerCv.clear())
        self.btn_workerClear.clicked.connect(lambda: self.le_workerName.clear())
        self.btn_workerClear.clicked.connect(lambda: self.le_workerUsername.clear())
        self.btn_workerClear.clicked.connect(lambda: self.le_workerPassword.clear())
        self.btn_workerClear.clicked.connect(lambda: self.le_workerPhone.clear())
        self.btn_workerClear.clicked.connect(lambda: self.le_workerAddress.clear())
        self.btn_workerClear.clicked.connect(lambda: self.l_workerPicture.clear())
        self.btn_workerClear.clicked.connect(lambda: self.le_workerSalary.clear())
        self.btn_workerClear.clicked.connect(lambda: self.le_workerScore.clear())
        self.btn_workerClear.clicked.connect(
            lambda: self.cb_workerCategory.setCurrentIndex(0)
        )
        self.btn_workerPictureClear.clicked.connect(
            lambda: self.l_workerPicture.clear()
        )
        self.btn_workerPicture.clicked.connect(
            lambda: self.pictureSelector(self.l_workerPicture)
        )
        self.tw_worker.doubleClicked.connect(self.loadWorker)
        self.le_workerSalary.setValidator(QDoubleValidator())
        self.le_workerScore.setValidator(QDoubleValidator())
        # Sell
        self.btn_sellAdd.clicked.connect(self.addSell)
        self.btn_sellEdit.clicked.connect(self.editSell)
        self.btn_sellDelete.clicked.connect(self.deleteSell)
        self.btn_sellShow.clicked.connect(self.showSell)
        self.btn_sellLoad.clicked.connect(self.loadOrder)
        self.btn_sellClear.clicked.connect(lambda: self.btn_sellShow.setEnabled(False))
        self.btn_sellClear.clicked.connect(lambda: self.btn_sellLoad.setEnabled(False))
        self.btn_sellClear.clicked.connect(lambda: self.btn_sellAdd.setEnabled(True))
        self.btn_sellClear.clicked.connect(lambda: self.btn_sellEdit.setEnabled(False))
        self.btn_sellClear.clicked.connect(
            lambda: self.btn_sellDelete.setEnabled(False)
        )
        self.btn_sellClear.clicked.connect(lambda: self.le_sellTotal.clear())
        self.btn_sellClear.clicked.connect(lambda: self.le_sellNbCovers.clear())
        self.btn_sellClear.clicked.connect(
            lambda: self.cb_sellIdWorker.setCurrentIndex(0)
        )
        self.btn_sellClear.clicked.connect(
            lambda: self.cb_sellIdCustomer.setCurrentIndex(0)
        )
        self.btn_sellClear.clicked.connect(
            lambda: self.dte_sellDate.setDateTime(QDateTime(datetime.datetime.now()))
        )
        self.tw_sell.doubleClicked.connect(self.loadSell)
        self.le_sellTotal.setValidator(QDoubleValidator())
        self.le_sellNbCovers.setValidator(QIntValidator())
        # Table
        self.btn_tableAdd.clicked.connect(self.addTable)
        self.btn_tableEdit.clicked.connect(self.editTable)
        self.btn_tableDelete.clicked.connect(self.deleteTable)
        self.btn_tableClear.clicked.connect(lambda: self.btn_tableAdd.setEnabled(True))
        self.btn_tableClear.clicked.connect(
            lambda: self.btn_tableEdit.setEnabled(False)
        )
        self.btn_tableClear.clicked.connect(
            lambda: self.btn_tableDelete.setEnabled(False)
        )
        self.btn_tableClear.clicked.connect(lambda: self.le_tableName.clear())
        self.btn_tableClear.clicked.connect(lambda: self.le_tableId.clear())
        self.btn_tableClear.clicked.connect(lambda: self.le_tableSeats.clear())
        self.btn_tableClear.clicked.connect(lambda: self.le_tableComment.clear())
        self.tw_table.doubleClicked.connect(self.loadTable)
        self.le_tableId.setValidator(QIntValidator())
        self.le_tableSeats.setValidator(QIntValidator())
        # Category
        self.btn_categoryAdd.clicked.connect(self.addCategory)
        self.btn_categoryEdit.clicked.connect(self.editCategory)
        self.btn_categoryDelete.clicked.connect(self.deleteCategory)
        self.btn_categoryClear.clicked.connect(
            lambda: self.btn_categoryAdd.setEnabled(True)
        )
        self.btn_categoryClear.clicked.connect(
            lambda: self.btn_categoryEdit.setEnabled(False)
        )
        self.btn_categoryClear.clicked.connect(
            lambda: self.btn_categoryDelete.setEnabled(False)
        )
        self.btn_categoryClear.clicked.connect(self.clearCategory)
        self.tw_category.doubleClicked.connect(self.loadCategory)
        # Stock
        self.btn_stockAdd.clicked.connect(self.addStockDB)
        self.btn_stockEdit.clicked.connect(self.editStockDB)
        self.btn_stockDelete.clicked.connect(self.deleteStockDB)
        self.btn_stockClear.clicked.connect(self.clearStockDB)
        self.tw_stockDb.doubleClicked.connect(self.loadStockDB)

        # TableOwnership
        self.btn_tableOwnershipAdd.clicked.connect(self.addTableOwnershipDb)
        self.btn_tableOwnershipEdit.clicked.connect(self.editTableOwnershipDb)
        self.btn_tableOwnershipDelete.clicked.connect(self.deleteTableOwnershipDb)
        self.btn_tableOwnershipClear.clicked.connect(self.clearTableOwnershipDb)
        self.tw_tableOwnershipDb.doubleClicked.connect(self.loadTableOwnershipDb)

        # DocFile
        self.btn_docClearFile.clicked.connect(
            lambda: self.clearFileDescription(self.le_docPath)
        )
        self.btn_docAddFile.clicked.connect(lambda: self.fileSelector(self.le_docPath))
        self.btn_docOpenFile.clicked.connect(
            lambda: Utility.loadConvertOpenFile(self.fileDescription)
        )
        self.btn_docAdd.clicked.connect(self.addFileDocDb)
        self.btn_docEdit.clicked.connect(self.editFileDocDb)
        self.btn_docDelete.clicked.connect(self.deleteFileDocDb)
        self.btn_docClear.clicked.connect(self.clearFileDocDb)
        self.tw_documentDb.doubleClicked.connect(self.loadFileDocDb)

        # Payment
        self.btn_paymentAdd.clicked.connect(self.addPaymentDb)
        self.btn_paymentEdit.clicked.connect(self.editPaymentDb)
        self.btn_paymentDelete.clicked.connect(self.deletePaymentDb)
        self.btn_paymentClear.clicked.connect(self.clearPaymentDb)
        self.tw_paymentDb.doubleClicked.connect(self.loadPaymentDb)
        self.le_payment_amount.setValidator(QDoubleValidator())

        # Waste Window
        # Waste Stock
        self.btn_wasteStockSave.clicked.connect(self.addWasteStock)
        self.btn_wasteStockClear.clicked.connect(
            lambda: self.le_wasteStockQuantity.clear()
        )
        self.btn_wasteStockClear.clicked.connect(
            lambda: self.cb_wasteStockWorkerId.setCurrentIndex(0)
        )
        # self.btn_wasteStockClear.clicked.connect(
        #     lambda: self.tw_wasteStock.setCurrentRow(0))
        self.le_wasteStockQuantity.setValidator(QDoubleValidator())
        # Waste Custom
        self.btn_wasteCustomSave.clicked.connect(self.addWasteCustom)
        self.btn_wasteCustomClear.clicked.connect(
            lambda: self.le_wasteCustomName.clear()
        )
        self.btn_wasteCustomClear.clicked.connect(
            lambda: self.le_wasteCustomQuantity.clear()
        )
        self.btn_wasteCustomClear.clicked.connect(
            lambda: self.le_wasteCustomPrice.clear()
        )
        self.btn_wasteCustomClear.clicked.connect(
            lambda: self.cb_wasteCustomWorkerId.setCurrentIndex(0)
        )
        self.btn_wasteCustomClear.clicked.connect(
            lambda: self.cb_wasteCustomCategory.setCurrentIndex(0)
        )
        self.le_wasteCustomQuantity.setValidator(QDoubleValidator())
        self.le_wasteCustomPrice.setValidator(QDoubleValidator())

        # Reservation Window
        # Reservation
        self.btn_reservationAdd.clicked.connect(self.addReservation)
        self.btn_reservationEdit.clicked.connect(self.editReservation)
        self.btn_reservationDelete.clicked.connect(self.deleteReservation)
        self.btn_reservationClear.clicked.connect(
            lambda: self.btn_reservationAdd.setEnabled(True)
        )
        self.btn_reservationClear.clicked.connect(
            lambda: self.btn_reservationEdit.setEnabled(False)
        )
        self.btn_reservationClear.clicked.connect(
            lambda: self.btn_reservationDelete.setEnabled(False)
        )
        self.btn_reservationClear.clicked.connect(
            lambda: self.le_reservationName.clear()
        )
        self.btn_reservationClear.clicked.connect(
            lambda: self.le_reservationPhone.clear()
        )
        self.btn_reservationClear.clicked.connect(
            lambda: self.le_reservationNbPerson.clear()
        )
        self.btn_reservationClear.clicked.connect(self.showReservation)
        self.btn_reservationClear.clicked.connect(
            lambda: self.dte_reservation.setDateTime(QDateTime(datetime.datetime.now()))
        )
        self.cb_reservationDate.clicked.connect(self.searchReservation)
        self.de_reservationSearchDate.dateTimeChanged.connect(self.searchReservation)
        self.tw_reservation.doubleClicked.connect(self.loadReservation)
        self.btn_reservationSearch.clicked.connect(self.searchReservation)
        self.dte_reservation.dateTimeChanged.connect(self.showTablesReservation)
        self.le_reservationNbPerson.setValidator(QIntValidator())
        self.le_reservationPhone.setValidator(
            QRegExpValidator(
                QRegExp("^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$")
            )
        )

        # Menu item receipt Window
        # Menu item Receipts
        self.btn_productReceiptAdd.clicked.connect(self.addMenuItemReceiptIngredient)
        self.btn_productReceiptEdit.clicked.connect(self.editMenuItemReceiptIngredient)
        self.btn_productReceiptRemove.clicked.connect(
            self.deleteMenuItemReceiptIngredient
        )
        self.btn_productReceiptClear.clicked.connect(
            lambda: self.btn_productReceiptAdd.setEnabled(True)
        )
        self.btn_productReceiptClear.clicked.connect(
            lambda: self.btn_productReceiptEdit.setEnabled(False)
        )
        self.btn_productReceiptClear.clicked.connect(
            lambda: self.btn_productReceiptRemove.setEnabled(False)
        )
        self.btn_productReceiptClear.clicked.connect(
            lambda: self.le_productReceiptIngredientQuantity.clear()
        )
        self.tw_productReceiptIngredientList.doubleClicked.connect(
            self.loadMenuItemReceiptIngredient
        )
        self.cb_productReceiptMenuItem.currentIndexChanged.connect(
            self.loadMenuItemReceiptIngredients
        )

        # Stock window
        self.rb_stockIngredients.clicked.connect(self.loadStock)
        self.rb_stockOthers.clicked.connect(self.loadStock)

        # Validators
        self.le_customerPhone.setValidator(
            QRegExpValidator(
                QRegExp("^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$")
            )
        )
        self.le_supplierPhone.setValidator(
            QRegExpValidator(
                QRegExp("^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$")
            )
        )
        self.le_workerPhone.setValidator(
            QRegExpValidator(
                QRegExp("^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$")
            )
        )

        self.le_supplierMail.setValidator(
            QRegExpValidator(QRegExp("[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"))
        )

        # Dashboard Client
        self.clearAllDashboardClients()

        # Main Window
        self.btn_fullScreen.clicked.connect(self.fullScreen)
        self.btn_setting.clicked.connect(self.changeSettings)
        self.homeScreen()
        self.infoThread.UpdateInfo.connect(self.updateInfo)
        self.infoThread.UpdateTables.connect(self.updateTables)
        self.infoThread.start()
        if self.serverThread is not None:
            self.serverThread.start()
        self.show()

        # Reduction
        self.btn_cashRegisterReduce.clicked.connect(self.reductionSetup)

        # Logger Show
        self.btn_logs.clicked.connect(self.showLogs)

        # Block Note show
        self.btn_blockNote.clicked.connect(self.showBlockNote)

        # Set dates
        self.dte_docDate.setDateTime(QDateTime(datetime.datetime.now()))
        self.dte_sellDate.setDateTime(QDateTime(datetime.datetime.now()))
        self.dte_reservation.setDateTime(QDateTime(datetime.datetime.now()))

    """License verification"""

    def check_me(self, license=""):
        if not check_license(license):
            check_dialog = CheckerL()
            check_dialog.show()
            rsp = check_dialog.exec_()
            if rsp != 1:
                self.close()
                sys.exit()

    """Logger file"""

    @staticmethod
    def prepareLogFile(level: int = logging.ERROR):
        logFilePath = os.path.join(os.getcwd(), "tmp", "PatusLog.log")
        os.makedirs(os.path.join(os.getcwd(), "tmp"), exist_ok=True)
        logging.basicConfig(
            filename=logFilePath,
            level=level,
            format="%(asctime)s %(levelname)s: %(message)s",
        )

    """Server Main"""

    def startServer(self):
        try:
            if self.serverThread is None:
                self.serverThread = Threads.ServerThread()
                self.serverThread.addClient.connect(self.addClientDashboard)
                self.serverThread.removeClient.connect(self.removeClientDashboard)
                self.serverThread.logUpdater.connect(self.callLog)
                # self.serverThread.logUpdater.connect(print)
                self.serverThread.tablesUpdated.connect(self.populateTables)
                self.serverThread.updateServerStatus.connect(self.updateServerStatus)
                self.serverThread.printerCall.connect(self.printerCall)
                self.serverThread.notificationCall.connect(self.notifySelf)
                self.serverThread.finished.connect(self.stoppedServerThread)
                self.serverThread.start()
            else:
                self.serverThread.stop()
                self.serverThread.wait(1000)
        except Exception as e:
            logging.error(f"[MAIN UI] Start server thread: {e}")

    def stoppedServerThread(self):
        self.serverThread = None

    """BottumBarMenu"""

    def showLogs(self):
        logFilePath = os.path.join(os.getcwd(), "tmp", "PatusLog.log")
        log_previewer = LogPreviewer(logFilePath)
        log_previewer.show()
        log_previewer.exec_()

    def showBlockNote(self):
        block_note = BlockNote(self.DB)
        block_note.show()
        block_note.exec_()

    """SideBarMenu"""

    def showHideSideBar(self):
        if self.f_sideBar.isVisible():
            self.f_sideBar.setVisible(False)
        else:
            self.f_sideBar.setVisible(True)

    """Notification"""

    def showHideNotification(self):
        if self.f_notification.isVisible():
            self.f_notification.setVisible(False)
        else:
            self.f_notification.setVisible(True)

    def clearAllNotifications(self):
        for child in self.w_notification.findChildren(QFrame):
            child.deleteLater()

    @pyqtSlot(str)
    def notifySelf(self, msg: str):
        addNewNotification(parent=self.w_notification, message=msg)

    """Home screen"""

    def homeScreen(self):
        def homeThread():
            while self.sw_content.currentIndex() == 0 and self:
                current_datetime = datetime.datetime.now()
                self.l_time.setText(
                    f"{current_datetime.hour:02d}:{current_datetime.minute:02d}:{current_datetime.second:02d}"
                )
                self.l_date.setText(f"{current_datetime.date()}")
                time.sleep(1)

        home_thread = threading.Thread(target=homeThread)
        home_thread.start()

    """Main Window"""

    def fullScreen(self):
        if self.isFullScreen():
            self.showMaximized()
        else:
            self.showFullScreen()

    """Stock Window"""

    def loadStock(self):
        all_data = self.DB.getAllStocks()
        displayDbData(self.tw_wasteStock, all_data)
        displayDbData(self.tw_stockDb, all_data)

        if self.rb_stockIngredients.isChecked():
            displayDbData(self.tw_stock, self.DB.getAllStockIngredients())
        else:
            displayDbData(self.tw_stock, self.DB.getAllStockOthers())

    """Database"""

    def pictureSelector(self, holder):
        try:
            file_name = QFileDialog.getOpenFileName(
                self,
                "Choose a picture",
                os.getcwd(),
                "JPG Files (*.jpg);;"
                "PNG Files (*.png);;JPEG Files (*.jpeg);;SVG Files (*.svg)",
            )[0]
            if os.path.isfile(file_name):
                # pickle.dump(self.picture, open("pic_compress.p", "wb"))
                pic_pixmap = QPixmap(file_name)
                holder.clear()
                holder.setPixmap(pic_pixmap)
        except Exception as e:
            logging.error(f"[MAIN UI] Picture selector: {e}")

    def fileSelector(self, holder: QLineEdit):
        try:
            file_path = QFileDialog.getOpenFileName(self, "Choose a file", os.getcwd())[
                0
            ]
            if os.path.isfile(file_path):
                description_json, description = Utility.openConvertFile(file_path, True)
                self.fileDescription = description_json
                if isinstance(holder, QLineEdit):
                    holder.setText(description["Extension"])
        except Exception as e:
            logging.error(f"[MAIN UI] File selector: {e}")

    def clearFileDescription(self, holder: QLineEdit):
        self.fileDescription = None
        if isinstance(holder, QLineEdit):
            holder.clear()

    def twDbHandler(self):
        #
        try:
            if self.tw_database.currentIndex() == 0:
                all_data = self.DB.getAllMenus(sorted=True)
                displayDbData(self.tw_menuItem, all_data)
            elif self.tw_database.currentIndex() == 1:
                all_data = self.DB.getAllMenuCategories()
                displayDbData(self.tw_menuCategoryCustom, all_data)
            elif self.tw_database.currentIndex() == 2:
                all_data = self.DB.getAllSupplements()
                displayDbData(self.tw_supplement, all_data)
            elif self.tw_database.currentIndex() == 3:
                all_data = self.DB.getAllExpenses()
                displayDbData(self.tw_expense, all_data)
            elif self.tw_database.currentIndex() == 4:
                all_data = self.DB.getAllExpenseCategories()
                displayDbData(self.tw_expenseCategory, all_data)
            elif self.tw_database.currentIndex() == 5:
                all_data = self.DB.getAllSuppliers(sorted=True)
                displayDbData(self.tw_supplier, all_data)
            elif self.tw_database.currentIndex() == 6:
                all_data = self.DB.getAllCustomers(sorted=True)
                displayDbData(self.tw_customer, all_data)
            elif self.tw_database.currentIndex() == 7:
                if self.currentWorkerCat.name != "Administrator":
                    self.tw_database.currentWidget().setVisible(False)
                else:
                    all_data = self.DB.getAllWorkers(sorted=True)
                    displayDbData(self.tw_worker, all_data)
            elif self.tw_database.currentIndex() == 8:
                if self.currentWorkerCat.name != "Administrator":
                    self.tw_database.currentWidget().setVisible(False)
                else:
                    all_data = self.DB.getAllCategories(sorted=True)
                    displayDbData(self.tw_category, all_data)
            elif self.tw_database.currentIndex() == 9:
                if self.currentWorkerCat.name != "Administrator":
                    self.tw_database.currentWidget().setVisible(False)
                else:
                    all_data = self.DB.getAllSells()
                    displayDbData(self.tw_sell, all_data)
            elif self.tw_database.currentIndex() == 10:
                all_data = self.DB.getAllTables()
                displayDbData(self.tw_table, all_data)
            elif self.tw_database.currentIndex() == 11:
                if self.currentWorkerCat.name != "Administrator":
                    self.tw_database.currentWidget().setVisible(False)
                else:
                    all_data = self.DB.getAllPointers()
                    displayDbData(self.tw_pointer, all_data)
            elif self.tw_database.currentIndex() == 12:
                all_data = self.DB.getAllStocks()
                displayDbData(self.tw_stockDb, all_data)
            elif self.tw_database.currentIndex() == 13:
                all_data = self.DB.getAllFileDoc()
                displayDbData(self.tw_documentDb, all_data)
            elif self.tw_database.currentIndex() == 14:
                all_data = self.DB.getAllTableOwnership()
                displayDbData(self.tw_tableOwnershipDb, all_data)
            else:
                if self.currentWorkerCat.name != "Administrator":
                    self.tw_database.currentWidget().setVisible(False)
                else:
                    all_data = self.DB.getAllPayments()
                    displayDbData(self.tw_paymentDb, all_data)
        except Exception as e:
            logging.error(f"[MAIN UI] twDbHandler: {e}")
        #

    def populateCb(self):
        self.cb_workerCategory.clear()
        self.cb_sellIdWorker.clear()
        self.cb_orderCustomer.clear()
        self.cb_orderWorker.clear()
        self.cb_sellIdCustomer.clear()
        self.cb_wasteStockWorkerId.clear()
        self.cb_wasteCustomWorkerId.clear()
        self.cb_expenseCategory.clear()
        self.cb_menuItemCategoryCustom.clear()
        self.cb_supplementProduct.clear()
        self.cb_productReceiptMenuItem.clear()
        self.cb_expenseSupplier.clear()
        self.cb_productReceiptIngredientName.clear()
        self.cb_tableOwnershipTableId.clear()
        self.cb_tableOwnershipWorkerId.clear()
        self.cb_payment_worker.clear()

        for i, category in enumerate(self.DB.getAllCategories(sorted=True)):
            self.categoryDict[i] = category.id
            self.categoryDictId[category.id] = i
            self.cb_workerCategory.insertItem(i, category.name)
        for i, worker in enumerate(self.DB.getAllWorkers(sorted=True)):
            self.workerDict[i] = worker.id
            self.workerDictId[worker.id] = i
            self.cb_orderWorker.insertItem(i, worker.name)
            self.cb_sellIdWorker.insertItem(i, worker.name)
            self.cb_wasteCustomWorkerId.insertItem(i, worker.name)
            self.cb_wasteStockWorkerId.insertItem(i, worker.name)
            self.cb_tableOwnershipWorkerId.insertItem(i, worker.name)
            self.cb_payment_worker.insertItem(i, worker.name)
        for i, customer in enumerate(self.DB.getAllCustomers()):
            self.customerDict[i] = customer.id
            self.customerDictId[customer.id] = i
            self.cb_orderCustomer.insertItem(i, customer.name)
            self.cb_sellIdCustomer.insertItem(i, customer.name)
        for i, menuItem in enumerate(self.DB.getAllMenus(sorted=True)):
            self.menuItemNameDict[i] = menuItem.id
            self.menuItemNameDictId[menuItem.id] = i
            self.cb_supplementProduct.insertItem(i, menuItem.name)
            self.cb_productReceiptMenuItem.insertItem(i, menuItem.name)
        for i, ingredientItem in enumerate(self.DB.getAllStockIngredients(sorted=True)):
            self.ingredientItemNameDict[i] = ingredientItem.id
            self.ingredientItemDictId[ingredientItem.id] = i
            self.cb_productReceiptIngredientName.insertItem(i, ingredientItem.name)
        for i, expenseCategory in enumerate(
            self.DB.getAllExpenseCategories(sorted=True)
        ):
            self.expenseCategoryNameDict[i] = expenseCategory.id
            self.expenseCategoryNameDictId[expenseCategory.id] = i
            self.cb_expenseCategory.insertItem(i, expenseCategory.name)
            self.cb_wasteCustomCategory.insertItem(i, expenseCategory.name)
            self.cb_stockCategory.insertItem(i, expenseCategory.name)
        for i, supplier in enumerate(self.DB.getAllSuppliers()):
            self.supplierNameDict[i] = supplier.id
            self.supplierNameDictId[supplier.id] = i
            self.cb_expenseSupplier.insertItem(i, supplier.name)
        for i, menuCustomCategory in enumerate(
            self.DB.getAllMenuCategories(sorted=True)
        ):
            self.menuCustomCategoryNameDict[i] = menuCustomCategory.id
            self.menuCustomCategoryNameDictId[menuCustomCategory.id] = i
            self.cb_menuItemCategoryCustom.insertItem(i, menuCustomCategory.name)
        for i, table in enumerate(self.DB.getAllTables(sorted=True)):
            self.tableDict[i] = table.id
            self.tableDictId[table.id] = i
            self.cb_tableOwnershipTableId.insertItem(i, table.name)

    # Menu Item

    def loadMenuItem(self):

        self.current = self.DB.getMenuItemById(
            int(
                self.tw_menuItem.item(
                    self.tw_menuItem.currentRow(), self.tw_menuItem.columnCount() - 1
                ).text()
            )
        )

        self.le_menuItemName.setText(self.current.name)
        self.le_menuItemUnit.setText(str(self.current.unit))
        self.le_menuItemUnitQuantity.setText(str(self.current.quantity))
        self.le_menuItemPrice.setText(str(self.current.price))
        self.l_menuItemPicture.setText(self.current.picture)
        self.cb_menuItemCategory.setCurrentIndex(
            self.menuItemDict[self.current.category]
        )
        self.cb_menuItemCategoryCustom.setCurrentIndex(
            self.menuCustomCategoryNameDictId[self.current.category_id]
        )
        self.btn_menuItemAdd.setEnabled(False)
        self.btn_menuItemEdit.setEnabled(True)
        self.btn_menuItemDelete.setEnabled(True)

    def addMenuItem(self):

        try:
            # pic = self.l_menuItemPicture.pixmap().toImage()
            menu_item = MenuItem(
                name=self.le_menuItemName.text(),
                category=self.cb_menuItemCategory.currentText(),
                category_id=self.menuCustomCategoryNameDict[
                    self.cb_menuItemCategoryCustom.currentIndex()
                ],
                unit=self.le_menuItemUnit.text(),
                quantity=float(self.le_menuItemUnitQuantity.text()),
                price=float(self.le_menuItemPrice.text()),
                picture=self.l_menuItemPicture.text(),
            )
            self.DB.insertMenuItem(menu_item)
            # clear all
            self.le_menuItemName.clear()
            self.le_menuItemUnit.clear()
            self.le_menuItemUnitQuantity.clear()
            self.le_menuItemPrice.clear()
            self.l_menuItemPicture.clear()
            self.cb_menuItemCategory.setCurrentIndex(0)
            self.twDbHandler()
            self.populateMenu()
            self.populateCb()
            self.notifyClients("MENUITEM")
        except Exception as e:
            logging.error(f"[MAIN UI] Add menu item: {e}")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Menu Item not added")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def editMenuItem(self):

        try:
            assert isinstance(self.current, MenuItem)
            self.current.name = self.le_menuItemName.text()
            self.current.category = self.cb_menuItemCategory.currentText()
            self.current.category_id = self.menuCustomCategoryNameDict[
                self.cb_menuItemCategoryCustom.currentIndex()
            ]
            self.current.unit = self.le_menuItemUnit.text()
            self.current.quantity = float(self.le_menuItemUnitQuantity.text())
            self.current.price = float(self.le_menuItemPrice.text())
            self.current.picture = self.l_menuItemPicture.text()
            self.DB.updateMenuItem(self.current)
            # clear all
            self.le_menuItemName.clear()
            self.le_menuItemUnit.clear()
            self.le_menuItemUnitQuantity.clear()
            self.le_menuItemPrice.clear()
            self.l_menuItemPicture.clear()
            self.cb_menuItemCategory.setCurrentIndex(0)
            self.btn_menuItemAdd.setEnabled(True)
            self.btn_menuItemEdit.setEnabled(False)
            self.btn_menuItemDelete.setEnabled(False)
            self.twDbHandler()
            self.populateMenu()
            self.populateCb()
            self.notifyClients("MENUITEM")
        except Exception as e:
            logging.error(f"[MAIN UI] Update menu item: {e}")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Menu Item not updated")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def deleteMenuItem(self):

        try:
            assert isinstance(self.current, MenuItem)
            self.DB.deleteMenuItem(self.current.id)
            # clear all
            self.le_menuItemName.clear()
            self.le_menuItemUnit.clear()
            self.le_menuItemUnitQuantity.clear()
            self.le_menuItemPrice.clear()
            self.l_menuItemPicture.clear()
            self.cb_menuItemCategory.setCurrentIndex(0)
            self.btn_menuItemAdd.setEnabled(True)
            self.btn_menuItemEdit.setEnabled(False)
            self.btn_menuItemDelete.setEnabled(False)
            self.twDbHandler()
            self.populateMenu()
            self.populateCb()
            self.notifyClients("MENUITEM")
        except Exception as e:
            logging.error(f"[MAIN UI] Delete menu item: {e}")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Menu Item not deleted")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    # Menu Custom Category

    def loadMenuCategoryCustom(self):

        self.current = self.DB.getMenuCategoryById(
            int(
                self.tw_menuCategoryCustom.item(
                    self.tw_menuCategoryCustom.currentRow(),
                    self.tw_menuCategoryCustom.columnCount() - 1,
                ).text()
            )
        )

        self.le_menuCategoryCustomName.setText(self.current.name)
        self.cb_menuCategoryCustomPrinting.setCurrentIndex(self.current.printing_place)
        self.btn_menuCategoryCustomAdd.setEnabled(False)
        self.btn_menuCategoryCustomEdit.setEnabled(True)
        self.btn_menuCategoryCustomDelete.setEnabled(True)

    def addMenuCategoryCustom(self):

        try:
            menu_category = MenuCategory(
                name=self.le_menuCategoryCustomName.text(),
                printing_place=self.cb_menuCategoryCustomPrinting.currentIndex(),
            )
            self.DB.insertMenuCategory(menu_category)
            # clear all
            self.le_menuCategoryCustomName.clear()
            self.cb_menuCategoryCustomPrinting.setCurrentIndex(0)
            self.twDbHandler()
            self.populateCb()
            self.notifyClients("MENUCATEGORY")
        except Exception as e:
            logging.error(f"[MAIN UI] Add menu category: {e}")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Menu Custom Category not added")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def editMenuCategoryCustom(self):

        try:
            assert isinstance(self.current, MenuCategory)
            self.current.name = self.le_menuCategoryCustomName.text()
            self.current.printing_place = (
                self.cb_menuCategoryCustomPrinting.currentIndex()
            )
            self.DB.updateMenuCategory(self.current)
            # clear all
            self.le_menuCategoryCustomName.clear()
            self.cb_menuCategoryCustomPrinting.setCurrentIndex(0)
            self.btn_menuCategoryCustomAdd.setEnabled(True)
            self.btn_menuCategoryCustomEdit.setEnabled(False)
            self.btn_menuCategoryCustomDelete.setEnabled(False)
            self.twDbHandler()
            self.populateCb()
            self.notifyClients("MENUCATEGORY")
        except Exception as e:
            logging.error(f"[MAIN UI] Edit menu category: {e}")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Menu Custom Category not updated")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def deleteMenuCategoryCustom(self):

        try:
            assert isinstance(self.current, MenuCategory)
            self.DB.deleteMenuCategory(self.current.id)
            # clear all
            self.le_menuCategoryCustomName.clear()
            self.cb_menuCategoryCustomPrinting.setCurrentIndex(0)
            self.btn_menuCategoryCustomAdd.setEnabled(True)
            self.btn_menuCategoryCustomEdit.setEnabled(False)
            self.btn_menuCategoryCustomDelete.setEnabled(False)
            self.twDbHandler()
            self.populateCb()
            self.notifyClients("MENUCATEGORY")
        except Exception as e:
            logging.error(f"[MAIN UI] Delete menu category: {e}")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Menu Custom Category not deleted")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    # Supplement

    def loadSupplement(self):

        self.current = self.DB.getSupplementById(
            int(
                self.tw_supplement.item(
                    self.tw_supplement.currentRow(),
                    self.tw_supplement.columnCount() - 1,
                ).text()
            )
        )

        self.le_supplementName.setText(self.current.name)
        self.le_supplementQuantity.setText(str(self.current.quantity))
        self.le_supplementPrice.setText(str(self.current.price))
        self.cb_supplementProduct.setCurrentIndex(
            self.menuItemNameDictId[self.current.related_item_id]
        )
        self.btn_supplementAdd.setEnabled(False)
        self.btn_supplementEdit.setEnabled(True)
        self.btn_supplementDelete.setEnabled(True)

    def addSupplement(self):

        try:
            supplement_item = Supplement(
                name=self.le_supplementName.text(),
                related_item_id=self.menuItemNameDict[
                    self.cb_supplementProduct.currentIndex()
                ],
                quantity=float(self.le_supplementQuantity.text()),
                price=float(self.le_supplementPrice.text()),
            )
            self.DB.insertSupplement(supplement_item)
            # clear all
            self.le_supplementName.clear()
            self.le_supplementQuantity.clear()
            self.le_supplementPrice.clear()
            self.cb_supplementProduct.setCurrentIndex(0)
            self.twDbHandler()
            self.populateCb()
            self.populateMenu()
            self.notifyClients("MENUITEM")
        except Exception as e:
            logging.error(f"[MAIN UI] Add supplement: {e}")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Supplement Item not added")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def editSupplement(self):

        try:
            assert isinstance(self.current, Supplement)
            self.current.name = self.le_supplementName.text()
            self.current.related_item_id = self.menuItemNameDict[
                self.cb_supplementProduct.currentIndex()
            ]
            self.current.quantity = float(self.le_supplementQuantity.text())
            self.current.price = float(self.le_supplementPrice.text())
            self.DB.updateSupplement(self.current)
            # clear all
            self.le_supplementName.clear()
            self.le_supplementQuantity.clear()
            self.le_supplementPrice.clear()
            self.cb_supplementProduct.setCurrentIndex(0)
            self.btn_supplementAdd.setEnabled(True)
            self.btn_supplementEdit.setEnabled(False)
            self.btn_supplementDelete.setEnabled(False)
            self.twDbHandler()
            self.populateCb()
            self.populateMenu()
            self.notifyClients("MENUITEM")
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Supplement Item not updated")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def deleteSupplement(self):

        try:
            assert isinstance(self.current, Supplement)
            self.DB.deleteSupplement(self.current.id)
            # clear all
            self.le_supplementName.clear()
            self.le_supplementQuantity.clear()
            self.le_supplementPrice.clear()
            self.cb_supplementProduct.setCurrentIndex(0)
            self.btn_supplementAdd.setEnabled(True)
            self.btn_supplementEdit.setEnabled(False)
            self.btn_supplementDelete.setEnabled(False)
            self.twDbHandler()
            self.populateCb()
            self.populateMenu()
            self.notifyClients("MENUITEM")
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Supplement Item not deleted")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    # Expense
    def expenseSetUp(self):
        expenses = self.DB.getAllExpenses()
        self.setCompleter(self.le_expenseName, [item.name for item in expenses])
        self.setCompleter(self.le_expenseUnit, [item.unit for item in expenses])

    def loadExpense(self):

        self.current = self.DB.getExpenseById(
            int(
                self.tw_expense.item(
                    self.tw_expense.currentRow(), self.tw_expense.columnCount() - 1
                ).text()
            )
        )

        self.le_expenseName.setText(self.current.name)
        self.le_expenseQuantity.setText(str(self.current.quantity))
        self.le_expenseUnit.setText(str(self.current.unit))
        self.le_expensePrice.setText(str(self.current.price))
        self.cb_expensePayed.setChecked(self.current.payed)
        self.btn_expenseAdd.setEnabled(False)
        self.btn_expenseEdit.setEnabled(True)
        self.btn_expenseDelete.setEnabled(True)
        if self.current.supplier_id is not None and isinstance(
            self.current.supplier_id, int
        ):
            self.cb_expenseSupplier.setCurrentIndex(
                self.supplierNameDictId[self.current.supplier_id]
            )
        if self.current.category is not None and isinstance(self.current.category, int):
            self.cb_expenseCategory.setCurrentIndex(
                self.expenseCategoryNameDictId[self.current.category]
            )

    def addExpense(self):

        try:
            expense = Expense(
                name=self.le_expenseName.text(),
                category=self.expenseCategoryNameDict[
                    self.cb_expenseCategory.currentIndex()
                ],
                unit=self.le_expenseUnit.text(),
                quantity=float(self.le_expenseQuantity.text()),
                price=float(eval(self.le_expensePrice.text())),
                supplier_id=self.supplierNameDict[
                    self.cb_expenseSupplier.currentIndex()
                ],
                payed=self.cb_expensePayed.isChecked(),
            )
            current_expense_category = self.DB.getExpenseCategoryById(expense.category)
            if current_expense_category.stock:
                stock_item = self.DB.getStockByNameCat(
                    name=expense.name.lower(), category=expense.category
                )
                if stock_item is not None:
                    if stock_item.unit != expense.unit:
                        raise Exception(
                            f"Stock and expense unit are different ({stock_item.unit=} and {expense.unit=})"
                        )
                    stock_item.quantity += expense.quantity
                    self.DB.updateStock(stock_item)
                else:
                    self.DB.insertStock(
                        Stock(
                            name=expense.name.lower(),
                            category=expense.category,
                            unit=expense.unit,
                            quantity=expense.quantity,
                            is_ingredient=current_expense_category.is_ingredient,
                        )
                    )
            self.DB.insertExpense(expense)
            # clear all
            self.le_expenseName.clear()
            self.le_expenseQuantity.clear()
            self.le_expenseUnit.clear()
            self.le_expensePrice.clear()
            self.cb_expenseCategory.setCurrentIndex(0)
            self.cb_expenseSupplier.setCurrentIndex(0)
            self.cb_expensePayed.setChecked(True)
            self.twDbHandler()
            self.populateCb()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Expense not added")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def editExpense(self):

        try:
            assert isinstance(self.current, Expense)
            self.current.name = self.le_expenseName.text()
            self.current.quantity = float(self.le_expenseQuantity.text())
            self.current.category = self.expenseCategoryNameDict[
                self.cb_expenseCategory.currentIndex()
            ]
            self.current.unit = self.le_expenseUnit.text()
            self.current.price = float(eval(self.le_expensePrice.text()))
            self.current.supplier_id = self.supplierNameDict[
                self.cb_expenseSupplier.currentIndex()
            ]
            self.current.payed = self.cb_expensePayed.isChecked()
            self.DB.updateExpense(self.current)
            # clear all
            self.le_expenseName.clear()
            self.le_expenseQuantity.clear()
            self.le_expenseUnit.clear()
            self.le_expensePrice.clear()
            self.cb_expenseCategory.setCurrentIndex(0)
            self.cb_expenseSupplier.setCurrentIndex(0)
            self.cb_expensePayed.setChecked(True)
            self.btn_expenseAdd.setEnabled(True)
            self.btn_expenseEdit.setEnabled(False)
            self.btn_expenseDelete.setEnabled(False)
            self.twDbHandler()
            self.populateCb()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Expense not updated")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def deleteExpense(self):

        try:
            assert isinstance(self.current, Expense)
            self.DB.deleteExpense(self.current.id)
            # clear all
            self.le_expenseName.clear()
            self.le_expenseQuantity.clear()
            self.le_expenseUnit.clear()
            self.le_expensePrice.clear()
            self.cb_expenseCategory.setCurrentIndex(0)
            self.cb_expenseSupplier.setCurrentIndex(0)
            self.cb_expensePayed.setChecked(True)
            self.btn_expenseAdd.setEnabled(True)
            self.btn_expenseEdit.setEnabled(False)
            self.btn_expenseDelete.setEnabled(False)
            self.twDbHandler()
            self.populateCb()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Raw Product not deleted")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    # Expense Category

    def loadExpenseCategory(self):

        self.current = self.DB.getExpenseCategoryById(
            int(
                self.tw_expenseCategory.item(
                    self.tw_expenseCategory.currentRow(),
                    self.tw_expenseCategory.columnCount() - 1,
                ).text()
            )
        )

        self.le_expenseCategoryName.setText(self.current.name)
        self.cb_expenseCategorySaveToStock.setChecked(self.current.stock)
        self.cb_expenseCategoryIsIngredient.setChecked(self.current.is_ingredient)
        self.btn_expenseCategoryAdd.setEnabled(False)
        self.btn_expenseCategoryEdit.setEnabled(True)
        self.btn_expenseCategoryDelete.setEnabled(True)

    def addExpenseCategory(self):

        try:
            expense_category = ExpenseCategory(
                name=self.le_expenseCategoryName.text(),
                stock=self.cb_expenseCategorySaveToStock.isChecked(),
                is_ingredient=self.cb_expenseCategoryIsIngredient.isChecked(),
            )
            self.DB.insertExpenseCategory(expense_category)
            # clear all
            self.le_expenseCategoryName.clear()
            self.cb_expenseCategorySaveToStock.setChecked(True)
            self.cb_expenseCategoryIsIngredient.setChecked(True)
            self.twDbHandler()
            self.populateCb()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Expense Category not added")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def editExpenseCategory(self):

        try:
            assert isinstance(self.current, ExpenseCategory)
            self.current.name = self.le_expenseCategoryName.text()
            self.current.stock = self.cb_expenseCategorySaveToStock.isChecked()
            self.current.is_ingredient = self.cb_expenseCategoryIsIngredient.isChecked()
            self.DB.updateExpenseCategory(self.current)
            # clear all
            self.le_expenseCategoryName.clear()
            self.cb_expenseCategorySaveToStock.setChecked(True)
            self.cb_expenseCategoryIsIngredient.setChecked(True)
            self.btn_expenseCategoryAdd.setEnabled(True)
            self.btn_expenseCategoryEdit.setEnabled(False)
            self.btn_expenseCategoryDelete.setEnabled(False)
            self.twDbHandler()
            self.populateCb()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Raw Product not updated")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def deleteExpenseCategory(self):

        try:
            assert isinstance(self.current, ExpenseCategory)
            self.DB.deleteExpenseCategory(self.current.id)
            # clear all
            self.le_expenseCategoryName.clear()
            self.cb_expenseCategorySaveToStock.setChecked(True)
            self.cb_expenseCategoryIsIngredient.setChecked(True)
            self.btn_expenseCategoryAdd.setEnabled(True)
            self.btn_expenseCategoryEdit.setEnabled(False)
            self.btn_expenseCategoryDelete.setEnabled(False)
            self.twDbHandler()
            self.populateCb()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Raw Product not deleted")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    # Supplier

    def loadSupplier(self):

        self.current = self.DB.getSupplierById(
            int(
                self.tw_supplier.item(
                    self.tw_supplier.currentRow(), self.tw_supplier.columnCount() - 1
                ).text()
            )
        )

        self.le_supplierName.setText(self.current.name)
        self.le_supplierPhone.setText(self.current.phone)
        self.le_supplierAddress.setText(self.current.address)
        self.le_supplierMail.setText(self.current.name)
        self.btn_supplierAdd.setEnabled(False)
        self.btn_supplierEdit.setEnabled(True)
        self.btn_supplierDelete.setEnabled(True)

    def addSupplier(self):

        try:
            expense_category = Supplier(
                name=self.le_supplierName.text(),
                phone=self.le_supplierPhone.text(),
                address=self.le_supplierAddress.text(),
                mail=self.le_supplierMail.text(),
            )
            self.DB.insertSupplier(expense_category)
            # clear all
            self.le_supplierName.clear()
            self.le_supplierPhone.clear()
            self.le_supplierAddress.clear()
            self.le_supplierMail.clear()
            self.twDbHandler()
            self.populateCb()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Raw Product not added")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def editSupplier(self):

        try:
            assert isinstance(self.current, Supplier)
            self.current.name = self.le_supplierName.text()
            self.current.phone = self.le_supplierPhone.text()
            self.current.address = self.le_supplierAddress.text()
            self.current.mail = self.le_supplierMail.text()
            self.DB.updateSupplier(self.current)
            # clear all
            self.le_supplierName.clear()
            self.le_supplierPhone.clear()
            self.le_supplierAddress.clear()
            self.le_supplierMail.clear()
            self.btn_supplierAdd.setEnabled(True)
            self.btn_supplierEdit.setEnabled(False)
            self.btn_supplierDelete.setEnabled(False)
            self.twDbHandler()
            self.populateCb()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Raw Product not updated")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def deleteSupplier(self):

        try:
            assert isinstance(self.current, Supplier)
            self.DB.deleteSupplier(self.current.id)
            # clear all
            self.le_supplierName.clear()
            self.le_supplierPhone.clear()
            self.le_supplierAddress.clear()
            self.le_supplierMail.clear()
            self.btn_supplierAdd.setEnabled(True)
            self.btn_supplierEdit.setEnabled(False)
            self.btn_supplierDelete.setEnabled(False)
            self.twDbHandler()
            self.populateCb()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Raw Product not deleted")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    # Customer

    def loadCustomer(self):

        self.current = self.DB.getCustomerById(
            int(
                self.tw_customer.item(
                    self.tw_customer.currentRow(), self.tw_customer.columnCount() - 1
                ).text()
            )
        )

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
            customer = Customer(
                self.le_customerName.text(),
                self.le_customerPhone.text(),
                self.le_customerAddress.text(),
                float(self.le_customerScore.text()),
                self.l_customerPicture.text(),
                None,
            )
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
            msg.setText("Check your fields")
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
            msg.setText("Check your fields")
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
            msg.setText("Check your fields")
            msg.setInformativeText("Customer not deleted")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    # Worker

    def loadWorker(self):

        self.current = self.DB.getWorkerById(
            int(
                self.tw_worker.item(
                    self.tw_worker.currentRow(), self.tw_worker.columnCount() - 1
                ).text()
            )
        )

        self.fileDescription = self.current.cv

        self.le_workerName.setText(self.current.name)
        self.le_workerUsername.setText(self.current.username)
        self.le_workerPhone.setText(str(self.current.phone))
        self.le_workerAddress.setText(str(self.current.address))
        self.le_workerSalary.setText(str(self.current.salary))
        self.le_workerScore.setText(str(self.current.score))
        self.l_workerPicture.setText(str(self.current.picture))
        if self.current.cv is not None:
            self.le_workerCv.setText(str(self.current.cv["Extension"]))
        self.btn_workerAdd.setEnabled(False)
        self.btn_workerEdit.setEnabled(True)
        self.btn_workerDelete.setEnabled(True)
        if self.current.id_category is not None and isinstance(
            self.current.id_category, int
        ):
            self.cb_workerCategory.setCurrentIndex(
                self.categoryDictId[self.current.id_category]
            )

    def addWorker(self):

        try:
            worker = Worker(
                name=self.le_workerName.text(),
                username=self.le_workerUsername.text(),
                password=hashlib.sha3_512(
                    self.le_workerPassword.text().encode()
                ).hexdigest(),
                phone=self.le_workerPhone.text(),
                id_category=self.categoryDict[self.cb_workerCategory.currentIndex()],
                address=self.le_workerAddress.text(),
                salary=float(self.le_workerSalary.text()),
                score=float(self.le_workerScore.text()),
                picture=self.l_workerPicture.text(),
                cv=self.fileDescription,
            )
            self.DB.insertWorker(worker)
            # clear all
            self.le_workerName.clear()
            self.le_workerUsername.clear()
            self.le_workerPassword.clear()
            self.le_workerPhone.clear()
            self.le_workerAddress.clear()
            self.le_workerSalary.clear()
            self.le_workerScore.clear()
            self.l_workerPicture.clear()
            self.le_workerCv.clear()
            self.fileDescription = None
            self.cb_workerCategory.setCurrentIndex(0)
            self.twDbHandler()
            self.populateCb()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Worker not added")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def editWorker(self):

        try:
            assert isinstance(self.current, Worker)
            self.current.name = self.le_workerName.text()
            self.current.username = self.le_workerUsername.text()
            if self.le_workerPassword.text() != "":
                self.current.password = hashlib.sha3_512(
                    self.le_workerPassword.text().encode()
                ).hexdigest()
            self.current.phone = self.le_workerPhone.text()
            self.current.id_category = self.categoryDict[
                self.cb_workerCategory.currentIndex()
            ]
            self.current.address = self.le_workerAddress.text()
            self.current.salary = float(self.le_workerSalary.text())
            self.current.score = float(self.le_workerScore.text())
            self.current.picture = None
            self.current.face = None
            if self.fileDescription is not None:
                self.current.cv = Utility.descriptionToJson(self.fileDescription)
            else:
                self.current.cv = None
            self.DB.updateWorker(self.current)
            # clear all
            self.le_workerName.clear()
            self.le_workerUsername.clear()
            self.le_workerPassword.clear()
            self.le_workerPhone.clear()
            self.le_workerAddress.clear()
            self.le_workerSalary.clear()
            self.le_workerScore.clear()
            self.l_workerPicture.clear()
            self.cb_workerCategory.setCurrentIndex(0)
            self.le_workerCv.clear()
            self.fileDescription = None
            self.btn_workerAdd.setEnabled(True)
            self.btn_workerEdit.setEnabled(False)
            self.btn_workerDelete.setEnabled(False)
            self.twDbHandler()
            self.populateCb()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
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
            self.le_workerSalary.clear()
            self.le_workerScore.clear()
            self.l_workerPicture.clear()
            self.cb_workerCategory.setCurrentIndex(0)
            self.le_workerCv.clear()
            self.fileDescription = None
            self.btn_workerAdd.setEnabled(True)
            self.btn_workerEdit.setEnabled(False)
            self.btn_workerDelete.setEnabled(False)
            self.twDbHandler()
            self.populateCb()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Worker not deleted")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    # Sell

    def loadSell(self):

        self.current = self.DB.getSellById(
            int(
                self.tw_sell.item(
                    self.tw_sell.currentRow(), self.tw_sell.columnCount() - 1
                ).text()
            )
        )

        self.dte_sellDate.setDateTime(
            QDateTime.fromString(self.current.date, "yyyy-MM-dd HH:mm:ss")
        )
        self.le_sellTotal.setText(str(self.current.total))
        self.le_sellNbCovers.setText(str(self.current.nb_covers))
        self.cb_sellIdWorker.setCurrentIndex(self.workerDictId[self.current.id_worker])
        self.cb_sellIdCustomer.setCurrentIndex(
            self.customerDictId[self.current.id_customer]
        )
        self.btn_sellAdd.setEnabled(False)
        self.btn_sellEdit.setEnabled(True)
        self.btn_sellDelete.setEnabled(True)
        self.btn_sellShow.setEnabled(True)
        self.btn_sellLoad.setEnabled(True)

    def showSell(self):
        try:
            ticket = prepareTicketForCashier(
                worker_name=self.DB.getWorkerById(self.current.id_worker).name,
                order_items=self.DB.getOrderBySellId(self.current.id),
                tax=0,
                comment="",
                ticket_number=self.current.id,
                given=self.current.total,
                time_date=self.current.date,
            )
            printerUi = PrinterProblem(tickets=[ticket], places=["Preview"])
            printerUi.setWindowTitle("Ticket preview")
            printerUi.buttonBox.setVisible(False)
            printerUi.show()
            printerUi.exec_()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Loading Error")
            msg.setInformativeText("Unable to load ticket")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def addSell(self):

        try:
            sell = Sell(
                id_worker=self.workerDict[self.cb_sellIdWorker.currentIndex()],
                id_customer=self.customerDict[self.cb_sellIdCustomer.currentIndex()],
                date=self.dte_sellDate.dateTime().toString("yyyy-MM-dd HH:mm:ss"),
                total=float(self.le_sellTotal.text()),
                nb_covers=int(self.le_sellNbCovers.text()),
            )
            self.DB.insertSell(sell)
            # clear all
            self.le_sellTotal.clear()
            self.le_sellNbCovers.clear()
            self.cb_sellIdWorker.setCurrentIndex(0)
            self.cb_sellIdCustomer.setCurrentIndex(0)
            self.twDbHandler()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Sell not added")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def editSell(self):

        try:
            assert isinstance(self.current, Sell)
            self.current.id_worker = self.workerDict[
                self.cb_sellIdWorker.currentIndex()
            ]
            self.current.id_customer = self.customerDict[
                self.cb_sellIdCustomer.currentIndex()
            ]
            self.current.date = self.dte_sellDate.dateTime().toString(
                "yyyy-MM-dd HH:mm:ss"
            )
            self.current.total = float(self.le_sellTotal.text())
            self.current.nb_covers = int(self.le_sellNbCovers.text())
            self.DB.updateSell(self.current)
            # clear all
            self.le_sellTotal.clear()
            self.le_sellNbCovers.clear()
            self.cb_sellIdWorker.setCurrentIndex(0)
            self.cb_sellIdCustomer.setCurrentIndex(0)
            self.btn_sellAdd.setEnabled(True)
            self.btn_sellEdit.setEnabled(False)
            self.btn_sellDelete.setEnabled(False)
            self.btn_sellShow.setEnabled(False)
            self.btn_sellLoad.setEnabled(False)
            self.twDbHandler()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Sell not updated")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def deleteSell(self):

        try:
            assert isinstance(self.current, Sell)
            self.DB.deleteSell(self.current.id)
            for table in self.DB.getAllTablesByIdSell(self.current.id):
                table.id_sell = None
                self.DB.updateTable(table)
            # clear all
            self.le_sellTotal.clear()
            self.le_sellNbCovers.clear()
            self.cb_sellIdWorker.setCurrentIndex(0)
            self.cb_sellIdCustomer.setCurrentIndex(0)
            self.btn_sellAdd.setEnabled(True)
            self.btn_sellEdit.setEnabled(False)
            self.btn_sellDelete.setEnabled(False)
            self.btn_sellShow.setEnabled(False)
            self.btn_sellLoad.setEnabled(False)
            self.twDbHandler()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Sell not deleted")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    # Table

    def loadTable(self):

        self.current = self.DB.getTableById(
            int(self.tw_table.item(self.tw_table.currentRow(), 0).text())
        )

        self.le_tableName.setText(self.current.name)
        self.le_tableId.setText(str(self.current.id))
        self.le_tableSeats.setText(str(self.current.seats))
        self.le_tableComment.setText(self.current.comment)
        self.btn_tableAdd.setEnabled(False)
        self.btn_tableEdit.setEnabled(True)
        self.btn_tableDelete.setEnabled(True)

    def addTable(self):
        try:
            table = Table(
                id=int(self.le_tableId.text()),
                name=self.le_tableName.text(),
                seats=int(self.le_tableSeats.text()),
                comment=self.le_tableComment.text(),
            )

            self.DB.insertTable(table)

            # clear all
            self.le_tableName.clear()
            self.le_tableId.clear()
            self.le_tableSeats.clear()
            self.le_tableComment.clear()
            self.twDbHandler()
            self.notifyClients("TABLES")
        except Exception as e:
            #
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
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
            self.current.comment = self.le_tableComment.text()
            # clear all
            self.le_tableName.clear()
            self.le_tableId.clear()
            self.le_tableSeats.clear()
            self.le_tableComment.clear()
            self.btn_tableAdd.setEnabled(True)
            self.btn_tableEdit.setEnabled(False)
            self.btn_tableDelete.setEnabled(False)
            self.DB.updateTable(self.current)
            self.twDbHandler()
            self.notifyClients("TABLES")
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
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
            self.le_tableComment.clear()
            self.btn_tableAdd.setEnabled(True)
            self.btn_tableEdit.setEnabled(False)
            self.btn_tableDelete.setEnabled(False)
            self.twDbHandler()
            self.notifyClients("TABLES")
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Table not deleted")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    # Category
    def clearCategory(self):
        self.le_categoryName.clear()
        self.cb_categoryLevelTables.setChecked(False)
        self.cb_categoryLevelCashier.setChecked(False)
        self.cb_categoryLevelReservation.setChecked(False)
        self.cb_categoryLevelWaste.setChecked(False)
        self.cb_categoryLevelStock.setChecked(False)
        self.cb_categoryLevelReceipt.setChecked(False)
        self.cb_categoryLevelDb.setChecked(False)
        self.cb_categoryLevelPhone.setChecked(False)
        self.cb_categoryLevelStat.setChecked(False)
        self.current = None

    def loadCategory(self):

        self.current = self.DB.getCategoryById(
            int(
                self.tw_category.item(
                    self.tw_category.currentRow(), self.tw_category.columnCount() - 1
                ).text()
            )
        )

        self.le_categoryName.setText(self.current.name)
        self.cb_categoryLevelTables.setChecked(self.current.tables == 1)
        self.cb_categoryLevelCashier.setChecked(self.current.cashier == 1)
        self.cb_categoryLevelReservation.setChecked(self.current.reservation == 1)
        self.cb_categoryLevelWaste.setChecked(self.current.waste == 1)
        self.cb_categoryLevelStock.setChecked(self.current.stock == 1)
        self.cb_categoryLevelReceipt.setChecked(self.current.receipt == 1)
        self.cb_categoryLevelDb.setChecked(self.current.database == 1)
        self.cb_categoryLevelPhone.setChecked(self.current.phone == 1)
        self.cb_categoryLevelStat.setChecked(self.current.dashboard == 1)
        self.btn_categoryAdd.setEnabled(False)
        self.btn_categoryEdit.setEnabled(True)
        self.btn_categoryDelete.setEnabled(True)

    def addCategory(self):

        try:
            category = Category(
                name=self.le_categoryName.text(),
                tables=self.cb_categoryLevelTables.isChecked(),
                cashier=self.cb_categoryLevelCashier.isChecked(),
                reservation=self.cb_categoryLevelReservation.isChecked(),
                waste=self.cb_categoryLevelWaste.isChecked(),
                stock=self.cb_categoryLevelStock.isChecked(),
                receipt=self.cb_categoryLevelReceipt.isChecked(),
                database=self.cb_categoryLevelDb.isChecked(),
                phone=self.cb_categoryLevelPhone.isChecked(),
                dashboard=self.cb_categoryLevelStat.isChecked(),
            )
            self.DB.insertCategory(category)
            # clear all
            self.clearCategory()
            self.twDbHandler()
            self.populateCb()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Worker category not added")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def editCategory(self):

        try:
            assert isinstance(self.current, Category)
            self.current.name = self.le_categoryName.text()
            self.current.tables = self.cb_categoryLevelTables.isChecked()
            self.current.cashier = self.cb_categoryLevelCashier.isChecked()
            self.current.reservation = self.cb_categoryLevelReservation.isChecked()
            self.current.waste = self.cb_categoryLevelWaste.isChecked()
            self.current.stock = self.cb_categoryLevelStock.isChecked()
            self.current.receipt = self.cb_categoryLevelReceipt.isChecked()
            self.current.database = self.cb_categoryLevelDb.isChecked()
            self.current.phone = self.cb_categoryLevelPhone.isChecked()
            self.current.dashboard = self.cb_categoryLevelStat.isChecked()

            # clear all
            self.btn_categoryAdd.setEnabled(True)
            self.btn_categoryEdit.setEnabled(False)
            self.btn_categoryDelete.setEnabled(False)
            self.DB.updateCategory(self.current)
            self.twDbHandler()
            self.populateCb()
            self.clearCategory()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Worker category not updated")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def deleteCategory(self):

        try:
            assert isinstance(self.current, Category)
            self.DB.deleteCategory(self.current.id)
            # clear all
            self.clearCategory()
            self.btn_categoryAdd.setEnabled(True)
            self.btn_categoryEdit.setEnabled(False)
            self.btn_categoryDelete.setEnabled(False)
            self.twDbHandler()
            self.populateCb()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Worker category not deleted")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    # Category
    def clearStockDB(self):
        self.le_stockProductName.clear()
        self.cb_stockCategory.setCurrentIndex(0)
        self.le_stockUnit.clear()
        self.le_stockQuantity.clear()
        self.cb_stockIsIngredient.setChecked(False)
        self.btn_stockAdd.setEnabled(True)
        self.btn_stockEdit.setEnabled(False)
        self.btn_stockDelete.setEnabled(False)
        self.current = None

    def loadStockDB(self):

        self.current = self.DB.getStockById(
            int(
                self.tw_stockDb.item(
                    self.tw_stockDb.currentRow(), self.tw_stockDb.columnCount() - 1
                ).text()
            )
        )

        self.le_stockProductName.setText(self.current.name)
        self.cb_stockCategory.setCurrentIndex(
            self.expenseCategoryNameDictId[self.current.category]
        )
        self.le_stockUnit.setText(self.current.unit)
        self.le_stockQuantity.setText(str(self.current.quantity))
        self.cb_stockIsIngredient.setChecked(self.current.is_ingredient)
        self.btn_categoryAdd.setEnabled(False)
        self.btn_categoryEdit.setEnabled(True)
        self.btn_categoryDelete.setEnabled(True)

    def addStockDB(self):

        try:
            stock = Stock(
                name=self.le_stockProductName.text(),
                category=self.expenseCategoryNameDict[
                    self.cb_stockCategory.currentIndex()
                ],
                unit=self.le_stockUnit.text(),
                quantity=float(self.le_stockQuantity.text()),
                is_ingredient=self.cb_stockIsIngredient.isChecked(),
            )
            self.DB.insertStock(stock)
            # clear all
            self.clearStockDB()
            self.loadStock()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Worker category not added")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def editStockDB(self):

        try:
            assert isinstance(self.current, Stock)

            self.current.name = self.le_stockProductName.text()
            self.current.category = self.expenseCategoryNameDict[
                self.cb_stockCategory.currentIndex()
            ]
            self.current.unit = self.le_stockUnit.text()
            self.current.quantity = float(self.le_stockQuantity.text())
            self.current.is_ingredient = self.cb_stockIsIngredient.isChecked()

            # clear all
            self.DB.updateCategory(self.current)
            self.clearStockDB()
            self.loadStock()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Worker category not updated")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def deleteStockDB(self):

        try:
            assert isinstance(self.current, Category)
            self.DB.deleteStock(self.current.id)
            # clear all
            self.clearStockDB()
            self.loadStock()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Worker category not deleted")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    # TableOwnership
    def clearTableOwnershipDb(self):
        self.cb_tableOwnershipTableId.setCurrentIndex(0)
        self.cb_tableOwnershipWorkerId.setCurrentIndex(0)
        self.btn_tableOwnershipAdd.setEnabled(True)
        self.btn_tableOwnershipEdit.setEnabled(False)
        self.btn_tableOwnershipDelete.setEnabled(False)
        self.current = None

    def loadTableOwnershipDb(self):

        self.current = self.DB.getTableOwnershipById(
            int(
                self.tw_tableOwnershipDb.item(
                    self.tw_tableOwnershipDb.currentRow(),
                    self.tw_tableOwnershipDb.columnCount() - 1,
                ).text()
            )
        )

        self.cb_tableOwnershipTableId.setCurrentIndex(
            self.tableDictId[self.current.table_id]
        )
        self.cb_tableOwnershipWorkerId.setCurrentIndex(
            self.workerDictId[self.current.worker_id]
        )
        self.btn_tableOwnershipAdd.setEnabled(False)
        self.btn_tableOwnershipEdit.setEnabled(True)
        self.btn_tableOwnershipDelete.setEnabled(True)

    def addTableOwnershipDb(self):

        try:
            tableOwnership = TableOwnership(
                table_id=self.tableDict[self.cb_tableOwnershipTableId.currentIndex()],
                worker_id=self.workerDict[
                    self.cb_tableOwnershipWorkerId.currentIndex()
                ],
            )
            self.DB.insertTableOwnership(tableOwnership)
            # clear all
            self.clearTableOwnershipDb()
            self.twDbHandler()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Table Ownership not added")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def editTableOwnershipDb(self):

        try:
            assert isinstance(self.current, TableOwnership)
            self.current.table_id = self.tableDict[
                self.cb_tableOwnershipTableId.currentIndex()
            ]
            self.current.worker_id = self.workerDict[
                self.cb_tableOwnershipWorkerId.currentIndex()
            ]

            # clear all
            self.btn_tableOwnershipAdd.setEnabled(True)
            self.btn_tableOwnershipEdit.setEnabled(False)
            self.btn_tableOwnershipDelete.setEnabled(False)
            self.DB.updateTableOwnership(self.current)
            self.clearTableOwnershipDb()
            self.twDbHandler()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Table Ownership not updated")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def deleteTableOwnershipDb(self):

        try:
            assert isinstance(self.current, TableOwnership)
            self.DB.deleteTableOwnership(self.current.id)
            # clear all
            self.clearTableOwnershipDb()
            self.btn_tableOwnershipAdd.setEnabled(True)
            self.btn_tableOwnershipEdit.setEnabled(False)
            self.btn_tableOwnershipDelete.setEnabled(False)
            self.twDbHandler()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Table Ownership not deleted")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    # FileDoc
    def clearFileDocDb(self):
        self.le_docName.clear()
        self.le_docComment.clear()
        self.le_docPath.clear()
        self.dte_docDate.setDateTime(QDateTime(datetime.datetime.now()))
        self.btn_docAdd.setEnabled(True)
        self.btn_docEdit.setEnabled(False)
        self.btn_docDelete.setEnabled(False)
        self.current = None

    def loadFileDocDb(self):
        try:
            self.current = self.DB.getFileDocById(
                int(
                    self.tw_documentDb.item(
                        self.tw_documentDb.currentRow(),
                        self.tw_documentDb.columnCount() - 1,
                    ).text()
                )
            )

            self.le_docName.setText(self.current.name)
            self.le_docComment.setText(self.current.comment)
            self.dte_docDate.setDateTime(
                QDateTime.fromString(self.current.date, "yyyy-MM-dd HH:mm:ss")
            )
            if self.current.file is not None:
                self.le_docPath.setText(str(self.current.file["Extension"]))
                self.fileDescription = self.current.file
            self.btn_docAdd.setEnabled(False)
            self.btn_docEdit.setEnabled(True)
            self.btn_docDelete.setEnabled(True)
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("File not loaded")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def addFileDocDb(self):
        try:
            fileDoc = FileDoc(
                name=self.le_docName.text(),
                date=self.dte_docDate.dateTime().toString("yyyy-MM-dd HH:mm:ss"),
                comment=self.le_docComment.text(),
                file=self.fileDescription,
            )
            self.DB.insertFileDoc(fileDoc)
            # clear all
            self.clearFileDocDb()
            self.twDbHandler()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("File not added")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def editFileDocDb(self):

        try:
            assert isinstance(self.current, FileDoc)
            self.current.name = self.le_docName.text()
            self.current.date = self.dte_docDate.dateTime().toString(
                "yyyy-MM-dd HH:mm:ss"
            )
            self.current.comment = self.le_docComment.text()
            if self.fileDescription is not None:
                self.current.file = Utility.descriptionToJson(self.fileDescription)
            else:
                self.current.file = None

            # clear all
            self.btn_docAdd.setEnabled(True)
            self.btn_docEdit.setEnabled(False)
            self.btn_docDelete.setEnabled(False)
            self.DB.updateFileDoc(self.current)
            self.clearFileDocDb()
            self.twDbHandler()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("File not updated")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def deleteFileDocDb(self):

        try:
            assert isinstance(self.current, FileDoc)
            self.DB.deleteFileDoc(self.current.id)
            # clear all
            self.btn_docAdd.setEnabled(True)
            self.btn_docEdit.setEnabled(False)
            self.btn_docDelete.setEnabled(False)
            self.clearFileDocDb()
            self.twDbHandler()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("File not deleted")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    # Payment
    def clearPaymentDb(self):
        self.cb_payment_worker.setCurrentIndex(0)
        self.le_payment_amount.clear()
        self.de_payment_date.setDateTime(QDateTime(datetime.datetime.now()))
        self.btn_paymentAdd.setEnabled(True)
        self.btn_paymentEdit.setEnabled(False)
        self.btn_paymentDelete.setEnabled(False)
        self.current = None

    def loadPaymentDb(self):
        try:
            self.current = self.DB.getPaymentById(
                int(
                    self.tw_paymentDb.item(
                        self.tw_paymentDb.currentRow(),
                        self.tw_paymentDb.columnCount() - 1,
                    ).text()
                )
            )

            self.cb_payment_worker.setCurrentIndex(
                self.workerDictId[self.current.worker_id]
            )
            self.le_payment_amount.setText(str(self.current.amount))
            self.de_payment_date.setDateTime(
                QDateTime.fromString(self.current.date, "yyyy-MM-dd HH:mm:ss")
            )
            self.btn_paymentAdd.setEnabled(False)
            self.btn_paymentEdit.setEnabled(True)
            self.btn_paymentDelete.setEnabled(True)
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Payment not loaded")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def addPaymentDb(self):
        try:
            payment = Payment(
                worker_id=self.workerDict[self.cb_payment_worker.currentIndex()],
                date=self.de_payment_date.dateTime().toString("yyyy-MM-dd HH:mm:ss"),
                amount=float(self.le_payment_amount.text()),
            )
            self.DB.insertPayment(payment)
            # clear all
            self.clearPaymentDb()
            self.twDbHandler()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Payment not added")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def editPaymentDb(self):

        try:
            assert isinstance(self.current, Payment)
            self.current.worker_id = self.workerDict[
                self.cb_payment_worker.currentIndex()
            ]
            self.current.date = self.de_payment_date.dateTime().toString(
                "yyyy-MM-dd HH:mm:ss"
            )
            self.current.amount = float(self.le_payment_amount.text())

            # clear all
            self.DB.updatePayment(self.current)
            self.clearPaymentDb()
            self.twDbHandler()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Payment not updated")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def deletePaymentDb(self):

        try:
            assert isinstance(self.current, Payment)
            self.DB.deletePayment(self.current.id)
            # clear all
            self.clearPaymentDb()
            self.twDbHandler()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Payment not deleted")
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
            text = f"{table.name}\nSeats: {table.seats}"
            table_button = MovableButton(parent=self.w_tables, text=text)
            table_button.setObjectName(f"{table.id}")
            table_button.move(
                self.tables_settings.value(
                    f"table_{table_button.objectName()}", QPoint(10, 10)
                )
            )
            table_button.setMinimumSize(120, 60)
            table_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
            if table.id_sell is not None:
                table_button.setStyleSheet("color: rgb(165, 0, 0);")
            else:
                if table.reserved:
                    table_button.setStyleSheet("color: rgb(190, 142, 30);")
                else:
                    table_button.setStyleSheet("color: rgb(20, 150, 0);")

            try:
                if self.currentWorkerCat is not None:
                    if self.currentWorkerCat.cashier:
                        table_button.clicked.connect(
                            partial(self.loadTableContent, table_button.objectName())
                        )
                    else:
                        table_button.clicked.connect(self.permissionProblem)
            except Exception as e:
                logging.error(f"[APP] Set permission ({e})")
            table_button.drag_initiated.connect(self.w_tables.btn_moving)
            table_button.setVisible(True)

    def permissionProblem(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Permission denied")
        msg.setInformativeText("You don't have permission for this action")
        msg.setWindowTitle("Information message")
        msg.exec_()

    def loadTableContent(self, table_id):
        self.clearCashRegister()
        self.sw_content.setCurrentIndex(3)
        self.rb_onTable.setChecked(True)
        self.l_cashRegisterTableNumber.setText(f"{table_id}")

        try:
            self.currentOrder, total, self.currentSell = self.DB.getTableContent(
                table_id
            )
            if self.currentSell is not None:
                self.l_cashRegisterTicketNumber.setText(f"{self.currentSell.id}")
                self.cb_orderWorker.setCurrentIndex(
                    self.workerDictId[self.currentSell.id_worker]
                )
            else:
                currentTable = self.DB.getTableById(table_id)
                currentTable.id_sell = None
                self.DB.updateTable(currentTable)
                self.notifyClients("TABLES")
                self.setNbCoversSetup()
            currentOrderShow = []
            for co in self.currentOrder:
                currentSuppShow = []
                for cs in co.orderItemSupplements:
                    currentSuppShow.append({cs.name: cs.price})
                currentOrderShow.append(
                    OrderItemShow(
                        Ready=bool(co.ready),
                        Name=co.productName,
                        Category=self.DB.getMenuCategoryById(co.productCategory).name,
                        Quantity=co.orderItemQuantity,
                        Total=round(co.orderItemTotal, 2),
                        Supplements=currentSuppShow,
                        Group=co.group_id,
                    )
                )
            currentOrderShow.sort(key=lambda x: x.Group)
            displayDbData(self.tw_orderList, currentOrderShow)
            self.current_table = table_id
            self.lcdN_totalHtt.setProperty("value", total)
            self.lcdN_tax.setProperty("value", self.tax)
            self.lcdN_totalTtc.setProperty("value", total - self.tax)
        except Exception as e:
            self.current_table = table_id
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Table empty")
            msg.setInformativeText(
                "This is an empty table you should use the phone app"
            )
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def editOnFly(self):
        return
        # print(self.tw_orderList.item(
        #     self.tw_orderList.currentRow(), 0).text())
        # print(self.tw_orderList.item(
        #     self.tw_orderList.currentRow(), 1).text())
        # print(self.tw_orderList.item(
        #     self.tw_orderList.currentRow(), 2).text())
        # print(self.tw_orderList.item(
        #     self.tw_orderList.currentRow(), 3).text())
        # print(self.tw_orderList.item(
        #     self.tw_orderList.currentRow(), 4).text())
        # print(self.tw_orderList.item(
        #     self.tw_orderList.currentRow(), 5).text())
        # print(self.tw_orderList.item(
        #     self.tw_orderList.currentRow(), 6).text())

        # # print(self.currentOrder)
        # name = self.tw_orderList.item(
        #     self.tw_orderList.currentRow(), 1).text()
        # cat = self.tw_orderList.item(
        #     self.tw_orderList.currentRow(), 2).text()
        # print(self.DB.getMenuItemByNameCat(
        #     name, self.DB.getMenuCategoryByName(cat)))

        # OrderItem()

    def changeTable(self):
        try:
            free_tables = self.DB.getFreeTables()
            current_table = self.DB.getTableById(self.current_table)
            table_changer_dialog = TableChanger(free_tables=free_tables)
            table_changer_dialog.show()
            rsp = table_changer_dialog.exec_()
            if rsp and rsp != -1:
                current_table.id_sell = None
                self.DB.updateTable(current_table)
                current_table = self.DB.getTableById(rsp)
                current_table.id_sell = self.currentSell.id
                self.DB.updateTable(current_table)
                self.current_table = current_table.id
                self.l_cashRegisterTableNumber.setText(str(rsp))
                self.notifyClients("TABLES")
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error when changing the table !")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def updateTables(self):
        self.twDbHandler()
        self.populateTables()
        self.notifyClients("TABLES")

    """Cash Register"""

    def clearAllProducts(self, fixed: bool = False) -> None:
        if fixed:
            parents = [
                self.w_salade,
                self.w_meal,
                self.w_pizza,
                self.w_hotDrink,
                self.w_hotDrink,
                self.w_coldDrink,
                self.w_dessert,
            ]
            for parent in parents:
                for child in parent.findChildren(QFrame):
                    child.deleteLater()
        else:
            for parent in self.tw_foodMenu.findChildren(QWidget):
                if parent.objectName() != "":
                    if parent.objectName()[:2] != "qt":
                        parent.deleteLater()

    def populateMenu(self, fixed: bool = False) -> None:
        self.clearAllProducts(fixed)
        if fixed:
            all_menu_item = self.DB.getAllMenus(sorted=True)

            for menu_item in all_menu_item:
                if menu_item.category == "Salade":
                    parent = self.w_salade
                elif menu_item.category == "Meal":
                    parent = self.w_meal
                elif menu_item.category == "Pizza":
                    parent = self.w_pizza
                elif menu_item.category == "Hot Drink":
                    parent = self.w_hotDrink
                elif menu_item.category == "Cold Drink":
                    parent = self.w_coldDrink
                else:
                    parent = self.w_dessert
                parent.layout().addWidget(
                    createProductContainer(
                        parent=parent,
                        db=self.DB,
                        product=menu_item,
                        table_id=self.current_table,
                        fc=self.addOrderItem,
                    )
                )

        else:
            all_menu_category = self.DB.getAllMenuCategories()
            for menu_category in all_menu_category:

                tab_widget = QWidget(
                    parent=self.tw_foodMenu, objectName=f"tab_{menu_category.name}"
                )
                tab_grid_layout = QGridLayout(tab_widget)
                tab_widget.setSizePolicy(
                    QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding
                )

                scroll_area = QScrollArea(
                    parent=tab_widget, objectName=f"sa_{menu_category.name}"
                )
                tab_grid_layout.addWidget(scroll_area)
                scroll_area.setSizePolicy(
                    QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding
                )

                widget = QWidget(
                    parent=scroll_area, objectName=f"w_{menu_category.name}"
                )
                grid_layout = QGridLayout(widget)
                widget.setSizePolicy(
                    QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding
                )

                i, j = 0, 0
                for menu_item in self.DB.getMenuItemByCat(menu_category.id):
                    grid_layout.addWidget(
                        createProductContainer(
                            parent=widget,
                            db=self.DB,
                            product=menu_item,
                            table_id=self.current_table,
                            fc=self.addOrderItem,
                        ),
                        i,
                        j,
                    )
                    j += 1
                    if j > 3:
                        i += 1
                        j = 0
                # self.tw_foodMenu.addTab(scroll_area, menu_category.name)
                scroll_area.setWidget(widget)
                self.tw_foodMenu.addTab(tab_widget, menu_category.name)

    def calculateTotal(self):
        total = 0
        for order in self.currentOrder:
            total += order.orderItemTotal
            for supp in order.orderItemSupplements:
                if (
                    order.productUnit.strip().lower() == "g"
                    or order.productUnit.strip().lower() == "kg"
                ):
                    total += supp.price
                else:
                    total += order.orderItemQuantity * supp.price
        self.lcdN_totalHtt.setProperty("value", total)
        self.lcdN_tax.setProperty("value", self.tax)
        self.lcdN_totalTtc.setProperty("value", total - self.tax)
        return total - self.tax

    def addOrderItem(self, order_item, supp_item, rank):
        # print(order_item, supp_item, rank.currentIndex() + 1)
        try:
            tag = True
            supp_list = []
            for ss in supp_item:
                if ss.isChecked():

                    supp_list.append(
                        self.DB.getSupplementById(int(ss.objectName().split("_")[-1]))
                    )

                    ss.setChecked(False)
            order_item = copy.deepcopy(order_item)
            order_item.tableId = self.current_table
            order_item.orderItemSupplements = supp_list
            order_item.group_id = rank.currentIndex() + 1
            rank.setCurrentIndex(0)

            # Check if it is in the current orders
            for order in self.currentOrder:
                if (
                    order_item.productId == order.productId
                    and order_item.orderItemSupplements == order.orderItemSupplements
                    and order_item.group_id == order.group_id
                ):
                    tag = False
                    order.orderItemQuantity += order_item.orderItemQuantity
                    order.orderItemTotal += order_item.orderItemTotal
                    # total += order.orderItemTotal
                    if order.orderItemQuantity <= 0:
                        self.currentOrder.remove(order)

            if tag and order_item.orderItemQuantity > 0:
                # total += order_item.orderItemTotal
                self.currentOrder.append(order_item)
            currentOrderShow = []
            for co in self.currentOrder:
                currentSuppShow = []
                for cs in co.orderItemSupplements:
                    currentSuppShow.append({cs.name: cs.price})
                currentOrderShow.append(
                    OrderItemShow(
                        Ready=bool(co.ready),
                        Name=co.productName,
                        Category=self.DB.getMenuCategoryById(co.productCategory).name,
                        Quantity=co.orderItemQuantity,
                        Total=round(co.orderItemTotal, 2),
                        Supplements=currentSuppShow,
                        Group=co.group_id,
                    )
                )
            currentOrderShow.sort(key=lambda x: x.Group)
            displayDbData(self.tw_orderList, currentOrderShow)
            self.calculateTotal()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Unable to add item")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Error message")
            msg.exec_()

    def deleteCurrent(self):
        try:
            confirmDeletingOrder = ConfirmDeletingOrder()
            confirmDeletingOrder.show()
            rsp = confirmDeletingOrder.exec_()
            if rsp:
                self.sendCancelTicket()
                self.DB.deleteOrder(self.currentSell, self.currentOrder)
                self.clearCashRegister()
                self.notifyClients("TABLES")
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(
                "Unable delete order\nMaybe this order is not saved yet check if it has a ticket number"
            )
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Error message")
            msg.exec_()

    def sendCancelTicket(self):
        try:
            self.printerThread = PrinterThread(
                which_printer="Kitchen",
                worker_name=self.DB.getWorkerById(self.currentSell.id_worker).name,
                order_items=self.currentOrder,
                comment=self.le_cashRegisterComment.toPlainText(),
                ticket_number=self.currentSell.id,
                old=False,
                tax=self.tax,
                mobile=True,
                cancel=True,
            )
            self.printerThread.printStatus.connect(self.printerProblem)
            self.printerThread.logUpdater.connect(self.callLog)
            self.printerThread.start()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Sent cancel ticket to printer!")
            msg.setWindowTitle("Information message")
            msg.exec_()

        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Problem sending cancel ticket to printer!")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def clearCashRegister(self):
        self.tax = 0
        self.l_cashRegisterTableNumber.setText("-")
        self.l_cashRegisterTicketNumber.setText("-")
        self.le_cashRegisterComment.setText("")
        self.tw_orderList.clear()
        self.tw_orderList.setRowCount(0)
        self.tw_orderList.setColumnCount(0)
        self.cb_orderCustomer.setCurrentIndex(0)
        self.cb_orderWorker.setCurrentIndex(self.workerDictId[self.currentWorker.id])
        self.rb_takeAway.setChecked(True)
        self.currentOrder = []
        self.current_table = None
        self.currentSell = None
        self.currentNbCovers = 1
        self.lcdN_totalHtt.setProperty("value", 0)
        self.lcdN_tax.setProperty("value", 0)
        self.lcdN_totalTtc.setProperty("value", 0)

    def pay(self):
        try:
            assert len(self.currentOrder) > 0
            self.cashRegisterPrintFunction("Cashier", False)
            total = self.calculateTotal()
            pay_dialog = Pay(
                callLog=self.callLog,
                printerProblem=self.printerProblem,
                worker_name=self.DB.getWorkerById(self.currentSell.id_worker).name,
                order_items=self.currentOrder,
                tax=self.tax,
                comment=self.le_cashRegisterComment.toPlainText(),
                ticket_number=self.currentSell.id,
                total=total,
                printerThread=PrinterThread,
            )
            pay_dialog.show()
            rsp = pay_dialog.exec_()
            if rsp:
                if self.current_table is not None:

                    table = self.DB.getTableById(self.current_table)
                    table.id_sell = None
                    self.DB.updateTable(table)

                if self.currentSell is not None:
                    self.currentSell.completed = 1
                    self.currentSell.id_customer = self.customerDict[
                        self.cb_orderCustomer.currentIndex()
                    ]

                    self.DB.updateSell(self.currentSell)
                    customer = self.DB.getCustomerById(self.currentSell.id_customer)
                    worker = self.DB.getWorkerById(self.currentSell.id_worker)

                else:
                    self.DB.insertOrder(
                        order_items=self.currentOrder,
                        total=total,
                        id_worker=self.currentWorker.id,
                        id_customer=self.customerDict[
                            self.cb_orderCustomer.currentIndex()
                        ],
                        completed=1,
                        nb_covers=self.currentNbCovers,
                        on_table=self.current_table if self.current_table else 0,
                    )
                    customer = self.DB.getCustomerById(
                        self.customerDict[self.cb_orderCustomer.currentIndex()]
                    )
                    worker = self.currentWorker
                self.updateScore(total=total, worker=worker, customer=customer)
                self.reduceFromStock(self.currentOrder)
                self.clearCashRegister()

                self.notifyClients("TABLES")
        except Exception as e:
            #
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No items to pay")
            msg.setInformativeText("The list of items is empty")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def updateScore(self, total: float, worker: Worker, customer: Customer):
        worker.score += total
        customer.score += total
        self.DB.updateCustomer(customer)
        self.DB.updateWorker(worker)

    def holdOrder(self):

        try:
            assert len(self.currentOrder)
            total = self.calculateTotal()
            if self.currentSell is None:
                self.DB.insertOrder(
                    order_items=self.currentOrder,
                    total=total,
                    id_worker=self.currentWorker.id,
                    id_customer=self.customerDict[self.cb_orderCustomer.currentIndex()],
                    completed=0,
                    nb_covers=self.currentNbCovers,
                    on_table=self.current_table if self.current_table else 0,
                )
            else:
                self.currentSell.total = self.calculateTotal()
                old_order = self.DB.updateOrder(
                    sell=self.currentSell, order_items=self.currentOrder
                )
                getTicketDifference(old_order, self.currentOrder)
            self.clearCashRegister()
            self.currentOrder = []
            self.notifyClients("TABLES")
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Nothing to holding!")
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
                self.currentOrder, total = self.DB.getUncompletedOrdersBySellId(rsp)
                if self.currentSell is not None:
                    self.l_cashRegisterTicketNumber.setText(f"{self.currentSell.id}")
                    self.cb_orderWorker.setCurrentIndex(
                        self.workerDictId[self.currentSell.id_worker]
                    )
                currentOrderShow = []
                for co in self.currentOrder:
                    currentSuppShow = []
                    for cs in co.orderItemSupplements:
                        currentSuppShow.append({cs.name: cs.price})
                    currentOrderShow.append(
                        OrderItemShow(
                            Ready=bool(co.ready),
                            Name=co.productName,
                            Category=self.DB.getMenuCategoryById(
                                co.productCategory
                            ).name,
                            Quantity=co.orderItemQuantity,
                            Total=round(co.orderItemTotal, 2),
                            Supplements=currentSuppShow,
                            Group=co.group_id,
                        )
                    )
                currentOrderShow.sort(key=lambda x: x.Group)
                displayDbData(self.tw_orderList, currentOrderShow)
                self.lcdN_totalHtt.setProperty("value", total)
                self.lcdN_tax.setProperty("value", self.tax)
                self.lcdN_totalTtc.setProperty("value", total - self.tax)
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No holding order !")
            msg.setInformativeText("The holding order list is empty nothing to resume")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def loadOrder(self):
        try:
            assert isinstance(self.current, Sell)
            self.clearCashRegister()
            self.currentSell = self.current
            self.currentOrder = self.DB.getOrderBySellId(self.current.id)
            total = self.calculateTotal()
            if self.currentSell is not None:
                self.l_cashRegisterTicketNumber.setText(f"{self.currentSell.id}")
                self.cb_orderWorker.setCurrentIndex(
                    self.workerDictId[self.currentSell.id_worker]
                )
            currentOrderShow = []
            for co in self.currentOrder:
                currentSuppShow = []
                for cs in co.orderItemSupplements:
                    currentSuppShow.append({cs.name: cs.price})
                currentOrderShow.append(
                    OrderItemShow(
                        Ready=bool(co.ready),
                        Name=co.productName,
                        Category=self.DB.getMenuCategoryById(co.productCategory).name,
                        Quantity=co.orderItemQuantity,
                        Total=round(co.orderItemTotal, 2),
                        Supplements=currentSuppShow,
                        Group=co.group_id,
                    )
                )
            currentOrderShow.sort(key=lambda x: x.Group)
            displayDbData(self.tw_orderList, currentOrderShow)
            self.lcdN_totalHtt.setProperty("value", total)
            self.lcdN_tax.setProperty("value", self.tax)
            self.lcdN_totalTtc.setProperty("value", total - self.tax)
            self.sw_content.setCurrentIndex(3)
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Not a valide sell")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    """Waste Management"""

    def addWasteStock(self):

        try:
            stock_item = self.DB.getStockById(
                int(
                    self.tw_wasteStock.item(
                        self.tw_wasteStock.currentRow(),
                        self.tw_wasteStock.columnCount() - 1,
                    ).text()
                )
            )
            expense_item = self.DB.getExpenseByNameCat(
                name=stock_item.name, category=stock_item.category
            )
            estimated_price = (expense_item.price / expense_item.quantity) * float(
                self.le_wasteStockQuantity.text()
            )
            self.DB.insertWaste(
                Waste(
                    worker_id=self.workerDict[
                        self.cb_wasteStockWorkerId.currentIndex()
                    ],
                    name=stock_item.name,
                    category=self.DB.getExpenseCategoryById(stock_item.category).name,
                    quantity=float(self.le_wasteStockQuantity.text()),
                    price=estimated_price,
                )
            )
            stock_item.quantity -= float(self.le_wasteStockQuantity.text())
            self.DB.updateStock(stock_item)
            self.showWasteHistory()
            self.loadStock()
            self.btn_wasteStockClear.click()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Check your fields")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def addWasteCustom(self):

        try:
            self.DB.insertWaste(
                Waste(
                    worker_id=self.workerDict[
                        self.cb_wasteCustomWorkerId.currentIndex()
                    ],
                    name=self.le_wasteCustomName.text(),
                    category=self.DB.getExpenseCategoryById(
                        self.expenseCategoryNameDict[
                            self.cb_wasteCustomCategory.currentIndex()
                        ]
                    ).name,
                    quantity=float(self.le_wasteCustomQuantity.text()),
                    price=float(self.le_wasteCustomPrice.text()),
                )
            )
            self.showWasteHistory()
            self.btn_wasteCustomClear.click()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Check your fields")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def showWasteHistory(self):

        all_data = self.DB.getAllWastes()

        displayDbData(self.tw_waste, all_data)

    """Reservation"""

    def showTablesReservation(self):
        requested_time_str = self.dte_reservation.dateTime().toString(
            "yyyy-MM-dd HH:mm"
        )

        requested_time = datetime.datetime.strptime(
            requested_time_str, "%Y-%m-%d %H:%M"
        )

        # requested_time = (datetime.datetime.now() +
        #                   datetime.timedelta(hours=24))

        all_data = self.DB.getFreeTablesByDateRange(
            start_date=(requested_time - datetime.timedelta(minutes=60)).strftime(
                "%Y-%m-%d %H:%M"
            ),
            end_date=(requested_time + datetime.timedelta(minutes=60)).strftime(
                "%Y-%m-%d %H:%M"
            ),
        )

        displayDbData(self.tw_reservationTable, all_data)

    def showReservation(self):

        all_data = self.DB.getAllReservations()

        displayDbData(self.tw_reservation, all_data)
        now_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.dte_reservation.setDateTime(
            QDateTime.fromString(now_date, "yyyy-MM-dd HH:mm:ss")
        )
        self.de_reservationSearchDate.setDateTime(
            QDateTime.fromString(now_date, "yyyy-MM-dd HH:mm:ss")
        )

    def loadReservation(self):

        self.current = self.DB.getReservationById(
            int(
                self.tw_reservation.item(
                    self.tw_reservation.currentRow(),
                    self.tw_reservation.columnCount() - 1,
                ).text()
            )
        )

        self.le_reservationName.setText(self.current.name)
        self.le_reservationPhone.setText(str(self.current.phone))
        self.le_reservationNbPerson.setText(str(self.current.nb_person))
        self.dte_reservation.setDateTime(
            QDateTime.fromString(self.current.date, "yyyy-MM-dd HH:mm:ss")
        )
        self.btn_reservationAdd.setEnabled(False)
        self.btn_reservationEdit.setEnabled(True)
        self.btn_reservationDelete.setEnabled(True)

    def addReservation(self):

        try:
            reservation = Reservation(
                name=self.le_reservationName.text(),
                phone=self.le_reservationPhone.text(),
                nb_person=int(self.le_reservationNbPerson.text()),
                table_id=int(
                    self.tw_reservationTable.item(
                        self.tw_reservationTable.currentRow(), 0
                    ).text()
                ),
                date=self.dte_reservation.dateTime().toString("yyyy-MM-dd HH:mm:ss"),
            )
            self.DB.insertReservation(reservation)
            # clear all
            self.btn_reservationClear.click()
            self.showReservation()
            if self.infoThread is not None:
                self.infoThread.check_tables()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Reservation not added")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def editReservation(self):

        try:
            assert isinstance(self.current, Reservation)
            self.current.name = self.le_reservationName.text()
            self.current.phone = self.le_reservationPhone.text()
            self.current.nb_person = self.le_reservationNbPerson.text()
            self.current.date = self.dte_reservation.dateTime().toString(
                "yyyy-MM-dd HH:mm:ss"
            )
            if self.tw_reservationTable.currentRow() >= 0:
                self.current.table_id = int(
                    self.tw_reservationTable.item(
                        self.tw_reservationTable.currentRow(), 0
                    ).text()
                )
            self.DB.updateReservation(self.current)
            # clear all
            self.btn_reservationClear.click()
            self.btn_reservationAdd.setEnabled(True)
            self.btn_reservationEdit.setEnabled(False)
            self.btn_reservationDelete.setEnabled(False)
            self.showReservation()
            if self.infoThread is not None:
                self.infoThread.check_tables()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Raw Product not updated")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def deleteReservation(self):

        try:
            assert isinstance(self.current, Reservation)
            self.DB.deleteReservation(self.current.id)
            # clear all
            self.btn_reservationClear.click()
            self.btn_reservationAdd.setEnabled(True)
            self.btn_reservationEdit.setEnabled(False)
            self.btn_reservationDelete.setEnabled(False)
            self.showReservation()
            if self.infoThread is not None:
                self.infoThread.check_tables()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Raw Product not deleted")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def searchReservation(self):

        if self.cb_reservationDate.isChecked():
            target_date = self.de_reservationSearchDate.dateTime().toString(
                "yyyy-MM-dd"
            )
            requested_time = datetime.datetime.strptime(target_date, "%Y-%m-%d")
            all_data = self.DB.getReservationByDateRange(
                start_date=requested_time.strftime("%Y-%m-%d"),
                end_date=(requested_time + datetime.timedelta(hours=24)).strftime(
                    "%Y-%m-%d"
                ),
            )
            displayDbData(self.tw_reservation, all_data)
        else:
            if self.cb_reservationSearchType.currentIndex() == 0:
                all_data = self.DB.getReservationByName(
                    self.le_reservationSearch.text()
                )
                displayDbData(self.tw_reservation, all_data)
            else:
                all_data = self.DB.getReservationByPhone(
                    self.le_reservationSearch.text()
                )
                displayDbData(self.tw_reservation, all_data)

    """MenuItemReceipt"""
    # Worker

    def loadMenuItemReceiptIngredient(self):

        self.current = self.DB.getMenuItemReceiptById(
            int(
                self.tw_productReceiptIngredientList.item(
                    self.tw_productReceiptIngredientList.currentRow(), 0
                ).text()
            ),
            int(
                self.tw_productReceiptIngredientList.item(
                    self.tw_productReceiptIngredientList.currentRow(), 2
                ).text()
            ),
        )

        self.le_productReceiptIngredientQuantity.setText(str(self.current.quantity))
        self.btn_productReceiptAdd.setEnabled(False)
        self.btn_productReceiptRemove.setEnabled(True)
        self.btn_productReceiptEdit.setEnabled(True)
        if self.current.ingredient_id is not None and isinstance(
            self.current.ingredient_id, int
        ):
            self.cb_productReceiptIngredientName.setCurrentIndex(
                self.ingredientItemDictId[self.current.ingredient_id]
            )

    def addMenuItemReceiptIngredient(self):

        try:
            menuItemReceipt = MenuItemReceipt(
                id=self.menuItemNameDict[self.cb_productReceiptMenuItem.currentIndex()],
                ingredient_name=self.cb_productReceiptIngredientName.currentText(),
                ingredient_id=self.ingredientItemNameDict[
                    self.cb_productReceiptIngredientName.currentIndex()
                ],
                quantity=float(self.le_productReceiptIngredientQuantity.text()),
            )
            self.DB.insertMenuItemReceipt(menuItemReceipt)
            # clear all
            self.btn_productReceiptClear.click()
            self.loadMenuItemReceiptIngredients()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Ingredient not added")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def editMenuItemReceiptIngredient(self):

        try:
            assert isinstance(self.current, MenuItemReceipt)
            self.current.id = self.menuItemNameDict[
                self.cb_productReceiptMenuItem.currentIndex()
            ]
            self.current.ingredient_name = (
                self.cb_productReceiptIngredientName.currentText()
            )
            self.current.ingredient_id = self.ingredientItemNameDict[
                self.cb_productReceiptIngredientName.currentIndex()
            ]
            self.current.quantity = float(
                self.le_productReceiptIngredientQuantity.text()
            )
            self.DB.updateMenuItemReceipt(self.current)
            # clear all
            self.btn_productReceiptClear.click()
            self.loadMenuItemReceiptIngredients()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Ingredient not updated")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def deleteMenuItemReceiptIngredient(self):
        try:
            assert isinstance(self.current, MenuItemReceipt)
            self.DB.deleteMenuItemReceipt(self.current.id, self.current.ingredient_id)
            # clear all
            self.btn_productReceiptClear.click()
            self.loadMenuItemReceiptIngredients()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Check your fields")
            msg.setInformativeText("Ingredient not deleted")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    def loadMenuItemReceiptIngredients(self):

        if self.cb_productReceiptMenuItem.currentIndex() != -1:
            all_data = self.DB.getAllMenuItemReceiptById(
                self.menuItemNameDict[self.cb_productReceiptMenuItem.currentIndex()]
            )
            displayDbData(self.tw_productReceiptIngredientList, all_data)
            self.l_productReceiptEstimatedProductionPrice.setText(
                str(self.calculateEstimatedPrice(all_data))
            )
            self.l_productReceiptPrice.setText(
                str(
                    self.DB.getMenuItemById(
                        self.menuItemNameDict[
                            self.cb_productReceiptMenuItem.currentIndex()
                        ]
                    ).price
                )
            )
            self.l_productReceiptQuantity.setText(
                str(self.calculateEstimatedQuantity(all_data))
            )

    def calculateEstimatedQuantity(self, items: list):
        possible_quantity = []
        if len(items) > 0:
            for item in items:
                stock_quantity = self.DB.getStockById(item.ingredient_id).quantity
                if stock_quantity > 0:
                    possible_quantity.append(stock_quantity / item.quantity)
                else:
                    return 0
            possible_quantity.sort()
            return possible_quantity[0]

    def calculateEstimatedPrice(self, items: list):
        total_price = 0
        if len(items) > 0:
            for item in items:
                all_prices = [
                    x.price for x in self.DB.getExpenseByName(item.ingredient_name)
                ]
                all_quantities = [
                    x.quantity for x in self.DB.getExpenseByName(item.ingredient_name)
                ]
                if len(all_prices) > 0:
                    total_price += (
                        sum(all_prices) / sum(all_quantities)
                    ) * item.quantity
            return total_price

    def reduceFromStock(self, orders: list):
        try:
            for order in orders:
                receipts = self.DB.getAllMenuItemReceiptById(order.productId)
                for receipt in receipts:
                    stock_item = self.DB.getStockById(receipt.ingredient_id)
                    if stock_item is not None:
                        stock_item.quantity -= (
                            receipt.quantity * order.orderItemQuantity
                        )
                        self.DB.updateStock(stock_item)
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Not reduce from stock!")
            msg.setInformativeText("Please check stock items and menu item receipts")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Information message")
            msg.exec_()

    """Reduction functions"""

    def reductionSetup(self):
        reduction_dialog = Reducer()
        reduction_dialog.show()
        rsp = reduction_dialog.exec_()
        if rsp:
            self.tax = float(reduction_dialog.le_reduction.text())
            self.lcdN_tax.setProperty("value", self.tax)
            self.calculateTotal()

    """Nb Covers functions"""

    def setNbCoversSetup(self):
        reduction_dialog = NbCoversChooser()
        reduction_dialog.show()
        rsp = reduction_dialog.exec_()
        if rsp:
            self.currentNbCovers = int(reduction_dialog.le_nb_covers.text())

    """Print functions"""

    def cashRegisterPrintFunction(self, place: str, use_printer: bool):
        try:
            assert len(self.currentOrder)
            order_show = self.currentOrder
            total = self.calculateTotal()
            if self.currentSell is None:

                sell_id = self.DB.insertOrder(
                    order_items=self.currentOrder,
                    total=total,
                    id_worker=self.currentWorker.id,
                    id_customer=self.customerDict[self.cb_orderCustomer.currentIndex()],
                    completed=0,
                    nb_covers=self.currentNbCovers,
                    on_table=self.current_table if self.current_table else 0,
                )
                self.currentSell = self.DB.getSellById(sell_id)

                old = False
            else:
                self.currentSell.total = total
                old_order = self.DB.updateOrder(
                    sell=self.currentSell, order_items=self.currentOrder
                )
                order_show = getTicketDifference(old_order, self.currentOrder)
                if len(order_show) == 0 and place == "Kitchen":
                    confirmDeletingOrder = ConfirmFullTicket()
                    confirmDeletingOrder.show()
                    rsp = confirmDeletingOrder.exec_()
                    if rsp:
                        order_show = self.currentOrder

                old = True

            self.l_cashRegisterTicketNumber.setText(f"{self.currentSell.id}")
            self.notifyClients("TABLES")

            if place == "Kitchen":
                self.serverThread.sendToKitchen(
                    Ticket(
                        id=self.currentSell.id,
                        table_id=self.current_table,
                        worker_id=self.currentSell.id_worker,
                        worker_name=self.DB.getWorkerById(
                            self.currentSell.id_worker
                        ).name,
                        orders=self.currentOrder,
                    )
                )

            if use_printer:
                try:
                    self.printerThread = PrinterThread(
                        which_printer=place,
                        worker_name=self.DB.getWorkerById(
                            self.currentSell.id_worker
                        ).name,
                        order_items=order_show
                        if place == "Kitchen"
                        else self.currentOrder,
                        comment=self.le_cashRegisterComment.toPlainText(),
                        ticket_number=self.currentSell.id,
                        old=old,
                        tax=self.tax,
                        mobile=True,
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

        except Exception as e:
            #
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Problem updating the order!")
            msg.setInformativeText("Please check your order")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    """Dashboard functions"""

    def clearAllDashboardClients(self):
        for child in self.w_workerStats.findChildren(QFrame):
            child.deleteLater()

    def addClientDashboard(self, client):
        self.w_workerStats.layout().addWidget(
            createClientDashBoardContainer(
                parent=self.w_workerStats,
                client=client,
                fc_ring=self.ringClientDashboard,
                fc_message=self.messageClientDashboard,
            )
        )

    def removeClientDashboard(self, client_address):
        for child in self.w_workerStats.findChildren(QFrame):
            if child.objectName() == f"f_{client_address}":
                child.deleteLater()

    def ringClientDashboard(self, client):
        if self.serverThread is not None:
            self.serverThread.ringClient(client)

    def messageClientDashboard(self, client, msg):
        if self.serverThread is not None:
            self.serverThread.messageClient(client, msg.text())
            msg.clear()

    def notifyClients(self, signal: str):
        # print(f"Notify clients: {signal}")
        if self.serverThread is not None:
            self.serverThread.notifyClients(signal)
            self.serverThread.notifyCompletionOrder()
        # print(f"Notified clients: {signal}")

    def notifyClient(self, signal: str, wroker_id: int):
        # print(f"Notify client: {signal} {wroker_id}")
        try:
            if wroker_id is not None and self.serverThread is not None:
                self.serverThread.notifyClient(signal, wroker_id)
        except Exception as e:
            logging.error(f"Failed to notify Client ({e})")

    """Utility functions"""

    def setCompleter(self, lineEdit: QLineEdit, suggestions: list) -> None:
        lineEdit.setCompleter(QCompleter(suggestions))

    @pyqtSlot(str, list, str, int, bool, float, int)
    def printerCall(
        self,
        worker_name: str,
        order_items: List[OrderItem],
        comment: str,
        ticket_number: int,
        old: bool,
        tax: float = 0.0,
        calling_thread: int = None,
    ):
        self.printerThread = PrinterThread(
            which_printer="Kitchen",
            worker_name=worker_name,
            order_items=order_items,
            comment=comment,
            ticket_number=ticket_number,
            old=old,
            tax=tax,
            mobile=True,
            calling_thread=calling_thread,
        )
        self.printerThread.printStatus.connect(self.printerProblem)
        self.printerThread.signalCallingThread.connect(self.notifyClient)
        self.printerThread.logUpdater.connect(self.callLog)
        self.printerThread.start()

    def printerProblem(self, tickets: list, places: list, ticket_thread: QThread):
        printerProblemUi = PrinterProblem(tickets=tickets, places=places)
        printerProblemUi.show()
        rsp = printerProblemUi.exec_()
        if rsp:
            self.printerThread = ticket_thread
            self.printerThread.errors_dictionary = {
                p: t for p, t in zip(places, tickets)
            }
            self.printerThread.start()

    def callLog(self, message: str, errorLog: bool = False):
        if errorLog:
            logging.error(message)
        else:
            logging.info(message)

    def updateInfo(self, nb_free_tables, nb_busy_tables, nb_month_sells, nb_day_sells):
        self.l_freeTables.setText(f"Free tables: {nb_free_tables}")
        self.l_busyTables.setText(f"Busy tables: {nb_busy_tables}")
        self.l_monthSells.setText(f"Number of sells this month: {nb_month_sells}")
        self.l_daySells.setText(f"Number of sells today: {nb_day_sells}")

    def updateServerStatus(self, msg: str):
        self.l_serverStatus.setText(msg)

    def login(self):

        worker = self.DB.getWorkerByUsername(self.le_username.text())

        if (
            isinstance(worker, Worker)
            and hashlib.sha3_512(self.le_password.text().encode()).hexdigest()
            == worker.password
            and isinstance(worker.id_category, int)
        ):
            self.le_username.clear()

            worker_category = self.DB.getCategoryById(worker.id_category)

            self.btn_logInOut.setEnabled(False)
            self.btn_exit.setEnabled(True)
            self.btn_logs.setEnabled(True)
            self.btn_notification.setEnabled(True)
            if worker_category.name != "Administrator":
                self.btn_cashRegisterDeleteCurrent.setEnabled(False)
            else:
                self.btn_cashRegisterDeleteCurrent.setEnabled(True)

            if worker_category.database:
                self.btn_database.setEnabled(True)
            if worker_category.cashier:
                self.btn_cashRegister.setEnabled(True)
            if worker_category.reservation:
                self.btn_reservation.setEnabled(True)
            if worker_category.waste:
                self.btn_waste.setEnabled(True)
            if worker_category.stock:
                self.btn_databaseOverview.setEnabled(True)
            if worker_category.receipt:
                self.btn_productReceipt.setEnabled(True)
            if worker_category.phone:
                self.btn_workerStatus.setEnabled(True)
            if worker_category.dashboard:
                self.btn_statistic.setEnabled(True)
            if worker_category.tables:
                self.btn_tables.setEnabled(True)

            self.currentWorker = worker
            self.currentWorkerCat = worker_category
            self.currentPointer = Pointer(
                date_start=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                date_end=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                id_worker=self.currentWorker.id,
            )
            self.clearCashRegister()
            self.populateTables()
            for child in self.f_sideBar.findChildren(QPushButton):
                if child.isEnabled():
                    child.click()
                    if child.objectName() == "btn_exit":
                        self.permissionProblem()
                    break
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Check your fields")
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
        self.btn_reservation.setEnabled(False)
        self.btn_waste.setEnabled(False)
        self.btn_databaseOverview.setEnabled(False)
        self.btn_workerStatus.setEnabled(False)
        self.btn_statistic.setEnabled(False)
        self.btn_productReceipt.setEnabled(False)
        self.btn_logInOut.setEnabled(True)
        self.btn_logs.setEnabled(False)
        self.btn_notification.setEnabled(False)
        if self.currentPointer is not None:
            self.currentPointer.date_end = datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            self.DB.insertPointer(self.currentPointer)
        self.currentWorker = None
        self.currentWorkerCat = None

    def changeSettings(self):
        try:
            setting = SettingUI()
            setting.show()
            rsp = setting.exec_()
            if rsp:
                logging.info(f"restart server with new settings...")
                if self.serverThread is not None:
                    self.serverThread.stop()
                    self.serverThread.wait(1000)
                    # self.serverThread.restart()
                self.serverThread = ServerThread()
                self.serverThread.addClient.connect(self.addClientDashboard)
                self.serverThread.removeClient.connect(self.removeClientDashboard)
                self.serverThread.logUpdater.connect(self.callLog)
                # self.serverThread.logUpdater.connect(print)
                self.serverThread.tablesUpdated.connect(self.populateTables)
                self.serverThread.printerCall.connect(self.printerCall)
                self.serverThread.updateServerStatus.connect(self.updateServerStatus)
                self.serverThread.notificationCall.connect(self.notifySelf)
                self.serverThread.finished.connect(self.stoppedServerThread)
                self.serverThread.start()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No settings !")
            msg.setInformativeText("The setting file is missing")
            msg.setDetailedText(str(e))
            msg.setWindowTitle("Warning message")
            msg.exec_()

    # On close work

    def closeEvent(self, event):
        self.sw_content.setCurrentIndex(1)
        if self.currentPointer is not None:
            self.currentPointer.date_end = datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            self.DB.insertPointer(self.currentPointer)

        if self.serverThread is not None:
            self.serverThread.stop()
        if self.infoThread is not None:
            self.infoThread.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PatusMainUI()
    sys.exit(app.exec_())
