from flask import Blueprint, render_template, current_app, session, request, redirect, url_for
from app.models.calis import verClientes ,  agregarCalis, verCalis , agregarAbonos, editarCalis, obtenerCatalogos, eliminarCalis
from datetime import datetime
cali = Blueprint('cali', __name__, url_prefix='/')

@cali.route('/ver_cali/<int:id_catalogo>', methods= ['POST', 'GET'])
def verCali(id_catalogo):
    if 'usuario_id' not in session:
        return redirect('/')
    usuario = session['usuario_id']
    mysql = current_app.mysql

    if not usuario:
        return redirect('/inicar_sesion')

    calis = verCalis(usuario, id_catalogo, mysql)

    if request.method == 'POST':
        cali = request.form['id_cali']
        raw = request.form['abono']
        abono = float(raw.replace(".","").replace(",","."))
        fecha = datetime.now()

        agregarAbonos(cali, abono, fecha, mysql)
        return redirect(url_for('cali.verCali', id_catalogo=id_catalogo))
    return render_template('cali.html', calis=calis, id_catalogo=id_catalogo)

@cali.route('/agregar_cali/<int:id_catalogo>', methods=['GET', 'POST'])
def agregarCali(id_catalogo):

    mysql = current_app.mysql
    usuario = session['usuario_id']
    clientes = verClientes(usuario,mysql)


    if request.method == 'POST':
        usuario = session['usuario_id']
        catalogo = id_catalogo
        cliente = request.form['nombre']
        raw = request.form['dinero']
        adeudado = float(raw.replace(".","").replace(",","."))
        mysql = current_app.mysql


        agregarCalis(usuario,catalogo,cliente,adeudado,mysql)
        return redirect(url_for('cali.verCali', id_catalogo=id_catalogo))

    return render_template('addcali.html', clientes=clientes)

@cali.route('/editar_cali/<int:id_cali>', methods = ['GET', 'POST'])
def editarCali(id_cali):
    clientes = verClientes(session['usuario_id'],current_app.mysql)
    catalogos = obtenerCatalogos(id_cali, session['usuario_id'],current_app.mysql)
    if request.method == 'POST':
        cliente = request.form['nombre']
        raw = request.form['dinero']
        dinero = float(raw.replace(".","").replace(",","."))
        usuario = session['usuario_id']
        mysql = current_app.mysql

        editarCalis(id_cali, cliente, dinero, usuario, mysql)
        return redirect(url_for('cali.verCali', id_catalogo=catalogos))
    return render_template('editcali.html',clientes=clientes)

@cali.route('/eliminar_cali/<int:id_cali>')
def eliminarCali(id_cali):
    catalogos = obtenerCatalogos(id_cali, session['usuario_id'],current_app.mysql)
    eliminarCalis(id_cali, current_app.mysql)
    return redirect(url_for('cali.verCali', id_catalogo=catalogos))
