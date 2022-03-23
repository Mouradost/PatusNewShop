import sqlite3 as sql
from DB.ShopDbInfo import *
from dataclasses import astuple
from DB.DbTables import *
import datetime
import hashlib
import os


class DBHelper(object):
    DATABASE_NAME = "Shop.db"
    DATABASE_VERSION = 1

    def __init__(self):
        self.conn = sql.connect(os.path.join(
            os.getcwd(), "DB", DBHelper.DATABASE_NAME), check_same_thread=False)
        self.c = self.conn.cursor()
        self.createTables()

        if len(self.getAllWorkers()) < 1:
            self.insertWorker(
                Worker(
                    name="Administrator", username="admin", password=hashlib.sha3_512(
                        "admin".encode()).hexdigest(),
                    phone="008615542642820")
            )

        if len(self.getAllCategories()) < 1:
            self.insertCategory(
                Category(
                    name="Administrator", level=0
                ))

        if len(self.getAllCustomers()) < 1:
            self.insertCustomer(
                Customer(
                    name="Unknown"
                ))

        if len(self.getAllSuppliers()) < 1:
            self.insertSupplier(
                Supplier(
                    name="Unknown"
                ))

    def createTables(self):
        with self.conn:
            sql_command = f"""CREATE TABLE IF NOT EXISTS {ExpenseTable.TABLE_NAME} 
                         ( {ExpenseTable.COLUMN_ID} INTEGER PRIMARY KEY AUTOINCREMENT, 
                        {ExpenseTable.COLUMN_NAME} TEXT NOT NULL, 
                        {ExpenseTable.COLUMN_CATEGORY} INTEGER NOT NULL,  
                        {ExpenseTable.COLUMN_UNIT} TEXT NOT NULL, 
                        {ExpenseTable.COLUMN_QUANTITY} REAL NOT NULL,  
                        {ExpenseTable.COLUMN_PRICE} REAL NOT NULL,    
                        {ExpenseTable.COLUMN_SUPPLIER_ID} INTEGER, 
                        {ExpenseTable.COLUMN_DATE} TEXT NOT NULL,
                        FOREIGN KEY ( {ExpenseTable.COLUMN_SUPPLIER_ID} ) REFERENCES 
                        {SupplierTable.TABLE_NAME} ({SupplierTable.COLUMN_ID}),
                        FOREIGN KEY ( {ExpenseTable.COLUMN_CATEGORY} ) REFERENCES 
                        {ExpenseCategoryTable.TABLE_NAME} ({ExpenseCategoryTable.COLUMN_ID}) )"""
            self.c.execute(sql_command)

            sql_command = f"""CREATE TABLE IF NOT EXISTS {MenuTable.TABLE_NAME} 
                         ( {MenuTable.COLUMN_ID} INTEGER PRIMARY KEY AUTOINCREMENT, 
                        {MenuTable.COLUMN_NAME} TEXT NOT NULL, 
                        {MenuTable.COLUMN_CATEGORY} TEXT NOT NULL,  
                        {MenuTable.COLUMN_CATEGORY_ID} INTEGER NOT NULL,
                        {MenuTable.COLUMN_UNIT} TEXT NOT NULL, 
                        {MenuTable.COLUMN_QUANTITY} REAL NOT NULL,  
                        {MenuTable.COLUMN_PRICE} REAL NOT NULL,  
                        {MenuTable.COLUMN_AVAILABLE} BOOL NOT NULL,  
                        {MenuTable.COLUMN_PICTURE} BLOB ,
                        FOREIGN KEY ( {MenuTable.COLUMN_CATEGORY_ID} ) REFERENCES 
                        {MenuCategoryTable.TABLE_NAME} ({MenuCategoryTable.COLUMN_ID}) )"""
            self.c.execute(sql_command)

            sql_command = f"""CREATE TABLE IF NOT EXISTS {MenuCategoryTable.TABLE_NAME} 
                         ( {MenuCategoryTable.COLUMN_ID} INTEGER PRIMARY KEY AUTOINCREMENT, 
                        {MenuCategoryTable.COLUMN_NAME} TEXT NOT NULL,
                        {MenuCategoryTable.COLUMN_PRINTING_PLACE} INTEGER NOT NULL)"""
            self.c.execute(sql_command)

            sql_command = f"""CREATE TABLE IF NOT EXISTS {StockTable.TABLE_NAME} 
                         ( {StockTable.COLUMN_ID} INTEGER PRIMARY KEY AUTOINCREMENT, 
                        {StockTable.COLUMN_NAME} TEXT NOT NULL, 
                        {StockTable.COLUMN_CATEGORY} TEXT NOT NULL,  
                        {StockTable.COLUMN_UNIT} TEXT NOT NULL, 
                        {StockTable.COLUMN_QUANTITY} REAL NOT NULL)"""
            self.c.execute(sql_command)

            sql_command = f"""CREATE TABLE IF NOT EXISTS {SupplementTable.TABLE_NAME} 
                         ( {SupplementTable.COLUMN_ID} INTEGER PRIMARY KEY AUTOINCREMENT, 
                        {SupplementTable.COLUMN_NAME} TEXT NOT NULL, 
                        {SupplementTable.COLUMN_RELATED_ITEM_ID} INTEGER NOT NULL, 
                        {SupplementTable.COLUMN_QUANTITY} REAL NOT NULL,
                        {SupplementTable.COLUMN_PRICE} REAL NOT NULL,
                        FOREIGN KEY ( {SupplementTable.COLUMN_RELATED_ITEM_ID} ) REFERENCES 
                        {MenuTable.TABLE_NAME} ({MenuTable.COLUMN_ID}) )"""
            self.c.execute(sql_command)

            sql_command = f"""CREATE TABLE IF NOT EXISTS {SupplierTable.TABLE_NAME} 
                         ( {SupplierTable.COLUMN_ID} INTEGER PRIMARY KEY AUTOINCREMENT, 
                        {SupplierTable.COLUMN_NAME} TEXT NOT NULL, 
                        {SupplierTable.COLUMN_PHONE} TEXT, 
                        {SupplierTable.COLUMN_ADDRESS} TEXT,
                        {SupplierTable.COLUMN_MAIL} TEXT)"""
            self.c.execute(sql_command)

            sql_command = f"""CREATE TABLE IF NOT EXISTS {ExpenseCategoryTable.TABLE_NAME} 
                         ( {ExpenseCategoryTable.COLUMN_ID} INTEGER PRIMARY KEY AUTOINCREMENT, 
                        {ExpenseCategoryTable.COLUMN_NAME} TEXT NOT NULL, 
                        {ExpenseCategoryTable.COLUMN_STOCK} BOOL NOT NULL)"""
            self.c.execute(sql_command)

            sql_command = f"""CREATE TABLE IF NOT EXISTS {ReservationTable.TABLE_NAME} 
                         ( {ReservationTable.COLUMN_ID} INTEGER PRIMARY KEY AUTOINCREMENT, 
                        {ReservationTable.COLUMN_NAME} TEXT NOT NULL, 
                        {ReservationTable.COLUMN_PHONE} TEXT,  
                        {ReservationTable.COLUMN_CUSTOMER_ID} INTEGER, 
                        {ReservationTable.COLUMN_NB_PERSON} INTEGER,  
                        {ReservationTable.COLUMN_TABLE_ID} INTEGER,  
                        {ReservationTable.COLUMN_DATE} TEXT NOT NULL,
                        FOREIGN KEY ( {ReservationTable.COLUMN_CUSTOMER_ID} ) REFERENCES 
                        {CustomerTable.TABLE_NAME} ({CustomerTable.COLUMN_ID}),
                        FOREIGN KEY ( {ReservationTable.COLUMN_TABLE_ID} ) REFERENCES 
                        {TableTable.TABLE_NAME} ({TableTable.COLUMN_ID}) )"""
            self.c.execute(sql_command)

            sql_command = f"""CREATE TABLE IF NOT EXISTS {WasteTable.TABLE_NAME} 
                         ( {WasteTable.COLUMN_ID} INTEGER PRIMARY KEY AUTOINCREMENT, 
                         {WasteTable.COLUMN_WORKER_ID} INTEGER,
                        {WasteTable.COLUMN_NAME} TEXT NOT NULL, 
                        {WasteTable.COLUMN_CATEGORY} TEXT NOT NULL,  
                        {WasteTable.COLUMN_QUANTITY} REAL NOT NULL, 
                        {WasteTable.COLUMN_PRICE} REAL NOT NULL,
                        {WasteTable.COLUMN_DATE} REAL NOT NULL,
                        FOREIGN KEY ( {WasteTable.COLUMN_WORKER_ID} ) REFERENCES 
                        {WorkerTable.TABLE_NAME} ({WorkerTable.COLUMN_ID}))"""
            self.c.execute(sql_command)

            sql_command = f"""CREATE TABLE IF NOT EXISTS {CustomerTable.TABLE_NAME} 
                                     ( {CustomerTable.COLUMN_ID} INTEGER PRIMARY KEY AUTOINCREMENT, 
                                    {CustomerTable.COLUMN_NAME} TEXT NOT NULL,  
                                    {CustomerTable.COLUMN_PHONE} TEXT,  
                                    {CustomerTable.COLUMN_ADDRESS} TEXT,  
                                    {CustomerTable.COLUMN_SCORE} REAL NOT NULL,  
                                    {CustomerTable.COLUMN_PICTURE} BLOB,  
                                    {CustomerTable.COLUMN_FACE} BLOB )"""
            self.c.execute(sql_command)

            sql_command = f"""CREATE TABLE IF NOT EXISTS {WorkerTable.TABLE_NAME} 
                                     ( {WorkerTable.COLUMN_ID} INTEGER PRIMARY KEY AUTOINCREMENT, 
                                    {WorkerTable.COLUMN_NAME} TEXT NOT NULL,   
                                    {WorkerTable.COLUMN_USERNAME} TEXT NOT NULL,
                                    {WorkerTable.COLUMN_PASSWORD} BLOB NOT NULL,  
                                    {WorkerTable.COLUMN_PHONE} TEXT,   
                                    {WorkerTable.COLUMN_ID_CATEGORY} INTEGER NOT NULL, 
                                    {WorkerTable.COLUMN_ADDRESS} TEXT,
                                    {WorkerTable.COLUMN_SALARY} REAL NOT NULL,
                                    {WorkerTable.COLUMN_SCORE} REAL NOT NULL,  
                                    {WorkerTable.COLUMN_PICTURE} BLOB,  
                                    {WorkerTable.COLUMN_FACE} BLOB, 
                                    CONSTRAINT {WorkerTable.COLUMN_USERNAME}_unique 
                                    UNIQUE ({WorkerTable.COLUMN_USERNAME}), 
                                     FOREIGN KEY ( {WorkerTable.COLUMN_ID_CATEGORY} ) REFERENCES 
                                     {CategoryTable.TABLE_NAME} ({CategoryTable.COLUMN_ID}) )"""
            self.c.execute(sql_command)

            sql_command = f"""CREATE TABLE IF NOT EXISTS {SellTable.TABLE_NAME} 
                                     ( {SellTable.COLUMN_ID} INTEGER PRIMARY KEY AUTOINCREMENT, 
                                    {SellTable.COLUMN_ID_WORKER} INTEGER NOT NULL, 
                                    {SellTable.COLUMN_ID_CUSTOMER} INTEGER NOT NULL, 
                                    {SellTable.COLUMN_DATE} TEXT NOT NULL,  
                                    {SellTable.COLUMN_TOTAL} REAL NOT NULL, 
                                    {SellTable.COLUMN_COMPLETED} INTEGER NOT NULL, 
                                     FOREIGN KEY ( {SellTable.COLUMN_ID_WORKER} ) REFERENCES 
                                     {WorkerTable.TABLE_NAME} ({WorkerTable.COLUMN_ID}), 
                                     FOREIGN KEY ( {SellTable.COLUMN_ID_CUSTOMER} ) REFERENCES 
                                     {CustomerTable.TABLE_NAME} ({CustomerTable.COLUMN_ID}) )"""
            self.c.execute(sql_command)

            sql_command = f"""CREATE TABLE IF NOT EXISTS {SellItemTable.TABLE_NAME} 
                                     ( {SellItemTable.COLUMN_ID} INTEGER PRIMARY KEY AUTOINCREMENT, 
                                    {SellItemTable.COLUMN_ID_PRODUCT} INTEGER NOT NULL, 
                                    {SellItemTable.COLUMN_ID_SELL} INTEGER NOT NULL, 
                                    {SellItemTable.COLUMN_QUANTITY} REAL NOT NULL,  
                                    {SellItemTable.COLUMN_TOTAL} REAL NOT NULL, 
                                     FOREIGN KEY ( {SellItemTable.COLUMN_ID_PRODUCT} ) REFERENCES 
                                     {MenuTable.TABLE_NAME} ({MenuTable.COLUMN_ID}) )"""
            self.c.execute(sql_command)

            sql_command = f"""CREATE TABLE IF NOT EXISTS {SellItemSupplementTable.TABLE_NAME} 
                                     ( {SellItemSupplementTable.COLUMN_ID} INTEGER PRIMARY KEY AUTOINCREMENT, 
                                    {SellItemSupplementTable.COLUMN_ID_SUPPLEMENT} INTEGER NOT NULL, 
                                    {SellItemSupplementTable.COLUMN_ID_SELL_ITEM} INTEGER NOT NULL, 
                                    {SellItemSupplementTable.COLUMN_PRICE} REAL NOT NULL, 
                                     FOREIGN KEY ( {SellItemSupplementTable.COLUMN_ID_SELL_ITEM} ) REFERENCES 
                                     {SellItemTable.TABLE_NAME} ({SellItemTable.COLUMN_ID}), FOREIGN KEY ( {SellItemSupplementTable.COLUMN_ID_SUPPLEMENT} ) REFERENCES 
                                     {SupplementTable.TABLE_NAME} ({SupplementTable.COLUMN_ID}) )"""
            self.c.execute(sql_command)

            sql_command = f"""CREATE TABLE IF NOT EXISTS {TableTable.TABLE_NAME} 
                                     ( {TableTable.COLUMN_ID} INTEGER PRIMARY KEY, 
                                    {TableTable.COLUMN_NAME} TEXT NOT NULL,  
                                    {TableTable.COLUMN_SEATS} INTEGER NOT NULL,  
                                    {TableTable.COLUMN_COMMENT} TEXT,  
                                    {TableTable.COLUMN_ID_SELL} INTEGER, 
                                     FOREIGN KEY ( {TableTable.COLUMN_ID_SELL} ) REFERENCES 
                                     {SellTable.TABLE_NAME} ({SellTable.COLUMN_ID}) )"""
            self.c.execute(sql_command)

            sql_command = f"""CREATE TABLE IF NOT EXISTS {CategoryTable.TABLE_NAME} 
                                                 ( {CategoryTable.COLUMN_ID} INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                {CategoryTable.COLUMN_NAME} TEXT NOT NULL,  
                                                {CategoryTable.COLUMN_LEVEL} INTEGER NOT NULL )"""
            self.c.execute(sql_command)

            sql_command = f"""CREATE TABLE IF NOT EXISTS {PointerTable.TABLE_NAME} 
                                                        ( {PointerTable.COLUMN_ID} INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                        {PointerTable.COLUMN_DATE_START} TEXT NOT NULL,   
                                                        {PointerTable.COLUMN_DATE_END} TEXT NOT NULL,  
                                                        {PointerTable.COLUMN_ID_WORKER} INTEGER NOT NULL, 
                                                        FOREIGN KEY ( {PointerTable.COLUMN_ID_WORKER} ) REFERENCES 
                                                        {WorkerTable.TABLE_NAME} ({WorkerTable.COLUMN_ID})  )"""
            self.c.execute(sql_command)

    # Insertions
    def insertMenuItem(self, x: MenuItem):
        with self.conn:
            sql_command = f"""INSERT INTO {MenuTable.TABLE_NAME} ({MenuTable.COLUMN_NAME}, 
                            {MenuTable.COLUMN_CATEGORY}, {MenuTable.COLUMN_CATEGORY_ID}, {MenuTable.COLUMN_UNIT}, {MenuTable.COLUMN_QUANTITY}, 
                            {MenuTable.COLUMN_PRICE}, {MenuTable.COLUMN_AVAILABLE}, {MenuTable.COLUMN_PICTURE}) 
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
            self.c.execute(sql_command, astuple(x)[:-1])

    def insertExpense(self, x: Expense):
        with self.conn:
            sql_command = f"""INSERT INTO {ExpenseTable.TABLE_NAME} ({ExpenseTable.COLUMN_NAME}, 
                            {ExpenseTable.COLUMN_CATEGORY}, {ExpenseTable.COLUMN_UNIT}, {ExpenseTable.COLUMN_QUANTITY}, 
                            {ExpenseTable.COLUMN_PRICE}, {ExpenseTable.COLUMN_SUPPLIER_ID}, {ExpenseTable.COLUMN_DATE}) 
                            VALUES (?, ?, ?, ?, ?, ?, ?)"""
            self.c.execute(sql_command, astuple(x)[:-1])

    def insertStock(self, x: Stock):
        with self.conn:
            sql_command = f"""INSERT INTO {StockTable.TABLE_NAME} ({StockTable.COLUMN_NAME}, 
                            {StockTable.COLUMN_CATEGORY}, {StockTable.COLUMN_UNIT}, {StockTable.COLUMN_QUANTITY}) 
                            VALUES (?, ?, ?, ?)"""
            self.c.execute(sql_command, astuple(x)[:-1])

    def insertSupplement(self, x: Supplement):
        with self.conn:
            sql_command = f"""INSERT INTO {SupplementTable.TABLE_NAME} ({SupplementTable.COLUMN_NAME}, 
                            {SupplementTable.COLUMN_RELATED_ITEM_ID}, {SupplementTable.COLUMN_QUANTITY}, {SupplementTable.COLUMN_PRICE}) 
                            VALUES (?, ?, ?, ?)"""
            self.c.execute(sql_command, astuple(x)[:-1])

    def insertCustomer(self, x: Customer):
        with self.conn:
            sql_command = f"""INSERT INTO {CustomerTable.TABLE_NAME} ({CustomerTable.COLUMN_NAME}, 
                            {CustomerTable.COLUMN_PHONE}, {CustomerTable.COLUMN_ADDRESS}, 
                            {CustomerTable.COLUMN_SCORE}, {CustomerTable.COLUMN_PICTURE}, 
                            {CustomerTable.COLUMN_FACE}) 
                            VALUES (?, ?, ?, ?, ?, ?)"""
            self.c.execute(sql_command, astuple(x)[:-1])

    def insertWorker(self, x: Worker):
        with self.conn:
            sql_command = f"""INSERT INTO {WorkerTable.TABLE_NAME} ({WorkerTable.COLUMN_NAME}, 
                            {WorkerTable.COLUMN_USERNAME}, {WorkerTable.COLUMN_PASSWORD}, {WorkerTable.COLUMN_PHONE}, 
                            {WorkerTable.COLUMN_ID_CATEGORY}, {WorkerTable.COLUMN_ADDRESS}, {WorkerTable.COLUMN_SALARY},
                            {WorkerTable.COLUMN_SCORE}, {WorkerTable.COLUMN_PICTURE}, 
                            {WorkerTable.COLUMN_FACE}) 
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            self.c.execute(sql_command, astuple(x)[:-1])

    def insertSell(self, x: Sell):
        with self.conn:
            sql_command = f"""INSERT INTO {SellTable.TABLE_NAME} ({SellTable.COLUMN_ID_WORKER}, 
                            {SellTable.COLUMN_ID_CUSTOMER}, {SellTable.COLUMN_DATE}, 
                            {SellTable.COLUMN_TOTAL}, {SellTable.COLUMN_COMPLETED}) 
                            VALUES (?, ?, ?, ?, ?)"""
            self.c.execute(sql_command, astuple(x)[:-1])
            return self.c.execute("SELECT last_insert_rowid()").fetchone()[0]

    def insertSellItem(self, x: SellItem):
        with self.conn:
            sql_command = f"""INSERT INTO {SellItemTable.TABLE_NAME} ({SellItemTable.COLUMN_ID_PRODUCT}, 
                            {SellItemTable.COLUMN_ID_SELL}, {SellItemTable.COLUMN_QUANTITY}, 
                            {SellItemTable.COLUMN_TOTAL}) VALUES (?, ?, ?, ?)"""
            self.c.execute(sql_command, astuple(x)[:-1])
            return self.c.execute("SELECT last_insert_rowid()").fetchone()[0]

    def insertSellItemSupplement(self, x: SellItemSupplement):
        with self.conn:
            sql_command = f"""INSERT INTO {SellItemSupplementTable.TABLE_NAME} ({SellItemSupplementTable.COLUMN_ID_SUPPLEMENT}, 
                            {SellItemSupplementTable.COLUMN_ID_SELL_ITEM}, {SellItemSupplementTable.COLUMN_PRICE}) VALUES (?, ?, ?)"""
            self.c.execute(sql_command, astuple(x)[:-1])

    def insertTable(self, x: Table):
        with self.conn:
            sql_command = f"""INSERT INTO {TableTable.TABLE_NAME} ({TableTable.COLUMN_ID}, {TableTable.COLUMN_NAME}, 
                            {TableTable.COLUMN_SEATS}, {TableTable.COLUMN_COMMENT}, {TableTable.COLUMN_ID_SELL}) 
                            VALUES (?, ?, ?, ?, ?)"""
            self.c.execute(sql_command, astuple(x))

    def insertCategory(self, x: Category):
        with self.conn:
            sql_command = f"""INSERT INTO {CategoryTable.TABLE_NAME} ({CategoryTable.COLUMN_NAME}, 
                            {CategoryTable.COLUMN_LEVEL}) 
                            VALUES (?, ?)"""
            self.c.execute(sql_command, astuple(x)[:-1])

    def insertPointer(self, x: Pointer):
        with self.conn:
            sql_command = f"""INSERT INTO {PointerTable.TABLE_NAME} ({PointerTable.COLUMN_DATE_START}, 
                            {PointerTable.COLUMN_DATE_END}, {PointerTable.COLUMN_ID_WORKER}) 
                            VALUES (?, ?, ?)"""
            self.c.execute(sql_command, astuple(x)[:-1])

    def insertSupplier(self, x: Supplier):
        with self.conn:
            sql_command = f"""INSERT INTO {SupplierTable.TABLE_NAME} ({SupplierTable.COLUMN_NAME}, 
                            {SupplierTable.COLUMN_PHONE}, {SupplierTable.COLUMN_ADDRESS}, {SupplierTable.COLUMN_MAIL}) 
                            VALUES (?, ?, ?, ?)"""
            self.c.execute(sql_command, astuple(x)[:-1])

    def insertExpenseCategory(self, x: ExpenseCategory):
        with self.conn:
            sql_command = f"""INSERT INTO {ExpenseCategoryTable.TABLE_NAME} ({ExpenseCategoryTable.COLUMN_NAME}, 
                            {ExpenseCategoryTable.COLUMN_STOCK}) 
                            VALUES (?, ?)"""
            self.c.execute(sql_command, astuple(x)[:-1])

    def insertMenuCategory(self, x: MenuCategory):
        with self.conn:
            sql_command = f"""INSERT INTO {MenuCategoryTable.TABLE_NAME} ({MenuCategoryTable.COLUMN_NAME}, {MenuCategoryTable.COLUMN_PRINTING_PLACE}) 
                            VALUES (?, ?)"""
            self.c.execute(sql_command, astuple(x)[:-1])

    def insertReservation(self, x: Reservation):
        with self.conn:
            sql_command = f"""INSERT INTO {ReservationTable.TABLE_NAME} ({ReservationTable.COLUMN_NAME}, 
                            {ReservationTable.COLUMN_PHONE}, {ReservationTable.COLUMN_CUSTOMER_ID}, {ReservationTable.COLUMN_NB_PERSON}, 
                            {ReservationTable.COLUMN_TABLE_ID}, {ReservationTable.COLUMN_DATE}) 
                            VALUES (?, ?, ?, ?, ?, ?)"""
            self.c.execute(sql_command, astuple(x)[:-1])

    def insertWaste(self, x: Waste):
        with self.conn:
            sql_command = f"""INSERT INTO {WasteTable.TABLE_NAME} ({WasteTable.COLUMN_WORKER_ID}, {WasteTable.COLUMN_NAME}, 
                            {WasteTable.COLUMN_CATEGORY}, {WasteTable.COLUMN_QUANTITY}, {WasteTable.COLUMN_PRICE}, {WasteTable.COLUMN_DATE}) 
                            VALUES (?, ?, ?, ?, ?, ?)"""
            self.c.execute(sql_command, astuple(x)[:-1])

    # Delete one
    def deleteExpense(self, _id: int):
        with self.conn:
            self.c.execute(
                f"DELETE FROM {ExpenseTable.TABLE_NAME} WHERE {ExpenseTable.COLUMN_ID}=?", (_id,))

    def deleteMenuItem(self, _id: int):
        with self.conn:
            self.c.execute(
                f"DELETE FROM {MenuTable.TABLE_NAME} WHERE {MenuTable.COLUMN_ID}=?", (_id,))

    def deleteCustomer(self, _id: int):
        with self.conn:
            self.c.execute(
                f"DELETE FROM {CustomerTable.TABLE_NAME} WHERE {CustomerTable.COLUMN_ID}=?", (_id,))

    def deleteWorker(self, _id: int):
        with self.conn:
            self.c.execute(
                f"DELETE FROM {WorkerTable.TABLE_NAME} WHERE {WorkerTable.COLUMN_ID}=?", (_id,))

    def deleteSell(self, _id: int):
        with self.conn:
            self.c.execute(
                f"DELETE FROM {SellTable.TABLE_NAME} WHERE {SellTable.COLUMN_ID}=?", (_id,))
        self.deleteSellContent()

    def deleteSellItem(self, _id: int):
        with self.conn:
            self.c.execute(
                f"DELETE FROM {SellItemTable.TABLE_NAME} WHERE {SellItemTable.COLUMN_ID}=?", (_id,))

    def deleteSellItemSupplement(self, _id: int):
        with self.conn:
            self.c.execute(
                f"DELETE FROM {SellItemSupplementTable.TABLE_NAME} WHERE {SellItemSupplementTable.COLUMN_ID}=?", (_id,))

    def deleteTable(self, _id: int):
        with self.conn:
            self.c.execute(
                f"DELETE FROM {TableTable.TABLE_NAME} WHERE {TableTable.COLUMN_ID}=?", (_id,))

    def deleteCategory(self, _id: int):
        with self.conn:
            self.c.execute(
                f"DELETE FROM {CategoryTable.TABLE_NAME} WHERE {CategoryTable.COLUMN_ID}=?", (_id,))

    def deletePointer(self, _id: int):
        with self.conn:
            self.c.execute(
                f"DELETE FROM {PointerTable.TABLE_NAME} WHERE {PointerTable.COLUMN_ID}=?", (_id,))

    def deleteStock(self, _id: int):
        with self.conn:
            self.c.execute(
                f"DELETE FROM {StockTable.TABLE_NAME} WHERE {StockTable.COLUMN_ID}=?", (_id,))

    def deleteSupplement(self, _id: int):
        with self.conn:
            self.c.execute(
                f"DELETE FROM {SupplementTable.TABLE_NAME} WHERE {SupplementTable.COLUMN_ID}=?", (_id,))

    def deleteSupplier(self, _id: int):
        with self.conn:
            self.c.execute(
                f"DELETE FROM {SupplierTable.TABLE_NAME} WHERE {SupplierTable.COLUMN_ID}=?", (_id,))

    def deleteExpenseCategory(self, _id: int):
        with self.conn:
            self.c.execute(
                f"DELETE FROM {ExpenseCategoryTable.TABLE_NAME} WHERE {ExpenseCategoryTable.COLUMN_ID}=?", (_id,))

    def deleteMenuCategory(self, _id: int):
        with self.conn:
            self.c.execute(
                f"DELETE FROM {MenuCategoryTable.TABLE_NAME} WHERE {MenuCategoryTable.COLUMN_ID}=?", (_id,))

    def deleteReservation(self, _id: int):
        with self.conn:
            self.c.execute(
                f"DELETE FROM {ReservationTable.TABLE_NAME} WHERE {ReservationTable.COLUMN_ID}=?", (_id,))

    def deleteWaste(self, _id: int):
        with self.conn:
            self.c.execute(
                f"DELETE FROM {WasteTable.TABLE_NAME} WHERE {WasteTable.COLUMN_ID}=?", (_id,))

    # Delete all

    def deleteAllExpenses(self):
        with self.conn:
            self.c.execute(f"DELETE FROM {ExpenseTable.TABLE_NAME}")

    def deleteAllMenus(self):
        with self.conn:
            self.c.execute(f"DELETE FROM {MenuTable.TABLE_NAME}")

    def deleteStock(self, _id: int):
        with self.conn:
            self.c.execute(
                f"DELETE FROM {StockTable.TABLE_NAME} WHERE {StockTable.COLUMN_ID}=?", (_id,))

    def deleteAllSupplements(self):
        with self.conn:
            self.c.execute(f"DELETE FROM {SupplementTable.TABLE_NAME}")

    def deleteAllSuppliers(self):
        with self.conn:
            self.c.execute(f"DELETE FROM {SupplierTable.TABLE_NAME}")

    def deleteAllCustomers(self):
        with self.conn:
            self.c.execute(f"DELETE FROM {CustomerTable.TABLE_NAME}")

    def deleteAllWorkers(self):
        with self.conn:
            self.c.execute(f"DELETE FROM {WorkerTable.TABLE_NAME}")

    def deleteAllSells(self):
        with self.conn:
            self.c.execute(f"DELETE FROM {SellTable.TABLE_NAME}")

    def deleteAllSellItems(self):
        with self.conn:
            self.c.execute(f"DELETE FROM {SellItemTable.TABLE_NAME}")

    def deleteAllSellItemSupplements(self):
        with self.conn:
            self.c.execute(f"DELETE FROM {SellItemSupplementTable.TABLE_NAME}")

    def deleteAllTables(self):
        with self.conn:
            self.c.execute(f"DELETE FROM {TableTable.TABLE_NAME}")

    def deleteAllCategories(self):
        with self.conn:
            self.c.execute(f"DELETE FROM {CategoryTable.TABLE_NAME}")

    def deleteAllPointers(self):
        with self.conn:
            self.c.execute(f"DELETE FROM {PointerTable.TABLE_NAME}")

    def deleteAllExpenseCategories(self):
        with self.conn:
            self.c.execute(f"DELETE FROM {ExpenseCategoryTable.TABLE_NAME}")

    def deleteAllMenuCategories(self):
        with self.conn:
            self.c.execute(f"DELETE FROM {MenuCategoryTable.TABLE_NAME}")

    def deleteAllReservations(self):
        with self.conn:
            self.c.execute(f"DELETE FROM {ReservationTable.TABLE_NAME}")

    def deleteAllWastes(self):
        with self.conn:
            self.c.execute(f"DELETE FROM {WasteTable.TABLE_NAME}")

    # Get all

    def getAllExpenses(self):
        with self.conn:
            self.c.execute(f"SELECT * FROM {ExpenseTable.TABLE_NAME}")
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    results.append(Expense(
                        x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[0]))
            return results

    def getAllMenus(self):
        with self.conn:
            self.c.execute(f"SELECT * FROM {MenuTable.TABLE_NAME}")
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    results.append(MenuItem(
                        x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[0]))
            return results

    def getAllMenusPhone(self):
        with self.conn:
            self.c.execute(f"SELECT * FROM {MenuTable.TABLE_NAME}")
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    results.append(MenuItemPhone(
                        x[1], x[2], x[3], x[4], x[5], x[6], x[7], "x[8]", self.getSupplementByMenuId(x[0]), x[0]))
            return results

    def getAllCustomers(self):
        with self.conn:
            self.c.execute(f"SELECT * FROM {CustomerTable.TABLE_NAME}")
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    results.append(
                        Customer(x[1], x[2], x[3], x[4], x[5], x[6], x[0]))
            return results

    def getAllWorkers(self):
        with self.conn:
            self.c.execute(f"SELECT * FROM {WorkerTable.TABLE_NAME}")
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    results.append(
                        Worker(x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[0]))
            return results

    def getAllSells(self):
        with self.conn:
            self.c.execute(f"SELECT * FROM {SellTable.TABLE_NAME}")
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    results.append(Sell(x[1], x[2], x[3], x[4], x[5], x[0]))
            return results

    def getAllSellItems(self):
        with self.conn:
            self.c.execute(f"SELECT * FROM {SellItemTable.TABLE_NAME}")
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    results.append(SellItem(x[1], x[2], x[3], x[4], x[0]))
            return results

    def getAllSellItemSupplements(self):
        with self.conn:
            self.c.execute(
                f"SELECT * FROM {SellItemSupplementTable.TABLE_NAME}")
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    results.append(SellItemSupplement(x[1], x[2], x[3], x[0]))
            return results

    def getAllTables(self):
        with self.conn:
            self.c.execute(f"SELECT * FROM {TableTable.TABLE_NAME}")
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    results.append(Table(x[0], x[1], x[2], x[3], x[4]))
            return results

    def getAllCategories(self):
        with self.conn:
            self.c.execute(f"SELECT * FROM {CategoryTable.TABLE_NAME}")
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    results.append(Category(x[1], x[2], x[0]))
            return results

    def getAllPointers(self):
        with self.conn:
            self.c.execute(f"SELECT * FROM {PointerTable.TABLE_NAME}")
            results = []
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    results.append(Pointer(x[1], x[2], x[3], x[0]))
            return results

    def getAllStocks(self):
        with self.conn:
            self.c.execute(f"SELECT * FROM {StockTable.TABLE_NAME}")
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    results.append(Stock(
                        x[1], x[2], x[3], x[4], x[0]))
            return results

    def getAllSupplements(self):
        with self.conn:
            self.c.execute(f"SELECT * FROM {SupplementTable.TABLE_NAME}")
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    results.append(Supplement(
                        x[1], x[2], x[3], x[4], x[0]))
            return results

    def getAllSuppliers(self):
        with self.conn:
            self.c.execute(f"SELECT * FROM {SupplierTable.TABLE_NAME}")
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    results.append(Supplier(
                        x[1], x[2], x[3], x[4], x[0]))
            return results

    def getAllExpenseCategories(self):
        with self.conn:
            self.c.execute(f"SELECT * FROM {ExpenseCategoryTable.TABLE_NAME}")
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    results.append(ExpenseCategory(
                        x[1], x[2], x[0]))
            return results

    def getAllMenuCategories(self):
        with self.conn:
            self.c.execute(f"SELECT * FROM {MenuCategoryTable.TABLE_NAME}")
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    results.append(MenuCategory(
                        x[1], x[2], x[0]))
            return results

    def getAllReservations(self):
        with self.conn:
            self.c.execute(f"SELECT * FROM {ReservationTable.TABLE_NAME}")
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    results.append(Reservation(
                        x[1], x[2], x[3], x[4], x[5], x[6], x[0]))
            return results

    def getAllWastes(self):
        with self.conn:
            self.c.execute(f"SELECT * FROM {WasteTable.TABLE_NAME}")
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    results.append(Waste(
                        x[1], x[2], x[3], x[4], x[5], x[6], x[0]))
            return results

    # Get by id

    def getExpenseById(self, _id: int):
        with self.conn:
            self.c.execute(
                f"SELECT * FROM {ExpenseTable.TABLE_NAME} WHERE {ExpenseTable.COLUMN_ID}=?", (_id,))
            x = self.c.fetchone()
            if x is not None:
                return Expense(x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[0])
            else:
                return x

    def getMenuItemById(self, _id: int):
        with self.conn:
            self.c.execute(
                f"SELECT * FROM {MenuTable.TABLE_NAME} WHERE {MenuTable.COLUMN_ID}=?", (_id,))
            x = self.c.fetchone()
            if x is not None:
                return MenuItem(x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[0])
            else:
                return x

    def getCustomerById(self, _id: int):
        with self.conn:
            self.c.execute(f"SELECT * FROM {CustomerTable.TABLE_NAME} WHERE {CustomerTable.COLUMN_ID}=?",
                           (_id,))
            x = self.c.fetchone()
            if x is not None:
                return Customer(x[1], x[2], x[3], x[4], x[5], x[6], x[0])
            else:
                return x

    def getWorkerById(self, _id: int):
        with self.conn:
            self.c.execute(f"SELECT * FROM {WorkerTable.TABLE_NAME} WHERE {WorkerTable.COLUMN_ID}=?",
                           (_id,))
            x = self.c.fetchone()
            if x is not None:
                return Worker(x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[0])
            else:
                return x

    def getSellById(self, _id: int):
        with self.conn:
            self.c.execute(f"SELECT * FROM {SellTable.TABLE_NAME} WHERE {SellTable.COLUMN_ID}=?",
                           (_id,))
            x = self.c.fetchone()
            if x is not None:
                return Sell(x[1], x[2], x[3], x[4], x[5], x[0])
            else:
                return x

    def getSellItemById(self, _id: int):
        with self.conn:
            self.c.execute(f"SELECT * FROM {SellItemTable.TABLE_NAME} WHERE {SellItemTable.COLUMN_ID}=?",
                           (_id,))
            x = self.c.fetchone()
            if x is not None:
                return SellItem(x[1], x[2], x[3], x[4], x[0])
            else:
                return x

    def getSellItemSupplementById(self, _id: int):
        with self.conn:
            self.c.execute(f"SELECT * FROM {SellItemSupplementTable.TABLE_NAME} WHERE {SellItemSupplementTable.COLUMN_ID}=?",
                           (_id,))
            x = self.c.fetchone()
            if x is not None:
                return SellItemSupplement(x[1], x[2], x[3], x[0])
            else:
                return x

    def getTableById(self, _id: int):
        with self.conn:
            self.c.execute(f"SELECT * FROM {TableTable.TABLE_NAME} WHERE {TableTable.COLUMN_ID}=?",
                           (_id,))
            x = self.c.fetchone()
            if x is not None:
                return Table(x[0], x[1], x[2], x[3], x[4])
            else:
                return x

    def getCategoryById(self, _id: int):
        with self.conn:
            self.c.execute(f"SELECT * FROM {CategoryTable.TABLE_NAME} WHERE {CategoryTable.COLUMN_ID}=?",
                           (_id,))
            x = self.c.fetchone()
            if x is not None:
                return Category(x[1], x[2], x[0])
            else:
                return x

    def getPointerById(self, _id: int):
        with self.conn:
            self.c.execute(f"SELECT * FROM {PointerTable.TABLE_NAME} WHERE {PointerTable.COLUMN_ID}=?",
                           (_id,))
            x = self.c.fetchone()
            if x is not None:
                return Pointer(x[1], x[2], x[3], x[0])
            else:
                return x

    def getStockById(self, _id: int):
        with self.conn:
            self.c.execute(
                f"SELECT * FROM {StockTable.TABLE_NAME} WHERE {StockTable.COLUMN_ID}=?", (_id,))
            x = self.c.fetchone()
            if x is not None:
                return Stock(x[1], x[2], x[3], x[4], x[0])
            else:
                return x

    def getSupplementById(self, _id: int):
        with self.conn:
            self.c.execute(
                f"SELECT * FROM {SupplementTable.TABLE_NAME} WHERE {SupplementTable.COLUMN_ID}=?", (_id,))
            x = self.c.fetchone()
            if x is not None:
                return Supplement(x[1], x[2], x[3], x[4], x[0])
            else:
                return x

    def getSupplierById(self, _id: int):
        with self.conn:
            self.c.execute(
                f"SELECT * FROM {SupplierTable.TABLE_NAME} WHERE {SupplierTable.COLUMN_ID}=?", (_id,))
            x = self.c.fetchone()
            if x is not None:
                return Supplier(x[1], x[2], x[3], x[4], x[0])
            else:
                return x

    def getExpenseCategoryById(self, _id: int):
        with self.conn:
            self.c.execute(
                f"SELECT * FROM {ExpenseCategoryTable.TABLE_NAME} WHERE {ExpenseCategoryTable.COLUMN_ID}=?", (_id,))
            x = self.c.fetchone()
            if x is not None:
                return ExpenseCategory(x[1], x[2], x[0])
            else:
                return x

    def getMenuCategoryById(self, _id: int):
        with self.conn:
            self.c.execute(
                f"SELECT * FROM {MenuCategoryTable.TABLE_NAME} WHERE {MenuCategoryTable.COLUMN_ID}=?", (_id,))
            x = self.c.fetchone()
            if x is not None:
                return MenuCategory(x[1], x[2], x[0])
            else:
                return x

    def getReservationById(self, _id: int):
        with self.conn:
            self.c.execute(
                f"SELECT * FROM {ReservationTable.TABLE_NAME} WHERE {ReservationTable.COLUMN_ID}=?", (_id,))
            x = self.c.fetchone()
            if x is not None:
                return Reservation(x[1], x[2], x[3], x[4], x[5], x[6], x[0])
            else:
                return x

    def getWasteById(self, _id: int):
        with self.conn:
            self.c.execute(
                f"SELECT * FROM {WasteTable.TABLE_NAME} WHERE {WasteTable.COLUMN_ID}=?", (_id,))
            x = self.c.fetchone()
            if x is not None:
                return Waste(x[1], x[2], x[3], x[4], x[5], x[6], x[0])
            else:
                return x

    # Update one

    def updateExpense(self, x: Expense):
        with self.conn:
            sql_command = f"""UPDATE {ExpenseTable.TABLE_NAME} SET {ExpenseTable.COLUMN_NAME}=?, 
                        {ExpenseTable.COLUMN_CATEGORY}=?, {ExpenseTable.COLUMN_UNIT}=?, {ExpenseTable.COLUMN_QUANTITY}=?, 
                        {ExpenseTable.COLUMN_PRICE}=?, {ExpenseTable.COLUMN_SUPPLIER_ID}=?, {ExpenseTable.COLUMN_DATE}=? 
                        WHERE {ExpenseTable.COLUMN_ID}=? """
            self.c.execute(sql_command, astuple(x))

    def updateMenuItem(self, x: MenuItem):
        with self.conn:
            sql_command = f"""UPDATE {MenuTable.TABLE_NAME} SET {MenuTable.COLUMN_NAME}=?, 
                        {MenuTable.COLUMN_CATEGORY}=?, {MenuTable.COLUMN_CATEGORY_ID}=?, {MenuTable.COLUMN_UNIT}=?, {MenuTable.COLUMN_QUANTITY}=?, 
                        {MenuTable.COLUMN_PRICE}=?, {MenuTable.COLUMN_AVAILABLE}=?, {MenuTable.COLUMN_PICTURE}=? 
                        WHERE {MenuTable.COLUMN_ID}=? """
            self.c.execute(sql_command, astuple(x))

    def updateCustomer(self, x: Customer):
        with self.conn:
            sql_command = f"""UPDATE {CustomerTable.TABLE_NAME} SET {CustomerTable.COLUMN_NAME}=?, 
                        {CustomerTable.COLUMN_PHONE}=?, {CustomerTable.COLUMN_ADDRESS}=?, 
                        {CustomerTable.COLUMN_SCORE}=?, {CustomerTable.COLUMN_PICTURE}=?, 
                        {CustomerTable.COLUMN_FACE}=? WHERE {CustomerTable.COLUMN_ID}=? """
            self.c.execute(sql_command, astuple(x))

    def updateWorker(self, x: Worker):
        with self.conn:
            sql_command = f"""UPDATE {WorkerTable.TABLE_NAME} SET {WorkerTable.COLUMN_NAME}=?, 
                        {WorkerTable.COLUMN_USERNAME}=?, {WorkerTable.COLUMN_PASSWORD}=?, 
                        {WorkerTable.COLUMN_PHONE}=?, {WorkerTable.COLUMN_ID_CATEGORY}=?, 
                        {WorkerTable.COLUMN_ADDRESS}=?, {WorkerTable.COLUMN_SALARY}=?, {WorkerTable.COLUMN_SCORE}=?, 
                        {WorkerTable.COLUMN_PICTURE}=?, {WorkerTable.COLUMN_FACE}=? 
                        WHERE {WorkerTable.COLUMN_ID}=? """
            self.c.execute(sql_command, astuple(x))

    def updateSell(self, x: Sell):
        with self.conn:
            sql_command = f"""UPDATE {SellTable.TABLE_NAME} SET {SellTable.COLUMN_ID_WORKER}=?, 
                        {SellTable.COLUMN_ID_CUSTOMER}=?, {SellTable.COLUMN_DATE}=?, 
                        {SellTable.COLUMN_TOTAL}=?, {SellTable.COLUMN_COMPLETED}=? WHERE {SellTable.COLUMN_ID}=? """
            self.c.execute(sql_command, astuple(x))

    def updateSellItem(self, x: SellItem):
        with self.conn:
            sql_command = f"""UPDATE {SellItemTable.TABLE_NAME} SET {SellItemTable.COLUMN_ID_PRODUCT}=?, 
                        {SellItemTable.COLUMN_ID_SELL}=?, {SellItemTable.COLUMN_QUANTITY}=?, 
                        {SellItemTable.COLUMN_TOTAL}=? WHERE {SellItemTable.COLUMN_ID}=? """
            self.c.execute(sql_command, astuple(x))

    def updateSellItemSupplement(self, x: SellItemSupplement):
        with self.conn:
            sql_command = f"""UPDATE {SellItemSupplementTable.TABLE_NAME} SET {SellItemSupplementTable.COLUMN_ID_SUPPLEMENT}=?, 
                        {SellItemSupplementTable.COLUMN_ID_SELL_ITEM}=?, {SellItemSupplementTable.COLUMN_PRICE}=? WHERE {SellItemSupplementTable.COLUMN_ID}=? """
            self.c.execute(sql_command, astuple(x))

    def updateTable(self, x: Table):
        with self.conn:
            sql_command = f"""UPDATE {TableTable.TABLE_NAME} SET {TableTable.COLUMN_ID}=?, 
                        {TableTable.COLUMN_NAME}=?, {TableTable.COLUMN_SEATS}=?, {TableTable.COLUMN_COMMENT}=?, 
                        {TableTable.COLUMN_ID_SELL}=? WHERE {TableTable.COLUMN_ID}=? """
            self.c.execute(sql_command, astuple(x) + (x.id,))

    def updateCategory(self, x: Category):
        with self.conn:
            sql_command = f"""UPDATE {CategoryTable.TABLE_NAME} SET {CategoryTable.COLUMN_NAME}=?, 
                        {CategoryTable.COLUMN_LEVEL}=? WHERE {CategoryTable.COLUMN_ID}=? """
            self.c.execute(sql_command, astuple(x))

    def updatePointer(self, x: Pointer):
        with self.conn:
            sql_command = f"""UPDATE {PointerTable.TABLE_NAME} SET {PointerTable.COLUMN_DATE_START}=?, 
                        {PointerTable.COLUMN_DATE_END}=?, {PointerTable.COLUMN_ID_WORKER}=?
                        WHERE {PointerTable.COLUMN_ID}=? """
            self.c.execute(sql_command, astuple(x))

    def updateStock(self, x: Stock):
        with self.conn:
            sql_command = f"""UPDATE {StockTable.TABLE_NAME} SET {StockTable.COLUMN_NAME}=?, 
                        {StockTable.COLUMN_CATEGORY}=?, {StockTable.COLUMN_UNIT}=?, {StockTable.COLUMN_QUANTITY}=? 
                        WHERE {StockTable.COLUMN_ID}=? """
            self.c.execute(sql_command, astuple(x))

    def updateSupplement(self, x: Supplement):
        with self.conn:
            sql_command = f"""UPDATE {SupplementTable.TABLE_NAME} SET {SupplementTable.COLUMN_NAME}=?, 
                        {SupplementTable.COLUMN_RELATED_ITEM_ID}=?, {SupplementTable.COLUMN_QUANTITY}=?, {SupplementTable.COLUMN_PRICE}=? 
                        WHERE {SupplementTable.COLUMN_ID}=? """
            self.c.execute(sql_command, astuple(x))

    def updateSupplier(self, x: Supplier):
        with self.conn:
            sql_command = f"""UPDATE {SupplierTable.TABLE_NAME} SET {SupplierTable.COLUMN_NAME}=?, 
                        {SupplierTable.COLUMN_PHONE}=?, {SupplierTable.COLUMN_ADDRESS}=?, {SupplierTable.COLUMN_MAIL}=? 
                        WHERE {SupplierTable.COLUMN_ID}=? """
            self.c.execute(sql_command, astuple(x))

    def updateExpenseCategory(self, x: ExpenseCategory):
        with self.conn:
            sql_command = f"""UPDATE {ExpenseCategoryTable.TABLE_NAME} SET {ExpenseCategoryTable.COLUMN_NAME}=?, 
                        {ExpenseCategoryTable.COLUMN_STOCK}=? WHERE {ExpenseCategoryTable.COLUMN_ID}=? """
            self.c.execute(sql_command, astuple(x))

    def updateMenuCategory(self, x: MenuCategory):
        with self.conn:
            sql_command = f"""UPDATE {MenuCategoryTable.TABLE_NAME} SET {MenuCategoryTable.COLUMN_NAME}=?, {MenuCategoryTable.COLUMN_PRINTING_PLACE}=? WHERE {MenuCategoryTable.COLUMN_ID}=? """
            self.c.execute(sql_command, astuple(x))

    def updateReservation(self, x: Reservation):
        with self.conn:
            sql_command = f"""UPDATE {ReservationTable.TABLE_NAME} SET {ReservationTable.COLUMN_NAME}=?, 
                        {ReservationTable.COLUMN_PHONE}=?, {ReservationTable.COLUMN_CUSTOMER_ID}=?, {ReservationTable.COLUMN_NB_PERSON}=?, 
                        {ReservationTable.COLUMN_TABLE_ID}=?, {ReservationTable.COLUMN_DATE}=? 
                        WHERE {ReservationTable.COLUMN_ID}=? """
            self.c.execute(sql_command, astuple(x))

    def updateWaste(self, x: Waste):
        with self.conn:
            sql_command = f"""UPDATE {WasteTable.TABLE_NAME} SET {WasteTable.COLUMN_WORKER_ID}=?, {WasteTable.COLUMN_NAME}=?,
                        {WasteTable.COLUMN_NAME}=?, {WasteTable.COLUMN_CATEGORY}=?, {WasteTable.COLUMN_QUANTITY}=?, 
                        {WasteTable.COLUMN_PRICE}=?, 
                        {WasteTable.COLUMN_DATE}=? 
                        WHERE {WasteTable.COLUMN_ID}=? """
            self.c.execute(sql_command, astuple(x))

    # Special Calls
    def getTableContent(self, _id: int):
        sql_command = f"""SELECT {TableTable.TABLE_NAME}.{TableTable.COLUMN_ID} as table_id, 
        {MenuTable.TABLE_NAME}.{MenuTable.COLUMN_ID} as product_id, 
        {MenuTable.TABLE_NAME}.{MenuTable.COLUMN_NAME},  
        {MenuTable.TABLE_NAME}.{MenuTable.COLUMN_CATEGORY_ID},
        {SellItemTable.TABLE_NAME}.{SellItemTable.COLUMN_ID}, 
        {SellItemTable.TABLE_NAME}.{SellItemTable.COLUMN_QUANTITY}, 
        {SellItemTable.TABLE_NAME}.{SellItemTable.COLUMN_TOTAL},  {SellTable.TABLE_NAME}.{SellTable.COLUMN_TOTAL}, {SellTable.TABLE_NAME}.{SellTable.COLUMN_ID}
        FROM {TableTable.TABLE_NAME}, {MenuTable.TABLE_NAME}, {SellItemTable.TABLE_NAME}, 
        {SellTable.TABLE_NAME} WHERE {TableTable.TABLE_NAME}.{TableTable.COLUMN_ID}=? AND 
        {TableTable.TABLE_NAME}.{TableTable.COLUMN_ID_SELL}={SellTable.TABLE_NAME}.{SellTable.COLUMN_ID} AND 
        {MenuTable.TABLE_NAME}.{MenuTable.COLUMN_ID}={SellItemTable.TABLE_NAME}.
        {SellItemTable.COLUMN_ID_PRODUCT} AND 
        {SellItemTable.TABLE_NAME}.{SellItemTable.COLUMN_ID_SELL}={SellTable.TABLE_NAME}.{SellTable.COLUMN_ID} AND 
        {SellTable.COLUMN_COMPLETED}=?"""
        with self.conn:
            self.c.execute(sql_command, (_id, 0))
            all_x = self.c.fetchall()
            results = []
            total = 0
            sell = None
            if all_x is not None:
                for x in all_x:
                    total = x[7]
                    sell = self.getSellById(x[8])
                    all_sup = self.getSellItemSupplementBySellItem(x[4])
                    results.append(
                        OrderItem(
                            tableId=x[0],
                            productId=x[1],
                            productName=x[2],
                            productCategory=x[3],
                            orderItemQuantity=x[5],
                            orderItemTotal=x[6],
                            orderItemSupplements=all_sup))
            return results, total, sell

    def getWorkerByUsername(self, username):
        with self.conn:
            self.c.execute(f"SELECT * FROM {WorkerTable.TABLE_NAME} WHERE {WorkerTable.COLUMN_USERNAME}=?",
                           (username,))
            x = self.c.fetchone()
            if x is not None:
                return Worker(x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[0])
            else:
                return x

    def deleteAllRelatedSellItems(self, _id: int):
        with self.conn:
            self.c.execute(
                f"DELETE FROM {SellItemTable.TABLE_NAME} WHERE {SellItemTable.COLUMN_ID_SELL}=?", (_id,))

    def deleteAllRelatedSellItemSupplements(self, _id: int):
        with self.conn:
            self.c.execute(
                f"DELETE FROM {SellItemSupplementTable.TABLE_NAME} WHERE {SellItemSupplementTable.COLUMN_ID_SELL_ITEM}=?", (_id,))

    def getAllUncompletedSells(self):
        with self.conn:
            self.c.execute(f"SELECT * FROM {SellTable.TABLE_NAME} WHERE "
                           f"{SellTable.TABLE_NAME}.{SellTable.COLUMN_COMPLETED}=?", (0,))
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    results.append(Sell(x[1], x[2], x[3], x[4], x[5], x[0]))
            return results

    def getAllHoldingSells(self):
        with self.conn:
            sql_command = f"""SELECT * FROM {SellTable.TABLE_NAME} 
                            WHERE {SellTable.TABLE_NAME}.{SellTable.COLUMN_ID} NOT IN 
                            (SELECT {TableTable.TABLE_NAME}.{TableTable.COLUMN_ID_SELL} FROM {TableTable.TABLE_NAME}
                            WHERE {TableTable.TABLE_NAME}.{TableTable.COLUMN_ID_SELL} NOT NULL) 
                            AND {SellTable.TABLE_NAME}.{SellTable.COLUMN_COMPLETED}=?"""
            self.c.execute(sql_command, (0,))
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    results.append(Sell(x[1], x[2], x[3], x[4], x[5], x[0]))
            return results

    def insertOrder(
            self,
            order_items: list,
            total: float,
            id_worker: int,
            id_customer: int,
            completed: int = 0):

        sell_id = self.insertSell(
            Sell(
                id_worker,
                id_customer,
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                total=total,
                completed=completed))
        if order_items[0].tableId is not None and completed == 0:
            table = self.getTableById(order_items[0].tableId)
            table.id_sell = sell_id
            self.updateTable(table)
        for item in order_items:
            sell_item_id = self.insertSellItem(
                SellItem(
                    id_product=item.productId,
                    id_sell=sell_id,
                    quantity=item.orderItemQuantity,
                    total=item.orderItemTotal))
            for sup in item.orderItemSupplements:
                self.insertSellItemSupplement(
                    SellItemSupplement(
                        id_supplement=sup.id,
                        id_sell_item=sell_item_id,
                        price=sup.price,
                    )
                )
        return sell_id

    def updateOrder(
            self,
            sell: Sell,
            order_items: list,
            completed: int = 0):
        self.updateSell(sell)
        if order_items[0].tableId is not None and completed == 0:
            table = self.getTableById(order_items[0].tableId)
            table.id_sell = sell.id
            self.updateTable(table)
        self.deleteSellContent(sell.id)
        for item in order_items:
            sell_item_id = self.insertSellItem(
                SellItem(
                    id_product=item.productId,
                    id_sell=sell.id,
                    quantity=item.orderItemQuantity,
                    total=item.orderItemTotal))
            for sup in item.orderItemSupplements:
                self.insertSellItemSupplement(
                    SellItemSupplement(
                        id_supplement=sup.id,
                        id_sell_item=sell_item_id,
                        price=sup.price,
                    )
                )

    def deleteSellContent(self, id_sell: int):
        with self.conn:
            self.c.execute(
                f"SELECT {SellItemTable.TABLE_NAME}.{SellItemTable.COLUMN_ID} FROM {SellItemTable.TABLE_NAME} WHERE {SellItemTable.COLUMN_ID_SELL}=?", (id_sell,))
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for id_sell_item in results:
                    self.c.execute(
                        f"DELETE FROM {SellItemSupplementTable.TABLE_NAME} WHERE {SellItemSupplementTable.COLUMN_ID_SELL_ITEM}=?", (
                            id_sell_item,)
                    )
            self.c.execute(
                f"DELETE FROM {SellItemTable.TABLE_NAME} WHERE {SellItemTable.COLUMN_ID_SELL}=?", (
                    id_sell,)
            )

    def getUncompletedOrdersBySellId(self, _id):
        sql_command = f"""SELECT NULL, 
                {MenuTable.TABLE_NAME}.{MenuTable.COLUMN_ID} as product_id, 
                {MenuTable.TABLE_NAME}.{MenuTable.COLUMN_NAME},  
                {MenuTable.TABLE_NAME}.{MenuTable.COLUMN_CATEGORY},
                {SellItemTable.TABLE_NAME}.{SellItemTable.COLUMN_ID},
                {SellItemTable.TABLE_NAME}.{SellItemTable.COLUMN_QUANTITY}, 
                {SellItemTable.TABLE_NAME}.{SellItemTable.COLUMN_TOTAL}, {SellTable.TABLE_NAME}.{SellTable.COLUMN_TOTAL} 
                FROM {MenuTable.TABLE_NAME}, {SellItemTable.TABLE_NAME}, 
                {SellTable.TABLE_NAME} WHERE {SellTable.TABLE_NAME}.{SellTable.COLUMN_ID}=? AND
                {MenuTable.TABLE_NAME}.{MenuTable.COLUMN_ID}={SellItemTable.TABLE_NAME}.
                {SellItemTable.COLUMN_ID_PRODUCT} AND 
                {SellItemTable.TABLE_NAME}.{SellItemTable.COLUMN_ID_SELL}={SellTable.TABLE_NAME}.
                {SellTable.COLUMN_ID} AND 
                {SellTable.COLUMN_COMPLETED}=?"""
        with self.conn:
            self.c.execute(sql_command, (_id, 0))
            all_x = self.c.fetchall()
        results = []
        total = 0
        if all_x is not None:
            for x in all_x:
                all_sup = self.getSellItemSupplementBySellItem(x[4])
                results.append(
                    OrderItem(x[0], x[1], x[2], x[3], x[5], x[6], all_sup))
                total = x[7]
        return results, total

    def getUncompletedOrders(self):
        sql_command = f"""SELECT {TableTable.TABLE_NAME}.{TableTable.COLUMN_ID} as table_id, 
                {MenuTable.TABLE_NAME}.{MenuTable.COLUMN_ID} as product_id, 
                {MenuTable.TABLE_NAME}.{MenuTable.COLUMN_NAME},  
                {MenuTable.TABLE_NAME}.{MenuTable.COLUMN_CATEGORY},
                {SellItemTable.TABLE_NAME}.{SellItemTable.COLUMN_ID},
                {SellItemTable.TABLE_NAME}.{SellItemTable.COLUMN_QUANTITY}, 
                {SellItemTable.TABLE_NAME}.{SellItemTable.COLUMN_TOTAL} 
                FROM {TableTable.TABLE_NAME}, {MenuTable.TABLE_NAME}, {SellItemTable.TABLE_NAME}, 
                {SellTable.TABLE_NAME} WHERE
                {MenuTable.TABLE_NAME}.{MenuTable.COLUMN_ID}={SellItemTable.TABLE_NAME}.
                {SellItemTable.COLUMN_ID_PRODUCT} AND 
                {SellItemTable.TABLE_NAME}.{SellItemTable.COLUMN_ID_SELL}={SellTable.TABLE_NAME}.{SellTable.COLUMN_ID} AND 
                {SellTable.COLUMN_COMPLETED}=?"""
        with self.conn:
            self.c.execute(sql_command, (0,))
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    all_sup = self.getSellItemSupplementBySellItem(x[3])
                    results.append(
                        OrderItem(x[0], x[1], x[2], x[4], x[5], x[6], all_sup))
            return results

    def getHomeScreenInfo(self, month_date: str, day_date: str):
        sql_command = "SELECT count(*) FROM Tables WHERE id_sell IS NULL"
        with self.conn:
            self.c.execute(sql_command)
            nb_free_tables = self.c.fetchone()
        sql_command = "SELECT count(*) FROM Tables WHERE id_sell IS NOT NULL"
        with self.conn:
            self.c.execute(sql_command)
            nb_busy_tables = self.c.fetchone()
        sql_command = "SELECT count(*) FROM Sells WHERE date >=?"
        with self.conn:
            self.c.execute(sql_command, (month_date,))
            nb_month_sells = self.c.fetchone()
        sql_command = "SELECT count(*) FROM Sells WHERE date >=?"
        with self.conn:
            self.c.execute(sql_command, (day_date,))
            nb_day_sells = self.c.fetchone()
        return nb_free_tables, nb_busy_tables, nb_month_sells, nb_day_sells

    def getStockByNameCat(self, name: str, category: str):
        with self.conn:
            self.c.execute(
                f"SELECT * FROM {StockTable.TABLE_NAME} WHERE {StockTable.COLUMN_NAME}=? AND {StockTable.COLUMN_CATEGORY}=?", (name, category))
            x = self.c.fetchone()
            if x is not None:
                return Stock(x[1], x[2], x[3], x[4], x[0])
            else:
                return x

    def getSupplementByMenuId(self, _id: int):
        with self.conn:
            self.c.execute(
                f"SELECT * FROM {SupplementTable.TABLE_NAME} WHERE {SupplementTable.COLUMN_RELATED_ITEM_ID}=?", (_id,))
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    results.append(Supplement(
                        x[1], x[2], x[3], x[4], x[0]))
            return results

    def getSellItemSupplementBySellItem(self, sell_item_id: int):
        with self.conn:
            self.c.execute(
                f"SELECT * FROM {SellItemSupplementTable.TABLE_NAME} WHERE {SellItemSupplementTable.COLUMN_ID_SELL_ITEM}=?", (sell_item_id,))
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    results.append(self.getSupplementById(
                        x[1]))
            return results

    def getExpenseByNameCat(self, name: str, category: int):
        with self.conn:
            self.c.execute(
                f"SELECT * FROM {ExpenseTable.TABLE_NAME} WHERE {ExpenseTable.COLUMN_NAME}=? AND {ExpenseTable.COLUMN_CATEGORY}=?", (name, category))
            x = self.c.fetchone()
            if x is not None:
                return Expense(x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[0])
            else:
                return x

    # Search
    def customSearchSingle(self, table_name, table_field, value):
        with self.conn:
            self.c.execute(
                f"SELECT * FROM {table_name} WHERE {table_field}=?", (value,))
            return self.c.fetchall()

    def getReservationByName(self, name: str):
        name = f"%{name}%"
        with self.conn:
            self.c.execute(
                f"SELECT * FROM {ReservationTable.TABLE_NAME} WHERE {ReservationTable.COLUMN_NAME} LIKE ?", (name,))
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    results.append(Reservation(
                        x[1], x[2], x[3], x[4], x[5], x[6], x[0]))
            return results

    def getReservationByPhone(self, phone: str):
        phone = f"{phone}%"
        with self.conn:
            self.c.execute(
                f"SELECT * FROM {ReservationTable.TABLE_NAME} WHERE {ReservationTable.COLUMN_PHONE} LIKE ?", (phone,))
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    results.append(Reservation(
                        x[1], x[2], x[3], x[4], x[5], x[6], x[0]))
            return results

    def getReservationByDate(self, selected_date: str):
        with self.conn:
            self.c.execute(
                f"SELECT * FROM {ReservationTable.TABLE_NAME} WHERE {ReservationTable.COLUMN_DATE}>=?", (selected_date,))
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    results.append(Reservation(
                        x[1], x[2], x[3], x[4], x[5], x[6], x[0]))
            return results
