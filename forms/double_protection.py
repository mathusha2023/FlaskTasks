from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class DoubleProtectForm(FlaskForm):
    id = StringField("id астронавта", validators=[DataRequired()])
    password = PasswordField("Пароль астронавта", validators=[DataRequired()])
    captain_id = StringField("id капитана", validators=[DataRequired()])
    captain_password = PasswordField("Пароль капитана", validators=[DataRequired()])
    submit = SubmitField("Доступ", validators=[DataRequired()])
