from DB.DbTables import *
from DB.DBHandler import DBHelper
import hashlib


if __name__ == '__main__':
    db = DBHelper()

    print(db.getAllHoldingSells())
    print("***"*100)
    # print(db.insertSell(Sell(1, 1, "2021-08-24 12:13:00", 480., 0)))

    """db.createTables()
    
    # Insertion
    # FinishProducts
    db.insertFinishProduct(FinishProduct("Burger", "Meal", 0, 200.))
    db.insertFinishProduct(FinishProduct("Pasta", "Meal", 0, 280.))

    db.insertFinishProduct(FinishProduct("Napolitane", "Pizza", 0, 400.))
    db.insertFinishProduct(FinishProduct("Four seasons", "Pizza", 0, 460.))

    db.insertFinishProduct(FinishProduct("Chocolate Cake", "Dessert", 0, 250.))
    db.insertFinishProduct(FinishProduct("Tart", "Dessert", 0, 350.))

    db.insertFinishProduct(FinishProduct("Coca Cola", "Cold Drink", 0, 50.))
    db.insertFinishProduct(FinishProduct("Fanta", "Cold Drink", 0, 60.))

    db.insertFinishProduct(FinishProduct("Coffee", "Hot Drink", 0, 150.))
    db.insertFinishProduct(FinishProduct("Tea", "Hot Drink", 0, 120.))

    # RawProducts
    db.insertRawProduct(RawProduct("tomato", "vegetable"))
    db.insertRawProduct(RawProduct("carrot", "vegetable"))
    db.insertRawProduct(RawProduct("beef", "meat"))
    db.insertRawProduct(RawProduct("chicken", "meat"))

    # Customers
    db.insertCustomer(Customer("customer 1"))
    db.insertCustomer(Customer("customer 2"))

    # Workers
    db.insertWorker(Worker("worker 1", "worker 1", hashlib.sha3_512("123".encode()).hexdigest(), id_category=1))
    db.insertWorker(Worker("worker 3", "worker 2", hashlib.sha3_512("123".encode()).hexdigest(), id_category=2))
    db.insertWorker(Worker("worker 2", "worker 3", hashlib.sha3_512("123".encode()).hexdigest(), id_category=3))

    # Sells
    db.insertSell(Sell(1, 1, "2021-08-24 12:13:00", 480., 0))
    db.insertSell(Sell(1, 2, "2021-08-24 13:13:00", 10, 0))
    db.insertSell(Sell(2, 1, "2021-08-24 10:13:00", 10, 0))
    db.insertSell(Sell(3, 2, "2021-08-24 11:13:00", 10, 1))

    # SellItem
    db.insertSellItem(SellItem(1, 1, 1, 10))
    db.insertSellItem(SellItem(2, 1, 2, 10))
    db.insertSellItem(SellItem(4, 1, 1, 460.))

    db.insertSellItem(SellItem(5, 2, 10, 10))
    db.insertSellItem(SellItem(1, 2, 10, 10))

    db.insertSellItem(SellItem(7, 3, 10, 10))

    db.insertSellItem(SellItem(3, 4, 10, 10))

    # Tables
    db.insertTable(Table(1, "table 1", 2, 1))
    db.insertTable(Table(2, "table 2", 4, 2))
    db.insertTable(Table(3, "table 3", 4, 3))
    db.insertTable(Table(4, "table 4", 6))
    db.insertTable(Table(5, "table 5", 6))

    # Category
    db.insertCategory(Category("boss", 0))
    db.insertCategory(Category("waiter", 2))
    db.insertCategory(Category("manager", 1))

    # Pointer
    db.insertPointer(Pointer("2021-08-12 12:30:00", "2021-08-12 18:30:00", 1))

    # Get by id
    print(db.getFinishProductById(1))
    print(db.getRawProductById(1))
    print(db.getCustomerById(1))
    print(db.getWorkerById(1))
    print(db.getSellById(1))
    print(db.getSellItemById(1))
    print(db.getTableById(0))
    print(db.getCategoryById(1))
    print(db.getPointerById(1))

    # Get all
    print(db.getAllFinishProducts())
    print(db.getAllRawProducts())
    print(db.getAllCustomers())
    print(db.getAllWorkers())
    print(db.getAllSells())
    print(db.getAllSellItems())
    print(db.getAllTables())
    print(db.getAllCategories())
    print(db.getAllPointers())

    # Delete one
    print(db.deleteFinishProduct(1))
    print(db.deleteRawProduct(1))
    print(db.deleteCustomer(1))
    print(db.deleteWorker(1))
    print(db.deleteSell(1))
    print(db.deleteSellItem(1))
    print(db.deleteTable(0))
    print(db.deleteCategory(1))
    print(db.deletePointer(1))

    # Delete all
    print(db.deleteAllFinishProducts())
    print(db.deleteAllRawProducts())
    print(db.deleteAllCustomers())
    print(db.deleteAllWorkers())
    print(db.deleteAllSells())
    print(db.deleteAllSellItems())
    print(db.deleteAllTables())
    print(db.deleteAllCategories())
    print(db.deleteAllPointers())

    # Update
    fp = db.getFinishProductById(4)
    rp = db.getRawProductById(4)
    c = db.getCustomerById(4)
    w = db.getWorkerById(4)
    s = db.getSellById(4)
    si = db.getSellItemById(4)
    t = db.getTableById(1)
    cat = db.getCategoryById(3)
    p = db.getPointerById(3)
    
    print(db.updateFinishProduct(fp))
    print(db.updateRawProduct(rp))
    print(db.updateCustomer(c))
    print(db.updateWorker(w))
    print(db.updateSell(s))
    print(db.updateSellItem(si))
    print(db.updateTable(t))
    print(db.updateCategory(cat))
    print(db.updatePointer(p))
    """