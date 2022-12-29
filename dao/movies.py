from dao.model.movies import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_movies(self, movie_id=None, **kwargs):
        query = self.session.query(Movie)
        if movie_id:
            return query.get(movie_id)
        if kwargs:
            for key, value in kwargs.items():
                query = query.filter(eval(f"Movie.{key}") == int(value))
        return query.all()

    def create_movies(self, data):
        new_movie = Movie(**data)
        with self.session.begin():
            self.session.add(new_movie)
        return new_movie

    def update_movies(self, movie):
        self.session.add(movie)
        self.session.commit()

    def delete_movies(self, movie_id):
        movie = self.get_movies(movie_id)
        self.session.delete(movie)
        self.session.commit()
