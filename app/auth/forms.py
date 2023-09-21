from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length


class LoginForm(FlaskForm):
    email=StringField(label="Correo electronico",
                        validators=[InputRequired()]
                        )
    password=PasswordField(label="clave",
                           validators=[InputRequired(), Length(8)]
                        )
                           
    submit=SubmitField(label="Iniciar sesion")
