from dataclasses import dataclass
import datetime
from typing import List


@dataclass
class Expense:
    name: str
    category: int
    unit: str = ""
    quantity: float = 0
    price: float = 0
    supplier_id: int = None
    date: str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    payed: bool = True
    id: int = None


@dataclass
class MenuItem:
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
class MenuItemPhone:
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
            'quantity': self.quantity,
            'price': self.price,
            "available": self.available,
            "picture": self.picture,
            "supplements": [x.toJson() for x in self.supplements],
            "id": self.id
        }


@dataclass
class Supplement:
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
class Stock:
    name: str
    category: int
    unit: str
    quantity: float = 0
    is_ingredient: bool = False
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
class Supplier:
    name: str
    phone: str = None
    address: str = None
    mail: str = None
    id: int = None


@dataclass
class ExpenseCategory:
    name: str
    stock: bool = True
    is_ingredient: bool = False
    id: int = None


@dataclass
class Reservation:
    name: str
    phone: str = None
    customer_id: int = None
    nb_person: int = None
    table_id: int = None
    date: str = None
    id: int = None


@dataclass
class Waste:
    worker_id: int = None
    name: str = None
    category: str = None
    quantity: float = None
    price: float = None
    date: str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    id: int = None


@dataclass
class MenuCategory:
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
    cv: object = None
    id: int = None


@dataclass
class Sell:
    id_worker: int
    id_customer: int
    date: str = ""
    total: float = 0
    completed: int = 0
    nb_covers: int = 0
    on_table: bool = True
    id: int = None


@dataclass
class SellItem:
    id_product: int
    id_sell: int
    quantity: float = 0
    total: float = 0
    group: int = 0
    ready: int = 0
    served: int = 0
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
    reserved: int = 0
    id_sell: int = None


@dataclass
class Category:
    name: str
    tables: int = 1
    cashier: int = 1
    reservation: int = 1
    waste: int = 1
    stock: int = 1
    receipt: int = 1
    database: int = 1
    phone: int = 1
    dashboard: int = 1
    id: int = None


@dataclass
class Pointer:
    date_start: str
    date_end: str
    id_worker: int
    id: int = None


@dataclass
class MenuItemReceipt:
    id: int
    ingredient_name: str
    ingredient_id: int
    quantity: float


@dataclass
class OrderItem:
    tableId: int
    productId: int
    productName: str
    productCategory: int
    productUnit: str
    orderItemQuantity: float
    orderItemTotal: float
    orderItemSupplements: list
    group_id: int
    nb_covers: int
    ready: bool
    served: bool
    id: int = None

    def toJson(self):
        return {
            "tableId": self.tableId,
            "productId": self.productId,
            "productName": self.productName,
            "productCategory": self.productCategory,
            "productUnit": self.productUnit,
            "orderItemQuantity": self.orderItemQuantity,
            "orderItemTotal": self.orderItemTotal,
            "orderItemSupplements": [x.toJson() for x in self.orderItemSupplements],
            "group_id": self.group_id,
            "nb_covers": self.nb_covers,
            "ready": self.ready,
            "served": self.served,
            "id": self.id
        }

    def getDiff(self, other):
        return OrderItem(
            tableId=self.tableId,
            productId=self.productId,
            productName=self.productName,
            productCategory=self.productCategory,
            productUnit=self.productUnit,
            orderItemQuantity=self.orderItemQuantity - other.orderItemQuantity,
            orderItemTotal=self.orderItemTotal - other.orderItemTotal,
            orderItemSupplements=self.orderItemSupplements,
            group_id=self.group_id,
            nb_covers=self.nb_covers,
            ready=self.ready,
            served=self.served,
            id=self.id)

    def isChanged(self, other):
        return (self.orderItemQuantity != other.orderItemQuantity) and (self.orderItemTotal != other.orderItemTotal)

    def compare(self, other):
        return (self.productId == other.productId) and (self.ready == other.ready)

    def getDeleted(self):
        return OrderItem(
            tableId=self.tableId,
            productId=self.productId,
            productName=self.productName,
            productCategory=self.productCategory,
            productUnit=self.productUnit,
            orderItemQuantity=-self.orderItemQuantity,
            orderItemTotal=-self.orderItemTotal,
            orderItemSupplements=self.orderItemSupplements,
            group_id=self.group_id,
            nb_covers=self.nb_covers,
            ready=self.ready,
            served=self.served,
            id=self.id)


@dataclass
class Ticket:
    id: int
    table_id: int
    worker_id: int
    worker_name: str
    orders: List[OrderItem]

    def toJson(self):
        return {
            "id": self.id,
            "table_id": self.table_id,
            "worker_id": self.worker_id,
            "worker_name": self.worker_name,
            "orders": [x.toJson() for x in self.orders]
        }


@dataclass
class OrderItemShow:
    Ready: bool
    Name: str
    Category: str
    Quantity: float
    Total: float
    Supplements: list
    Group: int


@dataclass
class HoldingSellShow:
    Ticket_Number: str
    Total: float
    Date: str
