from dataclasses import dataclass


@dataclass(frozen=True)
class ExpenseTable:
    TABLE_NAME: str = "Expense"
    COLUMN_ID: str = "_id"
    COLUMN_NAME: str = "name"
    COLUMN_CATEGORY: str = "category"
    COLUMN_UNIT: str = "unit"
    COLUMN_QUANTITY: str = "quantity"
    COLUMN_PRICE: str = "price"
    COLUMN_SUPPLIER_ID: str = "supplier_id"
    COLUMN_DATE: str = "date"
    COLUMN_PAYED: str = "payed"


@dataclass(frozen=True)
class MenuTable:
    TABLE_NAME: str = "Menu"
    COLUMN_ID: str = "_id"
    COLUMN_NAME: str = "name"
    COLUMN_CATEGORY: str = "category"
    COLUMN_CATEGORY_ID: str = "category_id"
    COLUMN_UNIT: str = "unit"
    COLUMN_QUANTITY: str = "quantity"
    COLUMN_PRICE: str = "price"
    COLUMN_AVAILABLE: str = "available"
    COLUMN_PICTURE: str = "picture"


@dataclass(frozen=True)
class MenuItemReceiptTable:
    TABLE_NAME: str = "MenuItemReceipt"
    COLUMN_ID: str = "_id"
    COLUMN_INGREDIENT_NAME: str = "ingredient_name"
    COLUMN_INGREDIENT_ID: str = "ingredient_id"
    COLUMN_QUANTITY: str = "quantity"


@dataclass(frozen=True)
class StockTable:
    TABLE_NAME: str = "Stock"
    COLUMN_NAME: str = "name"
    COLUMN_CATEGORY: str = "category"
    COLUMN_UNIT: str = "unit"
    COLUMN_QUANTITY: str = "quantity"
    COLUMN_IS_INGREDIENT: str = "is_ingredient"
    COLUMN_ID: str = "_id"


@dataclass(frozen=True)
class SupplementTable:
    TABLE_NAME: str = "Supplement"
    COLUMN_ID: str = "_id"
    COLUMN_NAME: str = "name"
    COLUMN_RELATED_ITEM_ID: str = "related_item_id"
    COLUMN_QUANTITY: str = "quantity"
    COLUMN_PRICE: str = "price"


@dataclass(frozen=True)
class SupplierTable:
    TABLE_NAME: str = "Supplier"
    COLUMN_ID: str = "_id"
    COLUMN_NAME: str = "name"
    COLUMN_PHONE: str = "phone"
    COLUMN_ADDRESS: str = "address"
    COLUMN_MAIL: str = "mail"


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
class ExpenseCategoryTable:
    TABLE_NAME: str = "ExpenseCategory"
    COLUMN_ID: str = "_id"
    COLUMN_NAME: str = "name"
    COLUMN_STOCK: str = "stock"
    COLUMN_IS_INGREDIENT: str = "is_ingredient"


@dataclass(frozen=True)
class ReservationTable:
    TABLE_NAME: str = "Reservation"
    COLUMN_ID: str = "_id"
    COLUMN_NAME: str = "name"
    COLUMN_PHONE: str = "phone"
    COLUMN_CUSTOMER_ID: str = "customer_id"
    COLUMN_NB_PERSON: str = "nb_person"
    COLUMN_TABLE_ID: str = "table_id"
    COLUMN_DATE: str = "date"


@dataclass(frozen=True)
class WasteTable:
    TABLE_NAME: str = "Waste"
    COLUMN_ID: str = "_id"
    COLUMN_WORKER_ID: str = "worker_id"
    COLUMN_NAME: str = "name"
    COLUMN_CATEGORY: str = "category"
    COLUMN_QUANTITY: str = "quantity"
    COLUMN_PRICE: str = "price"
    COLUMN_DATE: str = "date"


@dataclass(frozen=True)
class MenuCategoryTable:
    TABLE_NAME: str = "MenuCategory"
    COLUMN_ID: str = "_id"
    COLUMN_NAME: str = "name"
    COLUMN_PRINTING_PLACE: str = "printing_place"


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
    COLUMN_SALARY: str = "salary"
    COLUMN_SCORE: str = "score"
    COLUMN_PICTURE: str = "picture"
    COLUMN_FACE: str = "face"
    COLUMN_CV: str = "cv"


@dataclass(frozen=True)
class SellTable:
    TABLE_NAME: str = "Sells"
    COLUMN_ID: str = "_id"
    COLUMN_ID_WORKER: str = "id_worker"
    COLUMN_ID_CUSTOMER: str = "id_customer"
    COLUMN_DATE: str = "date"
    COLUMN_TOTAL: str = "total"
    COLUMN_COMPLETED: str = "completed"
    COLUMN_NB_COVERS: str = "nb_covers"
    COLUMN_ON_TABLE: str = "on_table"


@dataclass(frozen=True)
class SellItemTable:
    TABLE_NAME: str = "SellItems"
    COLUMN_ID: str = "_id"
    COLUMN_ID_PRODUCT: str = "id_product"
    COLUMN_ID_SELL: str = "id_sell"
    COLUMN_QUANTITY: str = "quantity"
    COLUMN_TOTAL: str = "total"
    COLUMN_GROUP: str = "group_id"
    COLUMN_READY: str = "ready"
    COLUMN_SERVED: str = "served"


@dataclass(frozen=True)
class SellItemSupplementTable:
    TABLE_NAME: str = "SellItemSupplement"
    COLUMN_ID: str = "_id"
    COLUMN_ID_SUPPLEMENT: str = "id_supplement"
    COLUMN_ID_SELL_ITEM: str = "id_sell_item"
    COLUMN_PRICE: str = "price"


@dataclass(frozen=True)
class TableTable:
    TABLE_NAME: str = "Tables"
    COLUMN_ID: str = "_id"
    COLUMN_NAME: str = "name"
    COLUMN_SEATS: str = "seats"
    COLUMN_COMMENT: str = "comment"
    COLUMN_RESERVED: str = "reserved"
    COLUMN_ID_SELL: str = "id_sell"


@dataclass(frozen=True)
class CategoryTable:
    TABLE_NAME: str = "Category"
    COLUMN_ID: str = "_id"
    COLUMN_NAME: str = "name"
    COLUMN_TABLES: str = "tables"
    COLUMN_CASHIER: str = "cashier"
    COLUMN_RESERVATION: str = "reservation"
    COLUMN_WASTE: str = "waste"
    COLUMN_STOCK: str = "stock"
    COLUMN_RECEIPT: str = "receipt"
    COLUMN_DATABASE: str = "database"
    COLUMN_PHONE: str = "phone"
    COLUMN_DASHBOARD: str = "dashboard"


@dataclass(frozen=True)
class PointerTable:
    TABLE_NAME: str = "Pointer"
    COLUMN_ID: str = "_id"
    COLUMN_DATE_START: str = "date_start"
    COLUMN_DATE_END: str = "date_end"
    COLUMN_ID_WORKER: str = "id_worker"
