from app.models.modelos import Usuario
from app import db

def verPerfiles(usuario_id):
    return Usuario.query.filter_by(id_usuario=usuario_id).first()

def editarPerfiles(nombres, apellidos, telefono, correo, usuario_id):
    usuario = Usuario.query.get(usuario_id)
    if usuario:
        usuario.nombres = nombres
        usuario.apellidos = apellidos
        usuario.telefono = telefono
        usuario.correo = correo
        db.session.commit()
