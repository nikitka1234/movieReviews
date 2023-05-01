from datetime import datetime

from . import db


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.Text, unique=True, nullable=False)
    img = db.Column(db.String(255), nullable=True)
    review = db.relationship("Review", back_populates="movie")

    def __repr__(self):
        return f"Movie {self.id}: {self.title}"


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    rating = db.Column(db.Integer, nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"), nullable=True)
    movie = db.relationship("Movie", back_populates="review")

    def __repr__(self):
        return f"Review {self.id}: {self.text[:20]}..."
