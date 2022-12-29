from dao.model.directors import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_directors(self, director_id=None):
        query = self.session.query(Director)
        if director_id:
            return query.get(director_id)
        return query.all()
