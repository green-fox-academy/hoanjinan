from Config import Config
import json, psycopg2

f = open("exercises-w4d3/car_dealer_data.json", mode = "r", encoding = "utf-8")
content = json.load(f)

connection = Config().connect()

create_car_dealer = """CREATE TABLE car_dealer(
                            id BIGSERIAL NOT NULL PRIMARY KEY,
                            brand VARCHAR(10),
                            model VARCHAR(10),
                            year int,
                            condition VARCHAR(10),
                            price int,
                            count int
                        );"""

insert_car_dealer = """INSERT INTO car_dealer (brand, model, year, condition, price, count)
                            VALUES(
                                %(brand)s,
                                %(model)s,
                                %(year)s,
                                %(condition)s,
                                %(price)s,
                                %(count)s
                            );"""

# Remove the cars which are not on stock
remove_car = """DELETE FROM car_dealer
                    WHERE count = 0;"""

# Decrease the price of wrecks by 20%
decrease_price = """UPDATE car_dealer
                        SET price = round(price * 0.8)
                        WHERE condition = 'wreck';"""

# Count the average age of the cars on the stock
count_avg_age = """SELECT ROUND(SUM((EXTRACT(year from CURRENT_DATE) - year) * count) / SUM(count)) AS avg_age FROM car_dealer;"""

cursor = connection.cursor()

cursor.execute(create_car_dealer)

for i in content:
    cursor.execute(insert_car_dealer, i)


print(cursor.mogrify(remove_car))
print(cursor.mogrify(decrease_price))
cursor.execute(remove_car)
cursor.execute(decrease_price)
cursor.execute(count_avg_age)

# cursor.execute("SELECT * FROM car_dealer;")
print(cursor.fetchall())
# print(cursor.rowcount)


connection.commit()
f.close()
cursor.close()
connection.close()