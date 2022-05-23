
import sqlite3

def _get_data(filename: str) -> list[tuple]:

    data_list = []
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()

    for i in data.split('\n'):
        data_list.append(tuple(i.split("\t")))

    return data_list


conn = sqlite3.connect('details_and_providers.db')
cur = conn.cursor()

# cur.execute("""CREATE TABLE table_J(
#   J TEXT,
#   name TEXT,
#   city TEXT
#   );""")


# cur.execute("""CREATE TABLE table_SPJ(
#   P TEXT,
#   D TEXT,
#   J TEXT,
#   amount INTEGER
#   );""")

# cur.execute("""CREATE TABLE table_S(
#   P TEXT,
#   name TEXT,
#   status TEXT, 
#   city TEXT
#   );""")

# cur.execute("""CREATE TABLE table_P(
#   D TEXT,
#   name TEXT,
#   color TEXT, 
#   weight TEXT, 
#   city TEXT
#   );""")

# cur.execute("""CREATE TABLE table_SP(
#   P TEXT,
#   D TEXT,
#   amount TEXT
#   );""")

# sqlite_insert_with_param = """INSERT INTO table_S
#                               (P, name, status, city)
#                               VALUES (?, ?, ?, ?);"""

# data = _get_data('data_s.txt')
# conn.executemany(sqlite_insert_with_param, data)

# sqlite_insert_with_param = """INSERT INTO table_P
#                               (D, name, color, weight, city)
#                               VALUES (?, ?, ?, ?, ?);"""

# data = _get_data('data_p.txt')
# conn.executemany(sqlite_insert_with_param, data)

# sqlite_insert_with_param = """INSERT INTO table_SP
#                               (P, D, amount)
#                               VALUES (?, ?, ?);"""

# data = _get_data('data_sp.txt')
# conn.executemany(sqlite_insert_with_param, data)

# sqlite_insert_with_param = """INSERT INTO table_J
#                               (J, name, city)
#                               VALUES (?, ?, ?);"""

# data = _get_data('data_j.txt')
# conn.executemany(sqlite_insert_with_param, data)

# sqlite_insert_with_param = """INSERT INTO table_SPJ
#                               (P, D, J, amount)
#                               VALUES (?, ?, ?, ?);"""

# data = _get_data('data_spj.txt')
# conn.executemany(sqlite_insert_with_param, data)

# •	Получите имена поставщиков, которые обеспечивают проект J1.

# cur.execute("""
#     SELECT DISTINCT table_S.name 
#     FROM table_SPJ
#     INNER JOIN table_S ON table_S.P=table_SPJ.P
#     WHERE table_SPJ.J="J1"
# """)


# •	Получите имена деталей, поставляемых поставщиком в Киев.
# cur.execute("""
# SELECT  DISTINCT table_P.name 
#     FROM table_SPJ
# INNER JOIN table_P ON table_P.D=table_SPJ.D
# INNER JOIN table_J ON table_J.J=table_SPJ.J

# WHERE table_J.city="Киев"
# """)

# Получите все такие тройки «имена поставщиков – «имена деталей – «имена проектов», для которых выводимые поставщик, деталь, проект размещены в одном городе

cur.execute("""
SELECT  table_P.name,
        table_S.name,
        table_J.name
FROM table_SPJ
INNER JOIN table_P ON table_P.D=table_SPJ.D
INNER JOIN table_S ON table_S.P=table_SPJ.P
INNER JOIN table_J ON table_J.J=table_SPJ.J

WHERE table_P.city=table_S.city AND table_S.city=table_J.city

""")

rows = cur.fetchall()
for row in rows:
    print(row)


conn.commit()
