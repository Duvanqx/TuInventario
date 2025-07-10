from flask import Blueprint, render_template, session, request, redirect, url_for
from app.models.calis import verClientes, agregarCalis, verCalis, agregarAbonos, editarCalis, obtenerCatalogos, eliminarCalis
from datetime import datetime

cali = Blueprint('cali', __name__, url_prefix='/')

@cali.route('/ver_cali/<int:id_catalogo>', methods=['GET', 'POST'])
def verCali(id_catalogo):
    if 'usuario_id' not in session:
        return redirect('/')
    usuario = session['usuario_id']
    calis = verCalis(usuario, id_catalogo)

    if request.method == 'POST':
        id_cali = request.form['id_cali']
        raw = request.form['abono']
        abono = float(raw.replace(".", "").replace(",", "."))
        fecha = datetime.now()
        agregarAbonos(id_cali, abono, fecha)
        return redirect(url_for('cali.verCali', id_catalogo=id_catalogo))

    return render_template('cali.html', calis=calis, id_catalogo=id_catalogo)

@cali.route('/agregar_cali/<int:id_catalogo>', methods=['GET', 'POST'])
def agregarCali(id_catalogo):
    usuario = session['usuario_id']
    clientes = verClientes(usuario)

    if request.method == 'POST':
        cliente = request.form['nombre']
        raw = request.form['dinero']
        adeudado = float(raw.replace(".", "").replace(",", "."))
        agregarCalis(usuario, id_catalogo, cliente, adeudado)
        return redirect(url_for('cali.verCali', id_catalogo=id_catalogo))

    return render_template('addcali.html', clientes=clientes)

@cali.route('/editar_cali/<int:id_cali>', methods=['GET', 'POST'])
def editarCali(id_cali):
    usuario = session['usuario_id']
    clientes = verClientes(usuario)
    catalogos = obtenerCatalogos(id_cali, usuario)

    if request.method == 'POST':
        cliente = request.form['nombre']
        raw = request.form['dinero']
        dinero = float(raw.replace(".", "").replace(",", "."))
        editarCalis(id_cali, cliente, dinero, usuario)
        return redirect(url_for('cali.verCali', id_catalogo=catalogos))

    return render_template('editcali.html', clientes=clientes)

@cali.route('/eliminar_cali/<int:id_cali>')
def eliminarCali(id_cali):
    catalogos = obtenerCatalogos(id_cali, session['usuario_id'])
    eliminarCalis(id_cali)
    return redirect(url_for('cali.verCali', id_catalogo=catalogos))
