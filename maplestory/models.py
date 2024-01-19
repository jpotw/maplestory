from flask_wtf import FlaskForm
from wtforms import SubmitField



class Button(FlaskForm):
    submit = SubmitField('강화하기')