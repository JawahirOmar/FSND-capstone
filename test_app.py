import os
import json
import unittest
from flask_sqlalchemy import SQLAlchemy
from datetime import date
from app import create_app
from models import Movie, Actor 
import datetime

class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.casting_assistant = os.getenv('CASTING_ASSISTANT')
        self.casting_director = os.getenv('CASTING_DIRECTOR')
        self.executive_producer = os.getenv('EXECUTIVE_PRODUCER')
        self.database_name = "agency"
        self.database_path = "postgres://{}/{}".format(
            'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_movie = {
            'title': 'Parasite',
            'release_date': '1/2020'
        }

        self.update_movie = {
            'title': 'Bombshell ',
            'release_date': datetime.date(2050, 6, 8),
        }

        self.new_actor = {
            'name': 'Leonardo DiCaprio',
            'age': '45',
            'gender': 'Male'
        }

        self.update_actor = {
            'name': 'Morgan Freeman',
            'age': '73',
            'gender': 'Male',
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass


    # GET Movie
    def test_get_movies_error(self):
        res = self.client().get('/movies', headers={"Authorization": "Bearer {}".format(self.casting_assistant)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_get_movies_error(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')
        self.assertEqual(data['description'], 'Authorization header is expected.')    

 
    # POST Movie
    def test_post_movies_success(self):
        res = self.client().post('/movies', headers={"Authorization": "Bearer {}".format(self.executive_producer)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['total_movies'] > 1)

    def tes_post_movies_error(self):
        res = self.client().get('/movies', headers={"Authorization": "Bearer {}".format(self.casting_assistant)})  
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401) 
        self.assertTrue(data['code'], 'unauthorized')
        self.assertTrue(['description'], 'Permision Not Found.')

    # DELETE Movie 
    def test_delete_movies_success(self):
        res = self.client().get('/movies/10', headers={"Authorization": "Bearer {}".format(self.executive_producer)})
        data = json.loads(res.data)
        movie = Movie.query.get(10)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['deleted_movie'], 10)
        self.assertIsNone(movie)


    def test_delete_movies_error(self):
        res = json.client().get('/movies/700', headers={"Authorization": "Bearer {}".format(self.executive_producer)})  
        data = json.loads(res.data)
        movie = Movie.query.get(700)  

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'resource not found')

    # PATCH Movie  
    def test_update_movies_success(self):
        res = self.client().patch('/movies/5',headers={"Authorization": "Bearer {}".format(self.casting_director)}, json=self.update_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_update_movies_error(self):
        res = self.client().patch('/movies/5',headers={"Authorization": "Bearer {}".format(self.casting_assistant)}, json=self.update_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')
    
    # GET Actor
    def test_get_actors_success(self):
        res = self.client().get('/actors',headers={"Authorization": "Bearer {}".format(self.casting_assistant)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_get_actors_error(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')
        self.assertEqual(data['description'], 'Authorization header is expected.')    
   

    # POST Actor
    def test_post_new_actors_succes(self):
        res = self.client().post('/actors',headers={"Authorization": "Bearer {}".format(self.executive_producer)}, json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_post_actor_error(self):
        res = self.client().post('/actors', headers={"Authorization": "Bearer {}".format(self.casting_assistant)}, json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.') 



    # DELETE Actor 
    def test_delete_actors_success(self):
        res = self.client().get('/actors/3', headers={"Authorization": "Bearer {}".format(self.casting_director)})
        data = json.loads(res.data)
        movie = Movie.query.get(3)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['deleted_actor'], 3)
        self.assertIsNone(movie)

    def test_delete_actors_error(self):
        res = self.client().delete('/actors/1', headers={"Authorization": "Bearer {}".format(self.casting_assistant)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found')

