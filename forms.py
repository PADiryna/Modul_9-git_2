from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class LibraryBookForm(FlaskForm):
  title = StringField('title', validators=[DataRequired()])
  ganre = StringField('ganre', validators=[DataRequired()])
  author = StringField('author', validators=[DataRequired()])
  date = StringField('date', validators=[DataRequired()])
  description = TextAreaField('description', validators=[DataRequired()])
  