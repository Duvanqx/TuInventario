from flask import Blueprint, render_template, session, current_app, request, redirect
from app.models.perfiles import verPerfiles, editarPerfiles
perfil = Blueprint('perfil', __name__, url_prefix='/')

@perfil.route('/ver_perfil')
def verPerfil():
    usuario = verPerfiles(session['usuario_id'], current_app.mysql)
    return render_template("perfil.html", usuario=usuario)

@perfil.route('/editar_perfil/<int:id_usuario>', methods= ['POST', 'GET'])
def editarPerfil(id_usuario):
    if request.method == 'POST':
        mysql = current_app.mysql
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        telefono = request.form['telefono']
        correo = request.form['correo']

        editarPerfiles(nombres, apellidos, telefono, correo,id_usuario, mysql)
        return redirect('/ver_perfil')
    usuario = verPerfiles(id_usuario, current_app.mysql)
    return render_template("editperfil.html", usuario=usuario)