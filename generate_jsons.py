from DB.DBHandler import DBHelper
import json


db = DBHelper()

print(("ok!AUTH\n"))
print((json.dumps([x.toJson() for x in db.getAllMenusPhone()]) + "!MENUITEM\n"))
print((json.dumps([x.__dict__ for x in db.getAllTables()]) + "!TABLES\n"))
print(("[]!TABLECONTENT\n"))
