from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL


class URLForm(FlaskForm):
    long_url = StringField('URL', [DataRequired(), URL(
        message="Must be a valid URL with http:// or https://")])
    submit = SubmitField('Shorten iT!')
