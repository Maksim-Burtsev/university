import sqlite3

conn = sqlite3.connect('konfeti.db')
cur = conn.cursor()

# CREATE TABLE customers(
#   customer_id INTEGER PRIMARY KEY,
#   surname TEXT,
#   city TEXT
#   );""")
# cur.execute("""
# CREATE TABLE sets(
#   set_id INTEGER PRIMARY KEY,
#   name  TEXT,
#   weight INTEGER,
#   price INTEGER,
#   amount INTEGER
# );
# cur.execute("""
# CREATE TABLE orders_finally(
#   order_id INTEGER,
#   gift_version TEXT,
#   date default current_timestamp,
#   customer_id INTEGER,
#   set_id INTEGER,
#   FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
#   FOREIGN KEY(set_id) REFERENCES sets(set_id)
# );
# """)


# sqlite_insert_with_param = """INSERT INTO customers
#                               (customer_id, surname, city)
#                               VALUES (?, ?, ?);"""
# data = [
#     (1, 'Петров', 'Кемерово')
#     (2, 'Петров', 'Вологда'),
#     (3, 'Уваров', 'Воложск'),
#     (4, 'Сидоров', 'Мытищи'),
#     (5, 'Комаров', 'Москва'),
# ]

# sqlite_insert_with_param = """INSERT INTO sets
#                               (set_id, name, weight, price, amount)
#                               VALUES (?, ?, ?, ?, ?);"""
# data = [
#     (1, 'Ассорти', 500, 120, 35),
#     (2, 'Вишня в шоколаде', 250, 54, 110),
#     (3, 'Дары природы', 350, 123, 510),
#     (4, 'Кофейный аромат', 500, 110, 350),
#     (5, 'Волшебный набор', 1000, 254, 120),
#     (6, 'Праздничный набор', 600, 350, 200),
#     (7, 'Новогодний набор', 350, 75, 109),
#     (8, 'Осенний набор', 400, 65, 345),
#     (9, 'Нежность', 250, 255, 210),
#     (10, 'Новогодний набор', 700, 150, 609),
#     (11, 'Ассорти', 250, 135, 540),
#     (12, 'Марципановое чудо', 125, 145, 625),
# ]


# sqlite_insert_with_param = """INSERT INTO orders_finally
#                               (order_id, gift_version, date, customer_id, set_id)
#                               VALUES (?, ?, ?, ?, ?);"""
# data = [
#     (1, 'Новогодний набор', '15.12.00', 1, 1),
#     (2, 'Осенний набор', '01.12.00', 2, 2),
#     (3, 'Вишня в шоколаде', '22.12.00', 2, 1),
#     (4, 'Новогодний набор', '21.12.00', 4, 2),
#     (5, 'Дары природы', '23.12.00', 1, 1),
#     (6, 'Праздничный набор', '24.12.00', 5, 1),
#     (7, 'Праздничный набор', '28.12.00', 3, 1),
# ]


conn.commit()
