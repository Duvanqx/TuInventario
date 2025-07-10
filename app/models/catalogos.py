from app import db
from app.models.modelos import Catalogo

def agregarCatalogos(usuario, nombre, fecha_inicio, fecha_fin, fecha_pago, foto):
    nuevo = Catalogo(
        id_usuario=usuario,
        nombre=nombre,
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin,
        fecha_limite_pago=fecha_pago,
        foto=foto
    )
    db.session.add(nuevo)
    db.session.commit()

def verCatalogos(id_usuario):
    return Catalogo.query.filter_by(id_usuario=id_usuario).all()

def eliminarCatalogos(id_catalogo):
    Catalogo.query.filter_by(id_catalogo=id_catalogo).delete()
    db.session.commit()

def editarCatalogos(id_catalogo, ruta_foto, nombre, fecha_inicio, fecha_fin, fecha_pago):
    catalogo = Catalogo.query.get(id_catalogo)
    if catalogo:
        catalogo.nombre = nombre
        catalogo.fecha_inicio = fecha_inicio
        catalogo.fecha_fin = fecha_fin
        catalogo.fecha_limite_pago = fecha_pago
        if ruta_foto:
            catalogo.foto = ruta_foto
        db.session.commit()

def informacionCatalogos(id_catalogo):
    return Catalogo.query.filter_by(id_catalogo=id_catalogo).first()
