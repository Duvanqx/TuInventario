def agregarProductos(usuario, nombre, categoria, cantidad, descripcion, precio, imagen, mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO productos(id_usuario, nombre, categoria, cantidad, descripcion, precio, imagen) VALUES (%s, %s, %s, %s, %s, %s, %s)",(usuario, nombre, categoria, cantidad, descripcion, precio, imagen))
    mysql.connection.commit()
    cursor.close()

def verProductos(usuario, mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM productos WHERE id_usuario = %s",(usuario,))
    productos = cursor.fetchall()
    cursor.close()
    return productos

def editarProductos(nombre, categoria, cantidad, descripcion, precio, imagen, producto, mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE productos SET nombre = %s, categoria = %s, cantidad = %s, descripcion = %s, precio = %s, imagen = %s WHERE id_producto = %s",(nombre, categoria, cantidad, descripcion, precio, imagen, producto))
    mysql.connection.commit()
    cursor.close()

def obtenerProducto(producto, mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM productos WHERE id_producto = %s",(producto,))
    producto = cursor.fetchall()
    cursor.close()
    return producto

def elimarProductos(producto, mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM productos WHERE id_producto = %s",(producto,))
    mysql.connection.commit()
    cursor.close()
