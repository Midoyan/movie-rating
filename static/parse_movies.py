import sqlite3
import time

import requests
import json
from pathlib import Path


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)

    return conn


def parse_movies():
    api_string = 'http://www.omdbapi.com/?apikey=65e3d2fc&i='
    id_list = ['tt0111161', 'tt0068646', 'tt0468569', 'tt0071562', 'tt0050083', 'tt0108052', 'tt0167260', 'tt0110912',
               'tt0120737', 'tt0060196', 'tt0109830', 'tt0137523', 'tt0167261', 'tt1375666', 'tt0080684', 'tt0133093',
               'tt0099685', 'tt0073486', 'tt0114369', 'tt0047478', 'tt0038650', 'tt0102926', 'tt0317248', 'tt0120815',
               'tt0118799', 'tt0816692', 'tt0120689', 'tt0076759', 'tt0103064', 'tt0088763', 'tt0245429', 'tt0054215',
               'tt0253474', 'tt6751668', 'tt0110413', 'tt0110357', 'tt0172495', 'tt0120586', 'tt0407887', 'tt0114814',
               'tt0482571', 'tt2582802', 'tt0034583', 'tt0056058', 'tt0095327', 'tt1675434', 'tt0027977', 'tt0064116',
               'tt0047396', 'tt0095765']
    movies = []

    print('fetching movies dictionary')

    try:
        for i in range(len(id_list)):
            print(i, id_list[i])
            movie = requests.get(api_string + id_list[i])
            movie_dict = json.loads(movie.text)
            movies.append(movie_dict)
            # print(movie_dict)
    except:
        print("An exception occurred")

    # add to db
    print("Adding to DB")

    database = Path(__file__).parents[1] / 'backend/db.sqlite'

    if database.is_file():
        conn = create_connection(database)
        c = conn.cursor()

        c.execute('DELETE FROM Movies;', )

        for movie in movies:
            print(movie)

            c.execute("INSERT INTO Movies(imdb_id,year,title,date,runtime,genre,director,writer,actors,plot,country,"
                      "awards,poster,imdb_rating,imdb_votes,box_office) "
                      "VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                      (movie['imdbID'], movie['Year'], movie['Title'], movie['Released'],
                       movie['Runtime'], movie['Genre'], movie['Director'], movie['Writer'],
                       movie['Actors'], movie['Plot'], movie['Country'], movie['Awards'],
                       movie['Poster'], movie['imdbRating'], movie['imdbVotes'],
                       movie['BoxOffice']))
        conn.commit()
        conn.close()
    else:
        raise Exception('Wrong database path')


if __name__ == '__main__':
    parse_movies()
