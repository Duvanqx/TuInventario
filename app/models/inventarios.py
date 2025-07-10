from app import db
from app.models.modelos import Producto

def agregarProductos(usuario, nombre, categoria, cantidad, descripcion, precio, imagen):
    nuevo = Producto(
        id_usuario=usuario,
        nombre=nombre,
        categoria=categoria,
        cantidad=cantidad,
        descripcion=descripcion,
        precio=precio,
        imagen=imagen
    )
    db.session.add(nuevo)
    db.session.commit()

def verProductos(usuario):
    return Producto.query.filter_by(id_usuario=usuario).all()

def editarProductos(nombre, categoria, cantidad, descripcion, precio, imagen, producto_id):
    producto = Producto.query.get(producto_id)
    if producto:
        producto.nombre = nombre
        producto.categoria = categoria
        producto.cantidad = cantidad
        producto.descripcion = descripcion
        producto.precio = precio
        producto.imagen = imagen
        db.session.commit()

def obtenerProducto(producto_id):
    return Producto.query.filter_by(id_producto=producto_id).first()

def eliminarProductos(producto_id):
    Producto.query.filter_by(id_producto=producto_id).delete()
    db.session.commit()
