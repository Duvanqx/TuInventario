from app.models.modelos import Usuario

from app import db

def registrarUsuario(nombres, apellidos, telefono, correo, contraseña_hash):
    usuario = Usuario(
        nombres=nombres,
        apellidos=apellidos,
        telefono=telefono,
        correo=correo,
        contraseña=contraseña_hash
    )
    db.session.add(usuario)
    db.session.commit()
    return usuario.id_usuario

def ObtenerUsuario(correo):
    return Usuario.query.filter_by(correo=correo).first()
