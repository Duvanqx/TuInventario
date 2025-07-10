def verPerfiles(usuario, mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s",(usuario,))
    usuario = cursor.fetchall()
    cursor.close()
    return usuario

def editarPerfiles(nombres, apellidos, telefono, correo, usuario, mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE usuarios SET nombres = %s, apellidos = %s, telefono = %s, correo = %s WHERE id_usuario = %s",(nombres,apellidos, telefono, correo,usuario))
    mysql.connection.commit()
    cursor.close()