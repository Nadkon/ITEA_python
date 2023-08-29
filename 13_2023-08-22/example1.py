import psycopg2
import psycopg2.extras

dbname = "python_pro"
user = "nadinekononykhina"
password = "1234"
host = "localhost"
port = "5432"

connection = psycopg2.connect(
    dbname = dbname,
    user = user,
    password = password,
    host = host,
    port = port,
    cursor_factory = psycopg2.extras.DictCursor #Щоб виводилося дікшионарі
)

cursor = connection.cursor()
query = 'SELECT * FROM "user";'
cursor.execute(query)

users = cursor.fetchall()
for user in users:
    print(user) #виведе все
    #print(user[1]) - виведе лише імена

#close the cursor
cursor.close()

#Застосування змін та закриття зєднання
connection.commit()
connection.close()
