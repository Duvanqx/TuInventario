from flask import Blueprint, render_template
from app import db
from app.models.modelos import Cliente, Pago, Catalogo, Cali

historiales = Blueprint('historiales', __name__)

@historiales.route('/historial/<int:id_catalogo>')
def historial(id_catalogo):
    pagos = db.session.query(
        Cliente.nombre_completo.label("cliente"),
        Pago.valor.label("monto_pago"),
        Pago.fecha.label("fecha_pago"),
        Catalogo.nombre.label("catalogo")
    ).join(Cali, Pago.id_cali == Cali.id_cali)\
     .join(Cliente, Cali.id_cliente == Cliente.id_cliente)\
     .join(Catalogo, Cali.id_catalogo == Catalogo.id_catalogo)\
     .filter(Catalogo.id_catalogo == id_catalogo)\
     .order_by(Pago.fecha.desc())\
     .all()

    return render_template("historial.html", pagos=pagos)