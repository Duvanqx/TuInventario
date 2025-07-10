def agregarCatalogos(usuario, nombre, fecha_inicio, fecha_fin, fecha_pago, foto,  mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO catalogos(id_usuario, nombre, fecha_inicio, fecha_fin, fecha_limite_pago, foto) VALUES (%s, %s, %s, %s, %s, %s)",
                   (usuario, nombre, fecha_inicio, fecha_fin, fecha_pago, foto))
    mysql.connection.commit()
    cursor.close()

def verCatalogos(id_usuario, mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM catalogos WHERE id_usuario = %s",(id_usuario,))
    catalogos_raw = cursor.fetchall()
    cursor.close()

    catalogos = []
    for c in catalogos_raw:
        catalogos.append((
            c[1],
            c[2],
            c[3],
            c[4],
            c[5],
            c[6],
        ))
    return catalogos_raw

def eliminarCatalogos(id_catalogo, mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM catalogos WHERE id_catalogo = %s",(id_catalogo,))
    mysql.connection.commit()
    cursor.close()

def editarCatalogos(id_catalogo, ruta_foto, nombre, fecha_inicio, fecha_fin, fecha_pago, mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE catalogos SET nombre = %s, fecha_inicio = %s, fecha_fin = %s, fecha_limite_pago = %s, foto = %s WHERE id_catalogo = %s",(nombre,fecha_inicio, fecha_fin, fecha_pago, ruta_foto, id_catalogo))
    mysql.connection.commit()
    cursor.close()

def informacionCatalogos(id_catalogo, mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM catalogos WHERE id_catalogo = %s",(id_catalogo,))
    catalogo = cursor.fetchall()
    cursor.close()
    return catalogo