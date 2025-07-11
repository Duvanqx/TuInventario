from app import db
from app.models.modelos import Cliente, Cali, Pago
from sqlalchemy.sql import func

def verClientes(usuario_id):
    return Cliente.query.filter_by(id_usuario=usuario_id).all()

def agregarCalis(usuario, catalogo, cliente, adeudado):
    nuevo = Cali(id_usuario=usuario, id_catalogo=catalogo, id_cliente=cliente, adeudado=adeudado)
    db.session.add(nuevo)
    db.session.commit()

def verCalis(usuario, id_catalogo):
    results = (
        db.session.query(Cali.id_cali, Cliente.nombre_completo.label("nombre_cliente"), Cali.adeudado,
                         func.coalesce(func.sum(Pago.valor), 0).label("total_abonado"))
        .join(Cliente, Cliente.id_cliente == Cali.id_cliente)
        .outerjoin(Pago, Pago.id_cali == Cali.id_cali)
        .filter(Cali.id_usuario == usuario, Cali.id_catalogo == id_catalogo)
        .group_by(Cali.id_cali, Cliente.nombre_completo, Cali.adeudado)
        .all()
    )

    return [
        {
            "id_cali": r.id_cali,
            "nombre_cliente": r.nombre_cliente,
            "adeudado": r.adeudado,
            "total_abonado": r.total_abonado,
            "saldo_restante": r.adeudado - r.total_abonado
        } for r in results
    ]


def agregarAbonos(cali, valor, fecha):
    nuevo = Pago(id_cali=cali, valor=valor, fecha=fecha)
    db.session.add(nuevo)
    db.session.commit()

def editarCalis(id_cali, cliente, dinero, usuario):
    cali = Cali.query.filter_by(id_cali=id_cali, id_usuario=usuario).first()
    if cali:
        cali.id_cliente = cliente
        cali.adeudado = dinero
        db.session.commit()

def obtenerCatalogos(id_cali, usuario):
    cali = Cali.query.filter_by(id_cali=id_cali, id_usuario=usuario).first()
    return cali.id_catalogo if cali else None

def eliminarCalis(id_cali):
    Cali.query.filter_by(id_cali=id_cali).delete()
    db.session.commit()

def obtenerCali(id_cali, usuario):
    return Cali.query.filter_by(id_cali=id_cali, id_usuario=usuario).first()
