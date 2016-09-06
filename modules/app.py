from flask import Flask, render_template, request, redirect
from flask_restful import Api
from flask_mongoalchemy import MongoAlchemy

app = Flask(__name__)

api = Api(app)

app.config['MONGOALCHEMY_DATABASE'] = 'education'
db = MongoAlchemy(app)


# Resources
from resources.university_controller.UniversityController import UniversityController
from resources.course_controller.CourseController import CourseController


api.add_resource(UniversityController, "/university")
api.add_resource(CourseController, "/course")


@app.route('/')
def education():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
