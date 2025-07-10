from app.extensions import db
from datetime import datetime

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(100))
    apellidos = db.Column(db.String(100))
    telefono = db.Column(db.String(20))
    correo = db.Column(db.String(100), unique=True)
    contraseña = db.Column(db.String(255))

    productos = db.relationship('Producto', backref='usuario', cascade="all, delete-orphan", lazy=True)
    clientes = db.relationship('Cliente', backref='usuario', cascade="all, delete-orphan", lazy=True)
    catalogos = db.relationship('Catalogo', backref='usuario', cascade="all, delete-orphan", lazy=True)
    calis = db.relationship('Cali', backref='usuario', cascade="all, delete-orphan", lazy=True)


class Producto(db.Model):
    __tablename__ = 'productos'
    id_producto = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(50))
    cantidad = db.Column(db.Integer)
    descripcion = db.Column(db.Text)
    precio = db.Column(db.Numeric(10, 2))
    imagen = db.Column(db.String(255))


class Cliente(db.Model):
    __tablename__ = 'clientes'
    id_cliente = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    nombre_completo = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(20))

    calis = db.relationship('Cali', backref='cliente', cascade="all, delete-orphan", lazy=True)


class Catalogo(db.Model):
    __tablename__ = 'catalogos'
    id_catalogo = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_fin = db.Column(db.Date, nullable=False)
    fecha_limite_pago = db.Column(db.Date, nullable=False)
    foto = db.Column(db.String(255))

    calis = db.relationship('Cali', backref='catalogo', cascade="all, delete-orphan", lazy=True)


class Cali(db.Model):
    __tablename__ = 'catalogos_clientes'
    id_cali = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    id_catalogo = db.Column(db.Integer, db.ForeignKey('catalogos.id_catalogo'), nullable=False)
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id_cliente'), nullable=False)
    adeudado = db.Column(db.Numeric(10, 2), nullable=False)

    pagos = db.relationship('Pago', backref='cali', cascade="all, delete-orphan", lazy=True)


class Pago(db.Model):
    __tablename__ = 'pagos'
    id_pago = db.Column(db.Integer, primary_key=True)
    id_cali = db.Column(db.Integer, db.ForeignKey('catalogos_clientes.id_cali'), nullable=False)
    valor = db.Column(db.Numeric(10, 2))
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
