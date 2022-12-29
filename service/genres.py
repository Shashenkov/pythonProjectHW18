from dao.genre import GenreDAO


class GenreService:

    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get(self, genre_id=None):
        return self.genre_dao.get(genre_id)
