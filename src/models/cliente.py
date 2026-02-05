"""
Clase base para representar un cliente. 
"""


from datetime import datetime

class Cliente:
    def __init__(self, id: int, nombre: str, apellido: str, email: str,
                telefono: str, direccion: str, fecha_registro: datetime, saldo: float):
            
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.fecha_registro = fecha_registro
        self.estado = "Activo"
        self._saldo = saldo
    
    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}"

    
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, value: float):
        self._saldo = value
    
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
        
