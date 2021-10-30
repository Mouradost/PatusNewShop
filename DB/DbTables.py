from dataclasses import dataclass


@dataclass
class FinishProduct(object):
    name: str
    category: str
    quantity: float = 0
    price: float = 0
    picture: object = None
    id: int = None


@dataclass
class RawProduct:
    name: str
    category: str
    quantity: float = 0
    price: float = 0
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
class Worker:
    name: str
    username: str
    password: object
    phone: str = None
    id_category: int = 0
    address: str = ""
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
class Table:
    id: int
    name: str
    seats: int
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
    productCategory: str
    orderItemQuantity: float
    orderItemTotal: float
