import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Movie, Actor, db
from auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resource={r"/api.*": {"origin": "*"}})

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS')
        return response


   # GET /movies
    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movie(jwt):
        selection = Movie.query.order_by(Movie.id).all()
        if movies is None:
            abort(404, 'There is no movie data.')

        movies = [m.format() for m in selection]
        return jsonify({
            'success': True,
            'movies': movies,
            'total_movies': len(movies)
        })

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
        movies = [m.format() for m in selection]

        return jsonify({
            'success': True,
            'movies': movies,
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
    @app.errorhandler(404)
    def notfound(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource_not_found"
        })

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        })

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify(error.error), error.status_code

    return app

app = create_app()


if __name__ == '__main__':
    app.run()
