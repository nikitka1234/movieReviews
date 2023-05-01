from flask import render_template, redirect

# from .forms import MovieForm, ReviewForm
from .models import Movie, Review
from . import app, db


@app.route("/")
def index():
    movies = Movie.query.all()

    return render_template("index.html", movies=movies)


@app.route("/movie/<int:id>", methods=["GET", "POST"])
def movie(id):
    return "Страница с фильмом"


@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    return "Добавление фильма"


@app.route("/reviews")
def reviews():
    return "Страница с отзывами"


@app.route("/delete_review/<int:id>")
def delete_review(id):
    return "Удаление новости"
