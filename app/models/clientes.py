from app import db
from app.models.modelos import Cliente

def agregarClientes(usuario, nombre_completo, telefono, direccion):
    nuevo = Cliente(
        id_usuario=usuario,
        nombre_completo=nombre_completo,
        telefono=telefono,
        direccion=direccion
    )
    db.session.add(nuevo)
    db.session.commit()

def verClientes(usuario):
    return Cliente.query.filter_by(id_usuario=usuario).all()

def eliminarClientes(id_cliente):
    Cliente.query.filter_by(id_cliente=id_cliente).delete()
    db.session.commit()

def editarClientes(nombre_completo, telefono, direccion, id_cliente):
    cliente = Cliente.query.get(id_cliente)
    if cliente:
        cliente.nombre_completo = nombre_completo
        cliente.telefono = telefono
        cliente.direccion = direccion
        db.session.commit()

def informacionClientes(id_cliente):
    return Cliente.query.filter_by(id_cliente=id_cliente).first()
