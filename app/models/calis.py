from app import db
from app.models.modelos import Cliente, Cali, Pago, Catalogo, Usuario
from sqlalchemy.sql import func

def verClientes(usuario_id):
    return Cliente.query.filter_by(id_usuario=usuario_id).all()

def agregarCalis(usuario, catalogo, cliente, adeudado):
    nuevo = Cali(id_usuario=usuario, id_catalogo=catalogo, id_cliente=cliente, adeudado=adeudado)
    db.session.add(nuevo)
    db.session.commit()

def verCalis(usuario, id_catalogo):
    results = (
        db.session.query(
            Usuario.id_usuario,
            Usuario.nombres.label("nombre_usuario"),
            Catalogo.nombre.label("nombre_catalogo"),
            Cliente.nombre_completo.label("nombre_cliente"),
            Cali.id_cali,
            Cali.adeudado,
            func.IFNULL(func.sum(Pago.valor), 0).label("total_abonado"),
            (Cali.adeudado - func.IFNULL(func.sum(Pago.valor), 0)).label("saldo_restante")
        )
        .join(Cali, Cali.id_usuario == Usuario.id_usuario)
        .join(Catalogo, Catalogo.id_catalogo == Cali.id_catalogo)
        .join(Cliente, Cliente.id_cliente == Cali.id_cliente)
        .outerjoin(Pago, Pago.id_cali == Cali.id_cali)
        .filter(Cali.id_usuario == usuario, Cali.id_catalogo == id_catalogo)
        .group_by(Cali.id_cali, Usuario.id_usuario, Catalogo.nombre, Cliente.nombre_completo, Cali.adeudado, Usuario.nombres)
        .order_by(Cliente.nombre_completo)
        .all()
    )
    return results

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
