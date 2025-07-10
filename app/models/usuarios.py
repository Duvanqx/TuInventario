def registrarUsuario(nombres, apellidos, telefono, correo, contraseña_hash, mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO usuarios (nombres, apellidos, telefono, correo, contraseña) VALUES (%s, %s, %s, %s, %s)",
                   (nombres, apellidos, telefono, correo, contraseña_hash))
    mysql.connection.commit()
    usuario = cursor.lastrowid
    cursor.close()
    return usuario

def ObtenerUsuario(correo, mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE correo = %s",(correo,))
    usuario = cursor.fetchone()
    cursor.close()
    return usuario