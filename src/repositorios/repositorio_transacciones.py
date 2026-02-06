# Ya que tambien tendremos un registro de transacciones del tipo. Retiro, Deposito y transferencia
# lo mejor es crear una clase separad de la del repostiro de transacciones para este tipo de operaciones

from datetime import datetime

class RepositorioTransacciones:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._crear_tabla_transacciones()
    
    def _crear_tabla_transacciones(self):
        import sqlite3
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS transacciones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente_id INTEGER NOT NULL,
                tipo TEXT NOT NULL,
                monto REAL NOT NULL,
                descripcion TEXT,
                fecha TEXT NOT NULL,
                destinatario TEXT,
                FOREIGN KEY(cliente_id) REFERENCES clientes(id)
            )
            """)
            
            # Simple migration logic: try to add column if it doesn't exist (for existing DBs)
            try:
                cursor.execute("ALTER TABLE transacciones ADD COLUMN destinatario TEXT")
            except sqlite3.OperationalError:
                # Column already exists, ignore
                pass
                
            conn.commit()

    def guardar_transaccion(self, cliente_id: int, tipo: str, monto: float, descripcion: str, destinatario: str = None):
        import sqlite3
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("""
            INSERT INTO transacciones (cliente_id, tipo, monto, descripcion, fecha, destinatario)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (cliente_id, tipo, monto, descripcion, fecha_actual, destinatario))
            conn.commit()
    
    def buscar_transaccion_por_id(self, transaccion_id):
        # Implementación básica opcional
        pass
    
    def listar_por_cliente(self, cliente_id: int):
        import sqlite3
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM transacciones WHERE cliente_id = ? ORDER BY fecha DESC", (cliente_id,))
            return cursor.fetchall()
    
    def exportar_transacciones_json(self, transacciones):
        pass
    
    def exportar_transacciones_csv(self, transacciones):
        pass