from flask import Flask, Response
from flask import render_template
from flask import jsonify
from flask import request
from flask import redirect
from flask import url_for
from flask_cors import CORS

from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

from config import Config
from datetime import datetime
from main import evaluate_rating
from words_model import words_7

load_dotenv('./.flaskenv')

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
import models

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/', methods=['GET'])
def index():
    return "hello, world"


@app.route('/api/getCarHistory', methods=['GET'])
def get():
    carHistory = models.Task.query.all()
    return jsonify(carHistory)


@app.route('/api/getMovies', methods=['GET'])
def get_movies():
    movies = models.Movies.query.all()
    return jsonify(movies)


@app.route('/api/getMovieRating/<int:movie_id>', methods=['GET'])
def get_movie_rating(movie_id):
    # movie = models.Movies.query.get(movie_id)
    response = models.Movies.query.join(models.Votes).filter(models.Votes.film_id == movie_id).all()
    # test_response = response
    if response:
        grades = []
        ratings = list(words_7['words'].keys())
        # print(response)
        # print(type(response))
        # print(response[0], type(response[0]))
        # print(response[0].id, type(response[0].id))
        # print(response[0].votes, type(response[0].votes))
        for i in response[0].votes:
            print("hola", i.id, i.film_id, i.mark_id, i.date)
            grades.append(ratings[i.mark_id])

        # return jsonify(response[0].votes)
        print(grades)
        result = list(evaluate_rating(grades))
        response = {"mark": result[0], "value": result[1]}
        return jsonify(response)
    else:
        return jsonify({})


@app.route('/api/getMovieVotes/<int:movie_id>', methods=['GET'])
def get_movie_votes(movie_id):
    # movie = models.Movies.query.get(movie_id)
    response = models.Movies.query.join(models.Votes).filter(models.Votes.film_id == movie_id).all()
    # test_response = response
    if response:
        print(response)
        print(type(response))
        print(response[0], type(response[0]))
        print(response[0].id, type(response[0].id))
        print(response[0].votes, type(response[0].votes))
        for i in response[0].votes:
            print("hola", i.id, i.film_id, i.mark_id, i.date)

        return jsonify(response[0].votes)
    else:
        return jsonify({})


@app.route('/api/getMovie/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    movie = models.Movies.query.get(movie_id)
    return jsonify(movie)


@app.route('/api/vote', methods=['POST'])
def submit_vote():
    # fuzzy_model = model()

    user_input = request.get_json()

    # car_condition = carEvaluation(int(user_input["age"]), int(user_input["mileage"]), int(user_input["repairments"]),
    #                              fuzzy_model[0], fuzzy_model[1], fuzzy_model[2])

    # est_price = user_input["selectedCarObj"]["price"] * car_condition[0] * 0.1
    # if str(user_input["areDocsInOrder"]) != 'True':
    #    est_price *= 0.2

    # response = {"price": est_price}
    # task = models.Task(
    #     age=user_input["age"],
    #     mileage=user_input["mileage"],
    #     repairments=user_input["repairments"],
    #     brand=user_input["selectedCarObj"]["brand"],
    #     name=user_input["selectedCarObj"]["name"],
    #     documents=user_input["areDocsInOrder"],
    #     est_price=response["price"])
    vote = models.Votes(
        film_id=user_input["film_id"],
        mark_id=user_input["mark_id"],
        date=datetime.now()
    )
    db.session.add(vote)
    db.session.commit()
    return jsonify(vote)


@app.route('/api/evaluate', methods=['POST'])
def get_price():
    fuzzy_model = model()
    user_input = request.get_json()
    car_condition = carEvaluation(int(user_input["age"]), int(user_input["mileage"]), int(user_input["repairments"]),
                                  fuzzy_model[0], fuzzy_model[1], fuzzy_model[2])
    est_price = user_input["selectedCarObj"]["price"] * car_condition[0] * 0.1
    if str(user_input["areDocsInOrder"]) != 'True':
        est_price *= 0.2

    response = {"price": est_price}
    task = models.Task(
        age=user_input["age"],
        mileage=user_input["mileage"],
        repairments=user_input["repairments"],
        brand=user_input["selectedCarObj"]["brand"],
        name=user_input["selectedCarObj"]["name"],
        documents=user_input["areDocsInOrder"],
        est_price=response["price"])
    db.session.add(task)
    db.session.commit()
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
