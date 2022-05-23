import sqlite3

conn = sqlite3.connect('konfeti.db')
cur = conn.cursor()
cur.execute("""
CREATE TABLE orders(
  order_id INTEGER, 
  gift_version TEXT, 
  date default current_timestamp,
  customer_id INTEGER,
  set_id INTEGER, 
  FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
  FOREIGN KEY(set_id) REFERENCES setew(set_id)
);
""")
# cur.execute("""
# CREATE TABLE setew(
#   set_id INTEGER PRIMARY KEY, 
#   name  TEXT,
#   weight INTEGER, 
#   price INTEGER, 
#   count INTEGER
# );""")
conn.commit()

