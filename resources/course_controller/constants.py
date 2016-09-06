from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help='name is required')
parser.add_argument('university', type=str, required=True, help='university guid is required')
parser.add_argument('description', type=str, required=True, help='description is required')
parser.add_argument('credits', type=int, required=True, help='description is required')