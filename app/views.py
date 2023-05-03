from flask import render_template, redirect, url_for

from .forms import MovieForm, ReviewForm
from .models import Movie, Review
from . import app, db

from pathlib import Path
from werkzeug.utils import secure_filename


BASEP = Path(__file__).parent
UPLOAD_FOLDER = BASEP / 'static' / 'images'


@app.route("/")
def index():
    movies = Movie.query.all()

    return render_template("index.html", movies=movies)


@app.route("/movie/<int:id>", methods=["GET", "POST"])
def movie(id):
    movie_inf = Movie.query.get(id)
    form = ReviewForm()
    reviews_list = movie_inf.review
    avg = round(sum([i.rating for i in reviews_list]) / len(reviews_list), 1)

    if form.validate_on_submit():
        new_review = Review()
        new_review.name = form.name.data
        new_review.text = form.text.data
        new_review.rating = form.rating.data
        new_review.movie_id = id

        db.session.add(new_review)
        db.session.commit()

    return render_template("movie.html", movie_inf=movie_inf, avg=avg, form=form)


@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    form = MovieForm()

    if form.validate_on_submit():
        new_movie = Movie()
        new_movie.title = form.title.data
        new_movie.description = form.description.data

        img = form.img.data
        img_name = secure_filename(img.filename)
        UPLOAD_FOLDER.mkdir(exist_ok=True)
        img.save(UPLOAD_FOLDER / img_name)

        new_movie.img = img_name

        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for("index"))

    return render_template("add_movie.html", form=form)


@app.route("/reviews")
def reviews():
    reviews_list = Review.query.all()

    return render_template("reviews.html", reviews_list=reviews_list)


@app.route("/delete_review/<int:id>")
def delete_review(id):
    review_d = Review.query.get(id)
    db.session.delete(review_d)
    db.session.commit()

    return redirect(url_for("reviews"))
