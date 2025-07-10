def verClientes(usuario, mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM clientes WHERE id_usuario = %s",(usuario,))
    clientes = cursor.fetchall()
    cursor.close()
    return clientes

def agregarCalis(usuario, catalogo,cliente,adeudado,mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO catalogos_clientes (id_usuario, id_catalogo, id_cliente, adeudado) VALUES (%s, %s, %s, %s)",(usuario, catalogo, cliente, adeudado))
    mysql.connection.commit()
    cursor.close()

def verCalis(usuario, id_catalogo, mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT u.id_usuario, u.nombres AS nombre_usuario, cat.nombre AS nombre_catalogo, cli.nombre_completo AS nombre_cliente,cc.id_cali, cc.adeudado,IFNULL(SUM(p.valor), 0) AS total_abonado,(cc.adeudado - IFNULL(SUM(p.valor), 0)) AS saldo_restante FROM catalogos_clientes cc INNER JOIN usuarios u ON cc.id_usuario = u.id_usuario INNER JOIN catalogos cat ON cc.id_catalogo = cat.id_catalogo INNER JOIN clientes cli ON cc.id_cliente = cli.id_cliente LEFT JOIN pagos p ON cc.id_cali = p.id_cali WHERE cc.id_catalogo = %s AND cc.id_usuario = %s GROUP BY cc.id_cali, u.id_usuario, cat.nombre, cli.nombre_completo, cc.adeudado, u.nombres ORDER BY cli.nombre_completo", (id_catalogo, usuario))
    
    calis = cursor.fetchall()
    cursor.close()
    return calis

def agregarAbonos(cali,valor,fecha,mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO pagos (id_cali, valor, fecha) VALUES (%s, %s, %s)",(cali,valor,fecha))
    mysql.connection.commit()
    cursor.close()

def editarCalis(id_cali, cliente, dinero, usuario,  mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE catalogos_clientes SET id_cliente = %s, adeudado = %s WHERE id_cali = %s AND id_usuario = %s",(cliente, dinero, id_cali, usuario))
    mysql.connection.commit()
    cursor.close()


def obtenerCatalogos(cali, usuario,  mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id_catalogo FROM catalogos_clientes WHERE id_cali = %s AND id_usuario = %s",(cali,usuario))
    resultado = cursor.fetchone()

    if resultado is not  None:
        catalogos = resultado[0]
    else:
        print("Este catalogo no existe")
        catalogos = None
    cursor.close()
    return catalogos

def eliminarCalis(cali, mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM catalogos_clientes WHERE id_cali = %s",(cali,))
    mysql.connection.commit()
    cursor.close()
