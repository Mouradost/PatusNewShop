from DB.DbTables import *
from DB.DBHandler import DBHelper
ticket_number = 24

db = DBHelper()
order_items = [OrderItem(tableId=2, productId=2, productName='ttttt', productCategory=2, productUnit='t', orderItemQuantity=17.0,
                         orderItemTotal=8500.0, orderItemSupplements=[], group_id=1, nb_covers=2, ready=0, served=0, id=177)]


ticket_kitchen, ticket_pizza, ticket_bar, kitchen_count, pizza_count, drink_count = "", "", "", 0, 0, 0
print(order_items)
print("*"*100)
sell = db.getSellById(ticket_number)
print(sell)
print("*" * 100)
sell_items = db.getSellItemBySellId(sell.id)
print(sell_items)
print("*"*100)
print(db.getOrderBySellId(sell_id=ticket_number))
