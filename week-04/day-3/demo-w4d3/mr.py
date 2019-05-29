import psycopg2

connection = psycopg2.connect(
    host = "localhost",
    database = "greenfox",
    username = "ikarasz",
    password = "ikarasz"
)

print(connection.get_dsn_parameters())

select_query = "SELECT * FROM students"

# SECURITY ISSUE!!!!! INJECTION!!!!!
# name = "Tony"
# class_name = "SEADOG"
# select_query = f"INSERT INTO students VALUES ({name}, {class_name})"

insert_name = "Tony"
insert_class_name = "SEADOG"
insert_query = "INSERT INTO students (name, class) VALUES (%(name)s, %(class_name)s)"

select_query1 = "SELECT * FROM students WHERE name LIKE %s"


cursor = connection.cursor()

# Check and verify
# print(cursor.mogrify(select_query, (name, class_name)))

cursor.execute(insert_query, {
    "name": insert_name,
    "class_name": insert_class_name
    })

# Tell database you have done and commit the action to the database otherwise the data will be lost
connection.commit()

cursor.execute(select_query1, ("%To%", ))

print(cursor.fetchall())

# Counting how many rows are updated
print(cursor.rowcount)

cursor.close()
connection.close()