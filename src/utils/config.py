from pathlib import Path

"""
Estos son los paths de las bases de datos. Archivo creado para mayor legibilidad de codigo y modularidad
"""

BASE_DIR = Path(__file__).resolve().parent.parent


PATH_DB_TEST = BASE_DIR / "data" / "test.db"
PATH_DB_CLIENTES = BASE_DIR / "data" / "data_clientes.db"
PATH_DB_TRANSACCIONES = BASE_DIR / "data" / "data_transacciones_clientes.db"


