from dao.directors import DirectorDAO


class DirectorService:

    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_directors(self, director_id=None):
        return self.director_dao.get_directors(director_id)
