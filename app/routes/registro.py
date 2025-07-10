from flask import Blueprint, render_template, request, redirect, session
from werkzeug.security import generate_password_hash
from app.models.usuarios import registrarUsuario

registro = Blueprint('registro', __name__)

@registro.route('/registro', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        telefono = request.form['telefono']
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        contraseña_hash = generate_password_hash(contraseña)

        id_usuario = registrarUsuario(nombres, apellidos, telefono, correo, contraseña_hash)

        session['usuario_id'] = id_usuario
        session['nombres'] = nombres
        return redirect('/')
    return render_template('registro.html')
