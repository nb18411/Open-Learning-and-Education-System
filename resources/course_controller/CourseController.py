from flask_restful import Resource, marshal
from modules.models import *
from modules.guid import guid
from constants import *


class CourseController(Resource):
    def get(self):
        courses = Course.query.all()

        return {"courses": [marshal(course, course_fields) for course in courses]}

    def post(self):
        args = parser.parse_args()

        course = Course(name=args["name"], description=args["description"], university=args["university"], guid=guid())
        course.save()

        return {"course": marshal(course, course_fields)}