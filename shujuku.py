import sqlite3

conn = sqlite3.connect('identifier.sqlite')
cursor = conn.cursor()
cursor.execute('create table user')