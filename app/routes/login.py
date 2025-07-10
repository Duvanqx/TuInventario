from flask import Blueprint, render_template, request, redirect, flash, session
from werkzeug.security import check_password_hash
from app.models.usuarios import ObtenerUsuario

login = Blueprint('login', __name__)

@login.route('/iniciar_sesion', methods=['GET', 'POST'])
def iniciarSesion():
    if request.method == 'POST':
        correo = request.form['correo']
        contraseña = request.form['contraseña']

        usuario = ObtenerUsuario(correo)
        if usuario and check_password_hash(usuario.contraseña, contraseña):
            session['usuario_id'] = usuario.id_usuario
            session['nombres'] = usuario.nombres
            return redirect('/')
        else:
            flash("Correo o contraseña incorrectos", 'error')
    return render_template("login.html")
