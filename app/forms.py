from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired 

class UploadForm(FlaskForm):
    up_image = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg','png'])])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Add Property')