from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help='name is required')
parser.add_argument('location', type=str, required=True, help='location is required')