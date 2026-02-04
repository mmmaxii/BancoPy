from pathlib import Path
from datetime import datetime

from repositorios.repositorio_clientes import RepositorioClientes
from models.cliente import Cliente

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "test.db"

repositorio = RepositorioClientes(DB_PATH)

def main():
    print("Gestor Inteligente de Clientes (GIC) iniciando...")

    cliente = Cliente(
        id=None,
        nombre="Maximiliano",
        apellido="Valderrama",
        email="maximilianovalderrama123@gmail.com",
        telefono="+56978451236",
        direccion="Av. Siempre Viva 123",
        fecha_registro=datetime.now().isoformat(),
        estado="activo",
        saldo=1000.0
    )


    cliente_2 = Cliente(
        id=None,
        nombre="Francisca",
        apellido="Rojas",
        email="fran.rojas@gmail.com",
        telefono="+56988776655",
        direccion="Calle Larga 789",
        fecha_registro=datetime.now().isoformat(),
        estado="activo",
        saldo=500.0
    )

    print("Guardando cliente...")
    repositorio.guardar_cliente(cliente)

    print("Guardando cliente 2...")
    repositorio.guardar_cliente(cliente_2)
    
    print("Listando clientes en la base:")
    clientes = repositorio.listar_clientes()

    for c in clientes:
        print(dict(c))  # sqlite3.Row -> dict

if __name__ == "__main__":
    main()
