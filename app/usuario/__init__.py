from flask import Blueprint 
usuario=Blueprint('usuario',
                    __name__,
                    url_prefix = '/usuario',
                    template_folder = 'templates')

from . import routes