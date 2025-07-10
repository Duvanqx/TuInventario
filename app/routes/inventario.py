from flask import Blueprint, render_template, session, redirect, request
from werkzeug.utils import secure_filename
import os
import uuid
from app.models.inventarios import agregarProductos, verProductos, editarProductos, obtenerProducto, eliminarProductos
from app.utils.uploads import allowed_file

inventario = Blueprint('inventario', __name__, url_prefix='/')

@inventario.route('/ver_inventario')
def verInventario():
    if 'usuario_id' not in session:
        return redirect('/')
    productos = verProductos(session['usuario_id'])
    return render_template('inventario.html', productos=productos)

@inventario.route('/agregar_producto', methods=['POST', 'GET'])
def agregarProducto():
    if request.method == 'POST':
        usuario = session['usuario_id']
        nombre = request.form['nombre']
        categoria = request.form['categoria']
        cantidad = request.form['cantidad']
        descripcion = request.form['descripcion']
        raw = request.form['precio']
        precio = float(raw.replace(".", "").replace(",", "."))
        imagen = request.files.get('imagen')

        ruta_imagen = None
        if imagen and imagen.filename != '' and allowed_file(imagen.filename):
            filename = f"{uuid.uuid4().hex}_{secure_filename(imagen.filename)}"
            upload_path = os.path.join('app/static/uploads', filename)
            imagen.save(upload_path)
            ruta_imagen = upload_path

        agregarProductos(usuario, nombre, categoria, cantidad, descripcion, precio, ruta_imagen)
        return redirect('/ver_inventario')

    return render_template('addproducto.html')

@inventario.route('/editar_producto/<int:id_producto>', methods=['POST', 'GET'])
def editarProducto(id_producto):
    if request.method == 'POST':
        nombre = request.form['nombre']
        categoria = request.form['categoria']
        cantidad = request.form['cantidad']
        descripcion = request.form['descripcion']
        raw = request.form['precio']
        precio = float(raw.replace(".", "").replace(",", "."))
        imagen = request.files.get('imagen')

        ruta_imagen = None
        if imagen and imagen.filename != '' and allowed_file(imagen.filename):
            filename = f"{uuid.uuid4().hex}_{secure_filename(imagen.filename)}"
            upload_path = os.path.join('app/static/uploads', filename)
            imagen.save(upload_path)
            ruta_imagen = upload_path

        editarProductos(nombre, categoria, cantidad, descripcion, precio, ruta_imagen, id_producto)
        return redirect('/ver_inventario')
    
    producto = obtenerProducto(id_producto)
    return render_template('editproducto.html', productos=producto)

@inventario.route('/eliminar_producto/<int:id_producto>')
def eliminarProducto(id_producto):
    eliminarProductos(id_producto)
    return redirect('/ver_inventario')
