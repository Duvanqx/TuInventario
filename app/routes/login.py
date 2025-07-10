from flask import Blueprint, render_template, request, redirect, flash, session, current_app
from werkzeug.security import check_password_hash
from app.models.usuarios import ObtenerUsuario

login = Blueprint('login', __name__)

@login.route('/iniciar_sesion', methods = ['GET', 'POST'])
def iniciarSesion():
    if request.method == 'POST':
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        mysql = current_app.mysql

        usuario = ObtenerUsuario(correo, mysql)
        if usuario and check_password_hash(usuario[5], contraseña):
            session['usuario_id'] = usuario[0]
            session['nombres'] = usuario[1]
            return redirect('/')
        else:
            flash("Correo o contraseña incorrectos", 'error')
    return render_template("login.html")