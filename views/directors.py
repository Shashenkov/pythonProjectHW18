from flask_restx import Resource, Namespace
from dao.model.directors import DirectorSchema
from implemented import director_service

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):
    schema = DirectorSchema(many=True)

    def get(self):
        return self.schema.dump(director_service.get_directors()), 200


@directors_ns.route('/<int:director_id>')
class DirectorView(Resource):
    schema = DirectorSchema()

    def get(self, director_id: int):
        return self.schema.dump(director_service.get_directors(director_id)), 200
