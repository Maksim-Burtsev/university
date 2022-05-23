import sqlite3

conn = sqlite3.connect('konfeti.db')
cur = conn.cursor()

# 1 Создайте запрос, включающий наборы, вес и цена которых превышают соответственно 375 г. и 150 рублей.
# cur.execute("""
# SELECT * FROM sets
# WHERE (weight > 375) AND (price > 150)
# """)

# 2. Создайте запрос, который выдает список наборов стоимостью от 100 рублей до 150 рублей, число которых на складе превышает 500 штук.
# cur.execute("""
# SELECT * FROM sets
# WHERE (price BETWEEN 100 AND 150) AND (amount > 500)
# """)

# 3. Создайте простой запрос, перечисляющий заказчиков новогодних наборов, размещенных с 10 по 25
# декабря.
# cur.execute("""
# SELECT customers.customer_id,
#        customers.surname,
#        customers.city
        
# FROM orders_finally 
# INNER JOIN customers ON orders_finally.customer_id=customers.customer_id
# WHERE date BETWEEN "10.12.00" AND "25.12.00"
# """)

# 4. Создайте запрос, перечисляющий заказчиков подарочных наборов и даты их заказов.
# cur.execute("""
# SELECT customers.customer_id,
#        customers.surname,
#        customers.city,
#        orders_finally.date

# FROM orders_finally
# INNER JOIN customers ON orders_finally.customer_id=customers.customer_id
# """)

# cur.execute("""
# SELECT * FROM orders_finally
# WHERE date BETWEEN "10.12.00" AND "25.12.00"
# """)

# 5. Включите в запрос 3 суммарную стоимость заказа.
# cur.execute("""
# SELECT customers.customer_id,
#        customers.surname,
#        customers.city,
#        SUM(sets.price)         

# FROM orders_finally 
# INNER JOIN sets ON orders_finally.set_id=sets.set_id
# INNER JOIN customers ON orders_finally.customer_id=customers.customer_id

# GROUP BY orders_finally.customer_id
# """)

#6. Сохраните результат работы запроса 1 в отдельную таблицу с названием «Дорогие подарки»
# cur.execute("""
# CREATE TABLE expensive_gifts AS   
# SELECT * FROM sets
# WHERE (weight > 375) AND (price > 150)
# """)

# 7. Создайте запрос, подсчитывающий общее количество заказов для каждого заказчика
# cur.execute("""
# SELECT customer_id,
#     COUNT(customer_id)

# FROM orders_finally

# GROUP BY customer_id
# """)


# 8. Получите все наборы, которые были заказаны заказчиком с кодом 44 (в моей таблице это 5 )
# cur.execute("""
# SELECT sets.set_id,
#        sets.name,
#        sets.weight,
#        sets.price,
#        sets.amount 

# FROM orders_finally 
# INNER JOIN sets ON orders_finally.set_id=sets.set_id

# WHERE customer_id=5
# """)

# 9. Получить названия всех наборов из прошлого запроса
cur.execute("""
SELECT sets.name

FROM orders_finally 
INNER JOIN sets ON orders_finally.set_id=sets.set_id

WHERE customer_id=5
""")

rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
