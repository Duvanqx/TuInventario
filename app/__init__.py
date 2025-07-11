from flask import Flask
from app.config import Config
from app.extensions import db  

from app.routes.index import index
from app.routes.registro import registro
from app.routes.login import login
from app.routes.logout import cerrar
from app.routes.catalogo import catalogo
from app.routes.cliente import cliente
from app.routes.cali import cali
from app.routes.inventario import inventario
from app.routes.perfil import perfil
from app.routes.historial import historiales

import pymysql
pymysql.install_as_MySQLdb()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app) 


    app.register_blueprint(index)
    app.register_blueprint(registro)
    app.register_blueprint(login)
    app.register_blueprint(cerrar)
    app.register_blueprint(catalogo)
    app.register_blueprint(cliente)
    app.register_blueprint(cali)
    app.register_blueprint(inventario)
    app.register_blueprint(perfil)
    app.register_blueprint(historiales)

    return app
