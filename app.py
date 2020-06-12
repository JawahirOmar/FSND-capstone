import os
import json
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from sqlalchemy import exc
from models import Movie, Actor, db
from auth import AuthError, requires_auth


database_path = os.environ.get('DATABASE_URL')
default_path = 'postgresql://postgres:90@localhost:5432/agency'

database_path = os.getenv('DATABASE_URL', default_path)

migrate = Migrate()


def create_app(test_config=None):
    """Create and configure the app."""
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)
    # setup_db(app)
    CORS(app, resource={r"/api.*": {"origin": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow_Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Contorl-Allow_Methods',
                             'GET,POST,PATCH,DELETE')
        return response


    @app.route('/', methods=['GET'])
    def welcome():
        return jsonify("Welcome to my app")

   # GET /movies
    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movie(jwt):
     try:
        movies = Movie.query.order_by(Movie.id).all()
        if len(movies) == 0:
            abort(404)

        movies_formatted = [m.format() for m in movies]
        return jsonify({
            'success': True,
            'movies': movies_formatted
    }),200

     except Exception:
        abort(422)

    # POST /movies
    @app.route('/movies', methods=['POST'])
    @requires_auth('create:movies')
    def post_movie(jwt):
        if request.data:
            new_movie = json.loads(request.data.decode('utf-8'))

            if 'title' not in new_movie:
                abort(422)

            if 'release_date' not in new_movie:
                abort(422)

            title = new_movie['title']
            release_date = new_movie['release_date']
            add_movie = Movie(title=title, release_date=release_date)

            add_movie.insert()

            selection = Movie.query.order_by(Movie.id).all()
            movies = [m.format() for m in selection]

            return jsonify({
                'success': True,
                'movies': movies,
                'total_movies': len(movies)
            })
        else:
            abort(400)

    # DELETE /movies/id
    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(jwt, movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none

        if not movie:
            return abort(404)

        movie.delete()

        selection = Movie.query.order_by(Movie.id).all()
        movies_formatted = [m.format() for m in selection]

        return jsonify({
            'success': True,
            'movies': movies_formatted,
            'deleted': movie.id
        })

    # PATCH /movies/id
    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('edit:movies')
    def update_actor(jwt, actor_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none

        if not movie:
            return abort(404)
        if request.data:
            body = json.loads(request.data.decode('utf-8'))
            if 'title' in body:
                title = body.get('title')
                movie.title = title
            if 'release_date' in body:
                release_date = body.get('release_date')
                movie.release_date = release_date

            movie.update()

            selection = Movie.query.order_by(Movie.id).all()
            movies = [m.format() for m in selection]

            return jsonify({
                'success': True,
                'movies': movies,
                'total_movies': len(movies),
                'updated': movie.id
            })
        else:
            abort(400)




    # GET/actors
    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(jwt):

        selection = Actor.query.order_by(Actor.id).all()
        actors = [d.format() for d in selection]

        return jsonify({
            'success': True,
            'actors': actors,
            'total_actors': len(actors)
        })

    # POST/actors
    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def post_actors(jwt):
        if request.data:
            new_actors = json.loads(request.data.decode('utf-8'))

            if 'name' not in new_actors:
                abort(422)
            if 'age' not in new_actors:
                abort(422)
            if 'gender' not in new_actors:
                abort(422)

            name = new_actors['name']
            age = new_actors['age']
            gender = new_actors['gender']
            actors = Actor(name=name, age=age, gender=gender)

            actors.insert()
            
            selection = Actor.query.order_by(Actor.id).all()
            actors = [d.format() for d in selection]

            return jsonify({
                'success': True,
                'actors': actors,
                'total_actors': len(actors)
            })
        else:
            abort(400)

    # DELETE/actors
    @app.route('/actors/<int:actors_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actors(jwt, actors_id):
        actors = Actor.query.filter(Actor.id == actors_id).one_or_none

        if not actors:
            return abort(404)

        actors.delete()

        selection = Actor.query.order_by(Actor.id).all()
        actors = [a.format() for a in selection]
        return jsonify({
            'success': True,
            'actors': actors,
            'deleted': actors.id
        })



    # Error Handling
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'message': 'Bad Request',
            'success': False
        }), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            'message': 'Unauthorized',
            'success': False
        }), 401

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'message': 'Not Found',
            'success': False
        }), 404

    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({
            'message': 'Method Not Allowed',
            'success': False
        }), 405

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'message': 'Unprocessable Entity',
            'success': False
        }), 422

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            'message': 'Server Error',
            'success': False
        }), 500

    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    return app

app = create_app()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
