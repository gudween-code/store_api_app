import sqlite3
from sqlite3.dbapi2 import connect

items = {"items": {}}
vls = []

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

query = "SELECT * FROM items"

for row in cursor.execute(query):
    print(row)
    print({"name": row[0], "price": row[1]})
    vls.append({"name": row[0], "price": row[1]})
    print(vls)
    items.update({"items": vls})
    print(items)

 