from flask import Blueprint , render_template, session, redirect
index = Blueprint('index', __name__)

@index.route('/')
def home():
    return render_template('index.html', usuario_id = session.get('usuario_id'), nombres = session.get('nombres'))