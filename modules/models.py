from app import db
from flask_restful import reqparse, fields


class University(db.Document):
    guid = db.StringField()
    name = db.StringField()
    location = db.StringField()


university_fields = {
	"guid": fields.String,
	"name": fields.String,
	"location": fields.String
}


class Course(db.Document):
    guid = db.StringField()
    name = db.StringField()
    description = db.StringField()
    credits = db.IntField()


course_fields = {
    "guid": fields.String,
    "name": fields.String,
    "description": fields.String,
    "credits": fields.Integer
}