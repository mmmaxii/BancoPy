# Ya que tambien tendremos un registro de transacciones del tipo. Retiro, Deposito y transferencia
# lo mejor es crear una clase separad de la del repostiro de transacciones para este tipo de operaciones

from datetime import datetime

class RepositorioTransacciones:
    def __init__(self, db_path: str, connection):
        pass
    
    def crear_tabla_transacciones(self):
        pass

    def guardar_transaccion(self, cliente_id: int, tipo: str, monto: float, descripcion: str, fecha: datetime):
        pass
    
    
    def buscar_transaccion_por_id(self, transaccion):
        pass
    
    def listar_por_cliente(self, cliente_id: int):
        pass
    
    def exportar_transacciones_json(self, transacciones):
        pass
    
    def exportar_transacciones_csv(self, transacciones):
        pass