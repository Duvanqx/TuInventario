from flask import Blueprint, render_template, session, request, redirect, flash, url_for
from app.models.perfiles import verPerfiles
from app import db
from app.models.modelos import Usuario

perfil = Blueprint('perfil', __name__, url_prefix='/')

@perfil.route('/ver_perfil')
def verPerfil():
    usuario = verPerfiles(session['usuario_id'])
    return render_template("perfil.html", usuario=usuario)


@perfil.route('/editar_perfil/<int:id_usuario>', methods=['GET', 'POST'])
def editarPerfil(id_usuario):
    usuario = Usuario.query.get_or_404(id_usuario)

    if request.method == 'POST':
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        telefono = request.form['telefono']
        correo = request.form['correo']

        
        existe = Usuario.query.filter(Usuario.correo == correo, Usuario.id_usuario != id_usuario).first()
        if existe:
            flash('❌ El correo ya está registrado en otra cuenta.', 'error')
            return redirect(url_for('perfil.editarPerfil', id_usuario=id_usuario))

        
        usuario.nombres = nombres
        usuario.apellidos = apellidos
        usuario.telefono = telefono
        usuario.correo = correo

        db.session.commit()
        flash('✅ Perfil actualizado correctamente.', 'success')
        return redirect(url_for('perfil.verPerfil'))

    return render_template("editperfil.html", usuario=usuario)

