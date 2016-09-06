from flask_restful import Resource, marshal
from modules.models import *
from modules.guid import guid
from constants import *


class UniversityController(Resource):
    def get(self):
        univeristies = University.query.all()

        return {"universities": [marshal(university, university_fields) for university in univeristies]}

    def post(self):
        args = parser.parse_args()

        university = University(name=args["name"], location=args["location"], guid=guid())
        university.save()

        return {"university": marshal(university, university_fields)}