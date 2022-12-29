from dao.model.genres import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get(self, genre_id=None):
        query = self.session.query(Genre)
        if genre_id:
            return query.get(genre_id)
        return query.all()
