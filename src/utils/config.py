from pathlib import Path

"""
Estos son los paths de las bases de datos. Archivo creado para mayor legibilidad de codigo y modularidad
Se toma en cuenta que estamos en el archivo src/utils/config.py y queremos tener el path de la carpeta data
"""

# Se aplican 3 .parent para subir 3 niveles desde config.py hasta la carpeta Bancopy
BASE_DIR = Path(__file__).resolve().parent.parent.parent


PATH_DB_TEST = BASE_DIR / "data" / "test.db"
PATH_DB_CLIENTES = BASE_DIR / "data" / "data_clientes.db"
PATH_DB_TRANSACCIONES = BASE_DIR / "data" / "data_transacciones_clientes.db"

# Configuraciones de Validación
DOMINIOS_PERMITIDOS = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com", "uac.cl", "uc.cl"]
