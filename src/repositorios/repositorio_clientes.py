import sqlite3
from pathlib import Path

from models.cliente import Cliente


class RepositorioClientes:
    def __init__(self, db_path: Path):
        self.db_path = db_path
        # Conectamos a la base de datos
        self.connection = sqlite3.connect(self.db_path)
        # Hacemos que la conexion devuelva filas como diccionarios
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        # Creamos la tabla si no existe
        self._crear_tabla()

    def _crear_tabla(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            telefono TEXT,
            direccion TEXT,
            fecha_registro TEXT,
            estado TEXT,
            saldo REAL,
            tipo_cliente TEXT NOT NULL
        );
        """)
        self.connection.commit()

    def guardar_cliente(self, cliente: Cliente):
        self.cursor.execute("""
        INSERT INTO clientes (
            nombre, apellido, email, telefono, direccion,
            fecha_registro, estado, saldo, tipo_cliente
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            cliente.nombre, cliente.apellido, cliente.email,
            cliente.telefono, cliente.direccion, cliente.fecha_registro,
            cliente.estado, cliente.saldo, cliente.__class__.__name__
        ))
        
        self.connection.commit()
        # Ya que el id es autogenerado por la base de datos, 
        # se lo asignamos al cliente para que pueda ser usado mas adelante.
        cliente.id = self.cursor.lastrowid


    def actualizar_cliente(self, cliente: Cliente):
        self.cursor.execute("""
        UPDATE clientes SET
            nombre = ?, apellido = ?, email = ?, telefono = ?,
            direccion = ?, fecha_registro = ?, estado = ?,
            saldo = ?, tipo_cliente = ?
        WHERE id = ?
        """, (
            cliente.nombre, cliente.apellido, cliente.email,
            cliente.telefono, cliente.direccion, cliente.fecha_registro,
            cliente.estado, cliente.saldo, cliente.__class__.__name__,
            cliente.id
        ))
        self.connection.commit()

    def eliminar_cliente(self, cliente: Cliente):
        self.cursor.execute("DELETE FROM clientes WHERE id = ?", (cliente.id,))
        self.connection.commit()

    def buscar_cliente_por_id(self, id_cliente: int):
        self.cursor.execute("SELECT * FROM clientes WHERE id = ?", (id_cliente,))
        return self.cursor.fetchone()

    def listar_clientes(self):
        self.cursor.execute("SELECT * FROM clientes")
        return self.cursor.fetchall()

    def cerrar_conexion(self):
        self.connection.close()