import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json


database_name = "agency"
database_path = os.environ.get('DATABASE_URL')
if not database_path:
    database_name = "agency"
    database_path = "postgres://{}:{}@{}/{}".format('postgres', '90', 'localhost:5432',database_name)


db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    migrate = Migrate(app, db)
    db.app = app
    db.init_app(app)
    db.create_all()


class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_date = Column(db.String)
    # casting = db.relationship('Casting', backref=db.backref('movie', lazy=True))


    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
        }


    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Actor(db.Model):
    __tablename__ = "actor"
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String)
    age = db.Column(Integer)
    gender = db.Column(String)
    # casting = db.relationship('Casting', backref=db.backref('actor', lazy=True))


    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }

# class Casting(db.Model):
#     __tablename__ = 'casting'
#     id = db.Column(db.Integer, primary_key=True)
#     actor_id = db.Column(db.Integer, db.ForeignKey('Actor.id'), nullable=False)
#     movie_id = db.Column(db.Integer, db.ForeignKey('Movie.id'), nullable=False)
    
    # def __init__(self, actor_id, movie_id):
    #     self.actor_id = actor_id
    #     self.movie_id = movie_id

    # def format(self):
    #     return {
    #         'id': self.id,
    #         'actor_id': self.actor_id,
    #         'movie_id': self.movie_id,
    #     }

    # def insert(self):
    #     db.session.add(self)
    #     db.session.commit()

    # def update(self):
    #     db.session.commit()

    # def delete(self):
    #     db.session.delete(self)
    #     db.session.commit()