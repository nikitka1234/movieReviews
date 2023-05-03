from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, FileField, SubmitField
from wtforms.validators import Optional, DataRequired


class MovieForm(FlaskForm):
    title = StringField("Название",
                        validators=[DataRequired(message='Поле "Название" не может быть пустым')])
    description = TextAreaField("Описание",
                                validators=[DataRequired(message='Поле "Описание" не может быть пустым')])
    img = FileField("Изображение", validators=[Optional()])
    submit = SubmitField("Добавить")


class ReviewForm(FlaskForm):
    name = StringField("Имя",
                        validators=[DataRequired(message='Поле "Имя" не может быть пустым')])
    text = TextAreaField("Отзыв",
                         validators=[DataRequired(message='Поле "Отзыв" не может быть пустым')])
    rating = SelectField("Оценка", choices=list(range(10, -1, -1)), default=10)
    submit = SubmitField("Добавить")
