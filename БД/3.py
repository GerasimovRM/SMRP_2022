from models.base_meta import global_init, create_session
from models.films import Films


global_init("films.sqlite")
session = create_session()

# CREATE
new_film = Films(title="Хех", duration=20, year=1990)
session.add(new_film)
session.commit()

# DELETE
session.delete(new_film)
session.commit()

films_query = session.query(Films)
print(films_query)
films = films_query.all()
for film in films:
    print(film.id, film.title, film.year, film.duration)

# UPDATE
film = films[0]
film.title = "Не, не было!"

session.commit()

session.close()