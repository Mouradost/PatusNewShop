from dataclasses import dataclass
import datetime
import json

from attr import asdict


@dataclass
class Expense(object):
    name: str
    category: int
    unit: str = ""
    quantity: float = 0
    price: float = 0
    supplier_id: int = None
    date: str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    id: int = None


@dataclass
class MenuItem(object):
    name: str
    category: str
    category_id: int = None
    unit: str = ""
    quantity: float = 0
    price: float = 0
    available: bool = True
    picture: object = None
    id: int = None


@dataclass
class MenuItemPhone(object):
    name: str
    category: str
    category_id: int = None
    unit: str = ""
    quantity: float = 0
    price: float = 0
    available: bool = True
    picture: str = None
    supplements: list = None
    id: int = None

    def toJson(self):
        if self.supplements is None:
            self.supplements = []

        return {
            'name': self.name,
            'category': self.category,
            'category_id': self.category_id,
            'unit': self.unit,
            'price': self.price,
            "available": self.available,
            "picture": self.picture,
            "supplements": [x.toJson() for x in self.supplements],
            "id": self.id
        }


@dataclass
class Supplement(object):
    name: str
    related_item_id: int = None
    quantity: float = 0
    price: float = 0
    id: int = None

    def toJson(self):
        return {
            "name": self.name,
            "related_item_id": self.related_item_id,
            "quantity": self.quantity,
            "price": self.price,
            "id": self.id
        }


# print(MenuItemPhone("", "").toJson())


@dataclass
class Stock(object):
    name: str
    category: int
    unit: str
    quantity: float = 0
    id: int = None


@dataclass
class Customer:
    name: str
    phone: str = None
    address: str = ""
    score: float = 0
    picture: object = None
    face: object = None
    id: int = None


@dataclass
class Supplier(object):
    name: str
    phone: str = None
    address: str = None
    mail: str = None
    id: int = None


@dataclass
class ExpenseCategory(object):
    name: str
    stock: bool = True
    id: int = None


@dataclass
class Reservation(object):
    name: str
    phone: str = None
    customer_id: int = None
    nb_person: int = None
    table_id: int = None
    date: str = None
    id: int = None


@dataclass
class Waste(object):
    worker_id: int = None
    name: str = None
    category: str = None
    quantity: float = None
    price: float = None
    date: str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    id: int = None


@dataclass
class MenuCategory(object):
    name: str
    printing_place: int = None
    id: int = None


@dataclass
class Worker:
    name: str
    username: str
    password: object
    phone: str = None
    id_category: int = 1
    address: str = ""
    salary: float = 0
    score: float = 0
    picture: object = None
    face: object = None
    id: int = None


@dataclass
class Sell:
    id_worker: int
    id_customer: int
    date: str = ""
    total: float = 0
    completed: int = 0
    id: int = None


@dataclass
class SellItem:
    id_product: int
    id_sell: int
    quantity: float = 0
    total: float = 0
    id: int = None


@dataclass
class SellItemSupplement:
    id_supplement: int
    id_sell_item: int
    price: float = 0
    id: int = None


@dataclass
class Table:
    id: int
    name: str
    seats: int
    comment: str = None
    id_sell: int = None


@dataclass
class Category:
    name: str
    level: int
    id: int = None


@dataclass
class Pointer:
    date_start: str
    date_end: str
    id_worker: int
    id: int = None


@dataclass
class OrderItem:
    tableId: int
    productId: int
    productName: str
    productCategory: int
    orderItemQuantity: float
    orderItemTotal: float
    orderItemSupplements: list

    def toJson(self):
        return {
            "tableId": self.tableId,
            "productId": self.productId,
            "productName": self.productName,
            "productCategory": self.productCategory,
            "orderItemQuantity": self.orderItemQuantity,
            "orderItemTotal": self.orderItemTotal,
            "orderItemSupplements": [x.toJson() for x in self.orderItemSupplements]
        }


@dataclass
class OrderItemShow:
    Name: str
    Category: str
    Quantity: float
    Total: float
    Supplements: list


@dataclass
class HoldingSellShow:
    Ticket_Number: str
    Total: float
    Date: str
