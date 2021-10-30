from dataclasses import dataclass


@dataclass(frozen=True)
class FinishProductTable:
    TABLE_NAME: str = "FinishProducts"
    COLUMN_ID: str = "_id"
    COLUMN_NAME: str = "name"
    COLUMN_CATEGORY: str = "category"
    COLUMN_QUANTITY: str = "quantity"
    COLUMN_PRICE: str = "price"
    COLUMN_PICTURE: str = "picture"


@dataclass(frozen=True)
class RawProductTable:
    TABLE_NAME: str = "RawProducts"
    COLUMN_ID: str = "_id"
    COLUMN_NAME: str = "name"
    COLUMN_CATEGORY: str = "category"
    COLUMN_QUANTITY: str = "quantity"
    COLUMN_PRICE: str = "price"


@dataclass(frozen=True)
class CustomerTable:
    TABLE_NAME: str = "Customers"
    COLUMN_ID: str = "_id"
    COLUMN_NAME: str = "name"
    COLUMN_PHONE: str = "phone"
    COLUMN_ADDRESS: str = "address"
    COLUMN_SCORE: str = "score"
    COLUMN_PICTURE: str = "picture"
    COLUMN_FACE: str = "face"


@dataclass(frozen=True)
class WorkerTable:
    TABLE_NAME: str = "Workers"
    COLUMN_ID: str = "_id"
    COLUMN_NAME: str = "name"
    COLUMN_USERNAME: str = "username"
    COLUMN_PASSWORD: str = "password"
    COLUMN_PHONE: str = "phone"
    COLUMN_ID_CATEGORY: str = "id_category"
    COLUMN_ADDRESS: str = "address"
    COLUMN_SCORE: str = "score"
    COLUMN_PICTURE: str = "picture"
    COLUMN_FACE: str = "face"


@dataclass(frozen=True)
class SellTable:
    TABLE_NAME: str = "Sells"
    COLUMN_ID: str = "_id"
    COLUMN_ID_WORKER: str = "id_worker"
    COLUMN_ID_CUSTOMER: str = "id_customer"
    COLUMN_DATE: str = "date"
    COLUMN_TOTAL: str = "total"
    COLUMN_COMPLETED: str = "completed"


@dataclass(frozen=True)
class SellItemTable:
    TABLE_NAME: str = "SellItems"
    COLUMN_ID: str = "_id"
    COLUMN_ID_PRODUCT: str = "id_product"
    COLUMN_ID_SELL: str = "id_sell"
    COLUMN_QUANTITY: str = "quantity"
    COLUMN_TOTAL: str = "total"


@dataclass(frozen=True)
class TableTable:
    TABLE_NAME: str = "Tables"
    COLUMN_ID: str = "_id"
    COLUMN_NAME: str = "name"
    COLUMN_SEATS: str = "seats"
    COLUMN_ID_SELL: str = "id_sell"


@dataclass(frozen=True)
class CategoryTable:
    TABLE_NAME: str = "Category"
    COLUMN_ID: str = "_id"
    COLUMN_NAME: str = "name"
    COLUMN_LEVEL: str = "level"


@dataclass(frozen=True)
class PointerTable:
    TABLE_NAME: str = "Pointer"
    COLUMN_ID: str = "_id"
    COLUMN_DATE_START: str = "date_start"
    COLUMN_DATE_END: str = "date_end"
    COLUMN_ID_WORKER: str = "id_worker"
