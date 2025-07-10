from flask import Blueprint, render_template, request, session, current_app, redirect
from werkzeug.utils import secure_filename
from datetime import date
import os
import uuid
from app.models.catalogos import agregarCatalogos, verCatalogos, eliminarCatalogos, editarCatalogos, informacionCatalogos
from app.utils.uploads import allowed_file
catalogo = Blueprint('catalogo', __name__, url_prefix='/')

@catalogo.route('/ver_catalogo')
def verCatalogo():
    if 'usuario_id' not in session:
        return redirect('/')
    mysql = current_app.mysql
    catalogos = verCatalogos(session['usuario_id'], mysql)
    return render_template('catalogos.html',catalogos=catalogos, hoy=date.today())

@catalogo.route('/agregar_catalogo', methods=['POST', 'GET'])
def agregarCatalogo():
    if request.method == 'POST':
        usuario = session['usuario_id']
        nombre = request.form['nombre']
        fecha_inicio = request.form['fecha_inicio']
        fecha_fin = request.form['fecha_fin']
        fecha_pago = request.form['fecha_pago']
        foto_file = request.files.get('foto')
        mysql = current_app.mysql

        ruta_foto = None
        if foto_file and foto_file.filename != '' and allowed_file(foto_file.filename):
            filename = f"{uuid.uuid4().hex}_{secure_filename(foto_file.filename)}"
            upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)


            foto_file.save(upload_path)
            ruta_foto = upload_path

        agregarCatalogos(usuario, nombre, fecha_inicio, fecha_fin, fecha_pago, ruta_foto, mysql)
        return redirect('/ver_catalogo')
    return render_template('addcatalogo.html')

@catalogo.route('/eliminar_catalogo/<int:id_catalogo>')
def eliminarCatalogo(id_catalogo):
    mysql = current_app.mysql
    eliminarCatalogos(id_catalogo, mysql)
    return redirect('/ver_catalogo')

@catalogo.route('/editar_catalogo/<int:id_catalogo>', methods = ['POST', 'GET'])
def editarCatalogo(id_catalogo):
    if request.method == 'POST':
        nombre = request.form['nombre']
        fecha_inicio = request.form['fecha_inicio']
        fecha_fin = request.form['fecha_fin']
        fecha_pago = request.form['fecha_pago']
        foto_file = request.files.get('foto')
        mysql = current_app.mysql

        ruta_foto = None
        if foto_file and foto_file.filename != '' and allowed_file(foto_file.filename):
            filename = f"{uuid.uuid4().hex}_{secure_filename(foto_file.filename)}"
            upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)


            foto_file.save(upload_path)
            ruta_foto = upload_path

        editarCatalogos(id_catalogo, ruta_foto, nombre, fecha_inicio, fecha_fin, fecha_pago, mysql)
        return redirect('/ver_catalogo')
    
    mysql = current_app.mysql
    catalogo = informacionCatalogos(id_catalogo, mysql)
    return render_template('editcatalogo.html', catalogo=catalogo)