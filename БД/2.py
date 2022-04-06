import sqlite3


connection = sqlite3.connect("films.sqlite")
cursor = connection.cursor()

title = '\"Мой новый фильм\"'
year = 2022
duration = 90
genre_id = 2

sql_query = f"""INSERT INTO films (title, year, duration, genre)
                VALUES ({title}, {year}, {duration}, {genre_id})"""
result = cursor.execute(sql_query)
connection.commit()

cursor.close()
connection.close()