from dao.movies import MovieDAO


class MovieService:

    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_movies(self, movie_id=None, **kwargs):
        return self.movie_dao.get_movies(movie_id, **kwargs)

    def create_movie(self, data):
        return self.movie_dao.create_movies(data)

    def update_movie(self, movie_id, data):
        movie = self.get_movies(movie_id)

        movie.title = data['title']
        movie.description = data['description']
        movie.trailer = data['trailer']
        movie.year = data['year']
        movie.rating = data['rating']
        movie.genre_id = data['genre_id']
        movie.director_id = data['director_id']
        self.movie_dao.update_movies(movie)
        return movie

    def delete_movie(self, movie_id):
        self.movie_dao.delete_movies(movie_id)

