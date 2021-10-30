import sqlite3 as sql
from DB.ShopDbInfo import *
from dataclasses import astuple
from DB.DbTables import *
import datetime


class DBHelper(object):
    DATABASE_NAME = "Shop.db"
    DATABASE_VERSION = 1

    def __init__(self):
        self.conn = sql.connect(DBHelper.DATABASE_NAME, check_same_thread=True)
        self.c = self.conn.cursor()

    def createTables(self):
        with self.conn:
            sql_command = f"""CREATE TABLE IF NOT EXISTS {FinishProductTable.TABLE_NAME} 
                         ( {FinishProductTable.COLUMN_ID} INTEGER PRIMARY KEY AUTOINCREMENT, 
                        {FinishProductTable.COLUMN_NAME} TEXT NOT NULL,  
                        {FinishProductTable.COLUMN_CATEGORY} TEXT NOT NULL,  
                        {FinishProductTable.COLUMN_QUANTITY} REAL NOT NULL,  
                        {FinishProductTable.COLUMN_PRICE} REAL NOT NULL,  
                        {FinishProductTable.COLUMN_PICTURE} BLOB )"""
            self.c.execute(sql_command)

            sql_command = f"""CREATE TABLE IF NOT EXISTS {RawProductTable.TABLE_NAME} 
                                     ( {RawProductTable.COLUMN_ID} INTEGER PRIMARY KEY AUTOINCREMENT, 
                                    {RawProductTable.COLUMN_NAME} TEXT NOT NULL,  
                                    {RawProductTable.COLUMN_CATEGORY} TEXT NOT NULL,  
                                    {RawProductTable.COLUMN_QUANTITY} REAL NOT NULL,  
                                    {RawProductTable.COLUMN_PRICE} REAL NOT NULL )"""
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
                                     {FinishProductTable.TABLE_NAME} ({FinishProductTable.COLUMN_ID}) )"""
            self.c.execute(sql_command)

            sql_command = f"""CREATE TABLE IF NOT EXISTS {TableTable.TABLE_NAME} 
                                     ( {TableTable.COLUMN_ID} INTEGER PRIMARY KEY, 
                                    {TableTable.COLUMN_NAME} TEXT NOT NULL,  
                                    {TableTable.COLUMN_SEATS} INTEGER NOT NULL,  
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
    def insertFinishProduct(self, x: FinishProduct):
        with self.conn:
            sql_command = f"""INSERT INTO {FinishProductTable.TABLE_NAME} ({FinishProductTable.COLUMN_NAME}, 
                            {FinishProductTable.COLUMN_CATEGORY}, {FinishProductTable.COLUMN_QUANTITY}, 
                            {FinishProductTable.COLUMN_PRICE}, {FinishProductTable.COLUMN_PICTURE}) 
                            VALUES (?, ?, ?, ?, ?)"""
            self.c.execute(sql_command, astuple(x)[:-1])

    def insertRawProduct(self, x: RawProduct):
        with self.conn:
            sql_command = f"""INSERT INTO {RawProductTable.TABLE_NAME} ({RawProductTable.COLUMN_NAME}, 
                            {RawProductTable.COLUMN_CATEGORY}, {RawProductTable.COLUMN_QUANTITY}, 
                            {RawProductTable.COLUMN_PRICE}) 
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
                            {WorkerTable.COLUMN_ID_CATEGORY}, {WorkerTable.COLUMN_ADDRESS}, 
                            {WorkerTable.COLUMN_SCORE}, {WorkerTable.COLUMN_PICTURE}, 
                            {WorkerTable.COLUMN_FACE}) 
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
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

    def insertTable(self, x: Table):
        with self.conn:
            sql_command = f"""INSERT INTO {TableTable.TABLE_NAME} ({TableTable.COLUMN_ID}, {TableTable.COLUMN_NAME}, 
                            {TableTable.COLUMN_SEATS}, {TableTable.COLUMN_ID_SELL}) 
                            VALUES (?, ?, ?, ?)"""
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

    # Delete one
    def deleteFinishProduct(self, _id: int):
        with self.conn:
            self.c.execute(f"DELETE FROM {FinishProductTable.TABLE_NAME} WHERE {FinishProductTable.COLUMN_ID}=?",
                           (_id,))

    def deleteRawProduct(self, _id: int):
        with self.conn:
            self.c.execute(f"DELETE FROM {RawProductTable.TABLE_NAME} WHERE {RawProductTable.COLUMN_ID}=?", (_id,))

    def deleteCustomer(self, _id: int):
        with self.conn:
            self.c.execute(f"DELETE FROM {CustomerTable.TABLE_NAME} WHERE {CustomerTable.COLUMN_ID}=?", (_id,))

    def deleteWorker(self, _id: int):
        with self.conn:
            self.c.execute(f"DELETE FROM {WorkerTable.TABLE_NAME} WHERE {WorkerTable.COLUMN_ID}=?", (_id,))

    def deleteSell(self, _id: int):
        with self.conn:
            self.c.execute(f"DELETE FROM {SellTable.TABLE_NAME} WHERE {SellTable.COLUMN_ID}=?", (_id,))

    def deleteSellItem(self, _id: int):
        with self.conn:
            self.c.execute(f"DELETE FROM {SellItemTable.TABLE_NAME} WHERE {SellItemTable.COLUMN_ID}=?", (_id,))

    def deleteTable(self, _id: int):
        with self.conn:
            self.c.execute(f"DELETE FROM {TableTable.TABLE_NAME} WHERE {TableTable.COLUMN_ID}=?", (_id,))

    def deleteCategory(self, _id: int):
        with self.conn:
            self.c.execute(f"DELETE FROM {CategoryTable.TABLE_NAME} WHERE {CategoryTable.COLUMN_ID}=?", (_id,))

    def deletePointer(self, _id: int):
        with self.conn:
            self.c.execute(f"DELETE FROM {PointerTable.TABLE_NAME} WHERE {PointerTable.COLUMN_ID}=?", (_id,))

    # Delete all
    def deleteAllFinishProducts(self):
        with self.conn:
            self.c.execute(f"DELETE FROM {FinishProductTable.TABLE_NAME}")

    def deleteAllRawProducts(self):
        with self.conn:
            self.c.execute(f"DELETE FROM {RawProductTable.TABLE_NAME}")

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

    def deleteAllTables(self):
        with self.conn:
            self.c.execute(f"DELETE FROM {TableTable.TABLE_NAME}")

    def deleteAllCategories(self):
        with self.conn:
            self.c.execute(f"DELETE FROM {CategoryTable.TABLE_NAME}")

    def deleteAllPointers(self):
        with self.conn:
            self.c.execute(f"DELETE FROM {PointerTable.TABLE_NAME}")

    # Get all
    def getAllFinishProducts(self):
        with self.conn:
            self.c.execute(f"SELECT * FROM {FinishProductTable.TABLE_NAME}")
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    results.append(FinishProduct(x[1], x[2], x[3], x[4], x[5], x[0]))
            return results

    def getAllRawProducts(self):
        with self.conn:
            self.c.execute(f"SELECT * FROM {RawProductTable.TABLE_NAME}")
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    results.append(RawProduct(x[1], x[2], x[3], x[4], x[0]))
            return results

    def getAllCustomers(self):
        with self.conn:
            self.c.execute(f"SELECT * FROM {CustomerTable.TABLE_NAME}")
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    results.append(Customer(x[1], x[2], x[3], x[4], x[5], x[6], x[0]))
            return results

    def getAllWorkers(self):
        with self.conn:
            self.c.execute(f"SELECT * FROM {WorkerTable.TABLE_NAME}")
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    results.append(Worker(x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[0]))
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

    def getAllTables(self):
        with self.conn:
            self.c.execute(f"SELECT * FROM {TableTable.TABLE_NAME}")
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    results.append(Table(x[0], x[1], x[2], x[3]))
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

    # Get by id
    def getFinishProductById(self, _id: int):
        with self.conn:
            self.c.execute(f"SELECT * FROM {FinishProductTable.TABLE_NAME} WHERE {FinishProductTable.COLUMN_ID}=?",
                           (_id,))
            x = self.c.fetchone()
            if x is not None:
                return FinishProduct(x[1], x[2], x[3], x[4], x[5], x[0])
            else:
                return x

    def getRawProductById(self, _id: int):
        with self.conn:
            self.c.execute(f"SELECT * FROM {RawProductTable.TABLE_NAME} WHERE {RawProductTable.COLUMN_ID}=?",
                           (_id,))
            x = self.c.fetchone()
            if x is not None:
                return RawProduct(x[1], x[2], x[3], x[4], x[0])
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
                return Worker(x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[0])
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

    def getTableById(self, _id: int):
        with self.conn:
            self.c.execute(f"SELECT * FROM {TableTable.TABLE_NAME} WHERE {TableTable.COLUMN_ID}=?",
                           (_id,))
            x = self.c.fetchone()
            if x is not None:
                return Table(x[0], x[1], x[2], x[3])
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

    # Update one
    def updateFinishProduct(self, x: FinishProduct):
        with self.conn:
            sql_command = f"""UPDATE {FinishProductTable.TABLE_NAME} SET {FinishProductTable.COLUMN_NAME}=?, 
                        {FinishProductTable.COLUMN_CATEGORY}=?, {FinishProductTable.COLUMN_QUANTITY}=?, 
                        {FinishProductTable.COLUMN_PRICE}=?, {FinishProductTable.COLUMN_PICTURE}=? 
                        WHERE {FinishProductTable.COLUMN_ID}=? """
            self.c.execute(sql_command, astuple(x))

    def updateRawProduct(self, x: RawProduct):
        with self.conn:
            sql_command = f"""UPDATE {RawProductTable.TABLE_NAME} SET {RawProductTable.COLUMN_NAME}=?, 
                        {RawProductTable.COLUMN_CATEGORY}=?, {RawProductTable.COLUMN_QUANTITY}=?, 
                        {RawProductTable.COLUMN_PRICE}=? WHERE {RawProductTable.COLUMN_ID}=? """
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
                        {WorkerTable.COLUMN_ADDRESS}=?, {WorkerTable.COLUMN_SCORE}=?, 
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

    def updateTable(self, x: Table):
        with self.conn:
            sql_command = f"""UPDATE {TableTable.TABLE_NAME} SET {TableTable.COLUMN_ID}=?, 
                        {TableTable.COLUMN_NAME}=?, {TableTable.COLUMN_SEATS}=?, 
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

    # Special Calls
    def getTableContent(self, _id: int):
        sql_command = f"""SELECT {TableTable.TABLE_NAME}.{TableTable.COLUMN_ID} as table_id, 
        {FinishProductTable.TABLE_NAME}.{FinishProductTable.COLUMN_ID} as product_id, 
        {FinishProductTable.TABLE_NAME}.{FinishProductTable.COLUMN_NAME},  
        {FinishProductTable.TABLE_NAME}.{FinishProductTable.COLUMN_CATEGORY},
        {SellItemTable.TABLE_NAME}.{SellItemTable.COLUMN_QUANTITY}, 
        {SellItemTable.TABLE_NAME}.{SellItemTable.COLUMN_TOTAL},  {SellTable.TABLE_NAME}.{SellTable.COLUMN_TOTAL}
        FROM {TableTable.TABLE_NAME}, {FinishProductTable.TABLE_NAME}, {SellItemTable.TABLE_NAME}, 
        {SellTable.TABLE_NAME} WHERE {TableTable.TABLE_NAME}.{TableTable.COLUMN_ID}=? AND 
        {TableTable.TABLE_NAME}.{TableTable.COLUMN_ID_SELL}={SellTable.TABLE_NAME}.{SellTable.COLUMN_ID} AND 
        {FinishProductTable.TABLE_NAME}.{FinishProductTable.COLUMN_ID}={SellItemTable.TABLE_NAME}.
        {SellItemTable.COLUMN_ID_PRODUCT} AND 
        {SellItemTable.TABLE_NAME}.{SellItemTable.COLUMN_ID_SELL}={SellTable.TABLE_NAME}.{SellTable.COLUMN_ID} AND 
        {SellTable.COLUMN_COMPLETED}=?"""
        with self.conn:
            self.c.execute(sql_command, (_id, 0))
            all_x = self.c.fetchall()
            results = []
            total = 0
            if all_x is not None:
                for x in all_x:
                    total = x[6]
                    results.append(OrderItem(x[0], x[1], x[2], x[3], x[4], x[5]))
            return results, total

    def getWorkerByUsername(self, username):
        with self.conn:
            self.c.execute(f"SELECT * FROM {WorkerTable.TABLE_NAME} WHERE {WorkerTable.COLUMN_USERNAME}=?",
                           (username,))
            x = self.c.fetchone()
            if x is not None:
                return Worker(x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[0])
            else:
                return x

    def deleteAllRelatedSellItems(self, _id: int):
        with self.conn:
            self.c.execute(f"DELETE FROM {SellItemTable.TABLE_NAME} WHERE {SellItemTable.COLUMN_ID_SELL}=?", (_id,))

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

    def insertOrder(self, order_items: list, total: float, id_worker: int, id_customer: int, completed: int = 0):
        sell_id = self.insertSell(Sell(id_worker, id_customer, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                       total=total, completed=completed))
        if order_items[0].tableId is not None and completed == 0:
            table = self.getTableById(order_items[0].tableId)
            print(f"add order to table {table.id}")
            table.id_sell = sell_id
            self.updateTable(table)
        for item in order_items:
            self.insertSellItem(SellItem(item.productId, sell_id, item.orderItemQuantity, item.orderItemTotal))

    def getUncompletedOrdersBySellId(self, _id):
        sql_command = f"""SELECT NULL, 
                {FinishProductTable.TABLE_NAME}.{FinishProductTable.COLUMN_ID} as product_id, 
                {FinishProductTable.TABLE_NAME}.{FinishProductTable.COLUMN_NAME},  
                {FinishProductTable.TABLE_NAME}.{FinishProductTable.COLUMN_CATEGORY},
                {SellItemTable.TABLE_NAME}.{SellItemTable.COLUMN_QUANTITY}, 
                {SellItemTable.TABLE_NAME}.{SellItemTable.COLUMN_TOTAL}, {SellTable.TABLE_NAME}.{SellTable.COLUMN_TOTAL} 
                FROM {FinishProductTable.TABLE_NAME}, {SellItemTable.TABLE_NAME}, 
                {SellTable.TABLE_NAME} WHERE {SellTable.TABLE_NAME}.{SellTable.COLUMN_ID}=? AND
                {FinishProductTable.TABLE_NAME}.{FinishProductTable.COLUMN_ID}={SellItemTable.TABLE_NAME}.
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
                    results.append(OrderItem(x[0], x[1], x[2], x[3], x[4], x[5]))
                    total = x[6]
            return results, total

    def getUncompletedOrders(self):
        sql_command = f"""SELECT {TableTable.TABLE_NAME}.{TableTable.COLUMN_ID} as table_id, 
                {FinishProductTable.TABLE_NAME}.{FinishProductTable.COLUMN_ID} as product_id, 
                {FinishProductTable.TABLE_NAME}.{FinishProductTable.COLUMN_NAME},  
                {FinishProductTable.TABLE_NAME}.{FinishProductTable.COLUMN_CATEGORY},
                {SellItemTable.TABLE_NAME}.{SellItemTable.COLUMN_QUANTITY}, 
                {SellItemTable.TABLE_NAME}.{SellItemTable.COLUMN_TOTAL} 
                FROM {TableTable.TABLE_NAME}, {FinishProductTable.TABLE_NAME}, {SellItemTable.TABLE_NAME}, 
                {SellTable.TABLE_NAME} WHERE
                {FinishProductTable.TABLE_NAME}.{FinishProductTable.COLUMN_ID}={SellItemTable.TABLE_NAME}.
                {SellItemTable.COLUMN_ID_PRODUCT} AND 
                {SellItemTable.TABLE_NAME}.{SellItemTable.COLUMN_ID_SELL}={SellTable.TABLE_NAME}.{SellTable.COLUMN_ID} AND 
                {SellTable.COLUMN_COMPLETED}=?"""
        with self.conn:
            self.c.execute(sql_command, (0,))
            all_x = self.c.fetchall()
            results = []
            if all_x is not None:
                for x in all_x:
                    results.append(OrderItem(x[0], x[1], x[2], x[3], x[4], x[5]))
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
