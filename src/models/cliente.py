# TODO: Implementar clase base Cliente
# Definimos las bases de nuestro sistema. Voy a declarar lo que acepta como input 
# para mas claridad.

from datetime import datetime

class Cliente:
    def __init__(self, id: int, nombre: str, apellido: str, email: str,
                telefono: str, direccion: str, fecha_registro: datetime,
                estado: str, saldo: float):
            
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.fecha_registro = fecha_registro
        self.estado = estado
        self._saldo = saldo
    
    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}"

    
    # Voy redefinir mas tarde para que se adapte a los distintos tipos de clientes.
    def get_saldo(self):
        return self._saldo
    
    def set_saldo(self, saldo: float):
        self._saldo = saldo
    
    # esta funcion me sirvio mucho para el segundo proyecto ABP, 
    # me ayudaba a guardar los datos en un archivo JSON. Quizas 
    # lo ocupe mas adelante.

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "fecha_registro": self.fecha_registro,
            "estado": self.estado,
            "saldo": self.saldo
        }
        
