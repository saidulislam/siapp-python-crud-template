from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms_components import EmailField
from wtforms.validators import DataRequired, Length


class SignupForm(FlaskForm):
    first = StringField("First Name", [DataRequired(), Length(3, 254)])
    last = StringField("Last Name", [DataRequired(), Length(3, 254)])
    email = EmailField("What's your e-mail address?",
                       [DataRequired(), Length(3, 254)])

