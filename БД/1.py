import sqlite3


connection = sqlite3.connect("films.sqlite")
cursor = connection.cursor()

sql_query = """SELECT * FROM films
                WHERE duration > 60"""


result = cursor.execute(sql_query).fetchall()
print(*result, sep="\n")

cursor.close()
connection.close()