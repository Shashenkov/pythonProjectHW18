# файл для создания DAO и сервисов чтобы импортировать их везде
from dao.movies import MovieDAO
from dao.genre import GenreDAO
from dao.directors import DirectorDAO
from service.movies import MovieService
from service.genres import GenreService
from service.directors import DirectorService
from setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)