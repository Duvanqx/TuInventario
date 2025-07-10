from flask import Blueprint, render_template, request, redirect, session, current_app
from app.models.clientes import agregarClientes, verClientes, eliminarClientes, editarClientes, informacionClientes
cliente = Blueprint('cliente', __name__, url_prefix='/')

@cliente.route('/ver_cliente')
def verCliente():
    if 'usuario_id' not in session:
        return redirect('/')
    usuario = session['usuario_id']
    mysql = current_app.mysql
    clientes = verClientes(usuario,mysql)
    return render_template('clientes.html', clientes=clientes)

@cliente.route('/agregar_cliente', methods=['GET', 'POST'])
def agregarCliente():
    if request.method == 'POST':
        usuario = session['usuario_id']
        nombre_completo = request.form['nombre_completo']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        mysql = current_app.mysql

        agregarClientes(usuario,nombre_completo,telefono,direccion,mysql)
        return redirect('/ver_cliente')
    return render_template('addcliente.html')

@cliente.route('/eliminar_cliente/<int:id_cliente>')
def eliminarCliente(id_cliente):
    mysql = current_app.mysql
    eliminarClientes(id_cliente, mysql)
    return redirect('/ver_cliente')

@cliente.route('/editar_cliente/<int:id_cliente>', methods=['GET', 'POST'])
def editarCliente(id_cliente):
    if request.method == 'POST':
        nombre_completo = request.form['nombre_completo']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        mysql = current_app.mysql

        editarClientes(nombre_completo,telefono,direccion,id_cliente, mysql)
        return redirect('/ver_cliente')
    
    mysql = current_app.mysql
    cliente = informacionClientes(id_cliente, mysql)
    return render_template('editcliente.html', cliente=cliente)
    