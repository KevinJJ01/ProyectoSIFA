from flask import Flask, render_template
from .config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .mi_blueprint import mi_blueprint
from app.usuario import usuario 
from app.aprendiz import aprendiz
from app.ficha import ficha
from app.auth import auth
from flask_bootstrap import Bootstrap

#inicializar el objeto flask
app = Flask(__name__)
app.config.from_object(Config)


#inicializar el objeto SQLALCHEMY
db=SQLAlchemy(app)
migrate=Migrate(app, db )
bootstrap=Bootstrap(app)
login=LoginManager(app)
login.login_view="/auth/login"


#registrar modulos(blueprints)
app.register_blueprint(mi_blueprint)
app.register_blueprint(usuario)
app.register_blueprint(ficha)
app.register_blueprint(auth)

@app.route('/prueba')
def prueba():
    return render_template("base.html")


from .models import Usuario, Ficha, Aprendiz