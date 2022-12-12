from dataclasses import dataclass
from datetime import datetime

import app


@dataclass
class Votes(app.db.Model):
    id: int
    film_id: str
    mark_id: int
    date: datetime

    id = app.db.Column(app.db.Integer(), primary_key=True)
    # film_id = app.db.Column(app.db.Integer())
    film_id = app.db.Column(app.db.Integer, app.db.ForeignKey('movies.id'), nullable=False)
    mark_id = app.db.Column(app.db.Integer())
    date = app.db.Column(app.db.DateTime())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'<Votes id: {self.id} - {self.film_id} - {self.mark_id} - {self.date}'


@dataclass
class Movies(app.db.Model):
    id: int
    imdb_id: str
    title: str
    year: int
    date: str
    runtime: str
    genre: str
    director: str
    writer: str
    actors: str
    plot: str
    country: str
    awards: str
    poster: str
    imdb_rating: str
    imdb_votes: int
    rating: str
    # votes: int
    box_office: str

    id = app.db.Column(app.db.Integer(), primary_key=True)
    imdb_id = app.db.Column(app.db.String(100))
    year = app.db.Column(app.db.Integer())
    title = app.db.Column(app.db.String(100))
    date = app.db.Column(app.db.String(100))
    runtime = app.db.Column(app.db.String(100))
    genre = app.db.Column(app.db.String(100))
    director = app.db.Column(app.db.String(100))
    writer = app.db.Column(app.db.String(100))
    actors = app.db.Column(app.db.String(100))
    plot = app.db.Column(app.db.String(400))
    country = app.db.Column(app.db.String(100))
    awards = app.db.Column(app.db.String(100))
    poster = app.db.Column(app.db.String(300))
    imdb_rating = app.db.Column(app.db.String(100))
    imdb_votes = app.db.Column(app.db.Integer())
    rating = app.db.Column(app.db.String(100))
    # votes = app.db.Column(app.db.Integer())
    votes = app.db.relationship('Votes', backref='movies', lazy=True)
    box_office = app.db.Column(app.db.String(100))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'<Movie id: {self.id} - {self.imdb_id} - {self.title} - {self.rating} - {self.votes}'
