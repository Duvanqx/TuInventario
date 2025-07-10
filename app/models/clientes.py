def agregarClientes(usuario, nombre_completo, telefono, direccion, mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO clientes (id_usuario, nombre_completo, telefono, direccion) VALUES (%s, %s, %s, %s)",(usuario,nombre_completo,telefono,direccion))
    mysql.connection.commit()
    cursor.close()

def verClientes(usuario,mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM clientes WHERE id_usuario = %s",(usuario,))
    clientes = cursor.fetchall()
    cursor.close()
    return clientes

def eliminarClientes(id_cliente,mysql):
    cursor= mysql.connection.cursor()
    cursor.execute("DELETE FROM clientes WHERE  id_cliente = %s",(id_cliente,))
    mysql.connection.commit()
    cursor.close()

def editarClientes(nombre_completo, telefono, direccion, id_cliente, mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE clientes SET nombre_completo = %s, telefono = %s, direccion = %s WHERE id_cliente = %s",(nombre_completo, telefono, direccion, id_cliente))
    mysql.connection.commit()
    cursor.close()

def informacionClientes(id_cliente,mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM clientes WHERE id_cliente = %s",(id_cliente,))
    cliente = cursor.fetchall()
    cursor.close()
    return cliente

