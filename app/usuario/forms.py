from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, EmailField, PasswordField
from wtforms.validators import InputRequired,NumberRange, Email, Length




class usuaForm():    
    email =  StringField("Ingrese su correo",validators=[InputRequired(message='correo requerido')])
    password = PasswordField("Ingrese la contraseña",validators=[InputRequired(message='Contraseña requerida')])
    



class NewUsuaForm(FlaskForm):
     email =  StringField("Ingrese su correo",validators=[InputRequired(message='correo requerido')])
    
    

class EditUsuaForm(FlaskForm,
                          usuaForm):
        submit = SubmitField("Actualizar")


