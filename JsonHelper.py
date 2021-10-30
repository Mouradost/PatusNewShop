from DB.DBHandler import DBHelper
from ServerHelper import Client
import json


if __name__ == '__main__':
    db = DBHelper()
    test = json.dumps([x.__dict__ for x in db.getAllTables()])
    print(test)
    client = Client()
    client.start(test)
    client.stop()


