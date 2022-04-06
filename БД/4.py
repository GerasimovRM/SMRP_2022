from models.base_meta import global_init, create_session
from models.films import Films


global_init("films.sqlite")
session = create_session()

films = session.query(Films).filter(Films.title == "Хех")
for film in films:
    print(film.id)
    session.delete(film)

session.commit()

films_query = session.query(Films)
films = films_query.all()
for film in films:
    print(film.id, film.title, film.year, film.duration)

session.close()