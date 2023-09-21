from app import db, login 
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

##method login 
class Cliente(db.Model, UserMixin):
    __tablename__= "usuario"
    idUsuario = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), unique = True)
    password = db.Column(db.Integer, unique = True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password, password)

##autentication for user  
@login.user_loader
def load_user(id):
    return Cliente.query.get(id)

##tables for proyect
class Usuario(db.Model):
    __tablename__="usuario"
    idUsuario = db.Column(db.Integer, primary_key = True)
    nombreUsuario = db.Column(db.String(120), unique = True)
    tipoDocumento = db.Column(db.String(120))
    documentoUsuario = db.Column(db.Integer, unique = True)
    celularUsuario = db.Column(db.Integer)
    rol = db.Column(db.String(120))
    correo = db.Column(db.String(120), unique = True)
    password = db.Column(db.Integer, unique = True)



class Ficha(db.Model):
    __tablename__= "ficha"
    idFicha = db.Column(db.Integer, primary_key = True)
    programaFormacion = db.Column(db.String(120))
    areaFormacion = db.Column(db.String(120))
    lugarFormacion = db.Column(db.String(120))
    estadoFicha = db.Column(db.String(120))
    idUsuario= db.Column(db.Integer,
                          db.ForeignKey('usuario.idUsuario'))
    


class Aprendiz(db.Model):
    __tablename__= "aprendiz"
    idAprendiz = db.Column(db.Integer, primary_key = True)
    nombreAprendiz = db.Column(db.String(120))
    tipodocAprendiz = db.Column(db.String(120))
    documentoAprendiz = db.Column(db.Integer, unique = True)
    celularAprendiz = db.Column(db.Integer)
    correoAprendiz = db.Column(db.String(120), unique = True)
    fechaNacimientoAprendiz = db.Column(db.DateTime , default = datetime.utcnow)
    estadoAprendiz = db.Column(db.Boolean)
    observaciones = db.Column(db.String(120))
    idFicha= db.Column(db.Integer,
                          db.ForeignKey('ficha.idFicha'))