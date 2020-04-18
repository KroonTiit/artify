import markdown
import os
import shelve

# Import the framework
from flask import Flask, g, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS, cross_origin

# Create an instance of Flask
app = Flask(__name__)

# Create the API
api = Api(app)
CORS(app, resources={r"/*": {"origins": "*"}})

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("people.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
@cross_origin()
def index():
    """Present some documentation"""

    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)


class PeopleList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        persons = []

        for key in keys:
            persons.append(shelf[key])

        return {'message': 'Success', 'data': persons}, 200

    def post(self):
        parser = reqparse.RequestParser()
        print(request.get_json)

        
        parser.add_argument('name', action="store", default=None, type=str, location='json')
        parser.add_argument('agreed', action="store", default=None, type=bool, location='json')
        parser.add_argument('skills', action="append", default=None, type=str, location='json')


        # Parse the arguments into an object
        args = parser.parse_args()
        # print(args)
        shelf = get_db()
        shelf[args['name']] = args

        return {}, 201


class Person(Resource):
    def get(self, name):
        shelf = get_db()

        # If the key does not exist in the data store, return a 404 error.
        if not (name in shelf):
            return {'message': 'Person not found', 'data': {}}, 404

        return {'message': 'Person found', 'data': shelf[name]}, 200

    def delete(self, name):
        shelf = get_db()

        # If the key does not exist in the data store, return a 404 error.
        if not (name in shelf):
            return {'message': 'Person not found', 'data': {}}, 404

        del shelf[name]
        return '', 204

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8080')
    response.headers.add('Access-Control-Allow-Headers', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response


api.add_resource(PeopleList, '/people')
api.add_resource(Person, '/person/<string:name>')




