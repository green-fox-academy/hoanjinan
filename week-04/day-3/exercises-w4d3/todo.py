from Config import Config
import sys, psycopg2

connection = Config("localhost", "todo_list", "hoanjinan_otoko", "hoanjinan_otoko").connect()

# print(connection.get_dsn_parameters())
# print(connection.status)
# print(sys.argv)

# SELECT query 
select_todo = "SELECT * FROM todo;"
# INSERT query
insert_todo = "INSERT INTO todo (task) VALUES (%(task)s);"
# DELETE query
delete_todo = "DELETE FROM todo WHERE todo_id = %(task_id)s;"

cursor = connection.cursor()

if sys.argv[1] == "-l":
    cursor.execute(select_todo)
    fetched_data = cursor.fetchall()
    for i in range(len(fetched_data)):
        print(f"{fetched_data[i][0]} - {fetched_data[i][1]}")
elif sys.argv[1] == "-a":
    words = sys.argv[2:]
    task = " ".join(words)
    cursor.execute(insert_todo, {"task": task})
    connection.commit()
elif sys.argv[1] == "-c":
    check_id = sys.argv[2]
    status = False
    cursor.execute(select_todo)
    fetched_data = cursor.fetchall()
    for i in range(len(fetched_data)):
        if fetched_data[i][0] == int(check_id):
            status = True
    if status == True:
        print("In the database")
    else:
        print("Not in the database")
elif sys.argv[1] == "-r":
    cursor.execute(delete_todo, {"task_id": sys.argv[2]})
    connection.commit()

cursor.close()
connection.close()

