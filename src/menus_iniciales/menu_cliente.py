from services.servicio_login_cliente import LoginCliente
from models.cliente import Cliente


def mostrar_menu_cliente(cliente: Cliente):
    login_cliente = LoginCliente(cliente)
    while True:
        print("\n--- MENU CLIENTE ---")
        print("1. Ver saldo")
        print("2. Ver transacciones")
        print("3. Hacer deposito")
        print("4. Hacer transferencia")
        print("5. Servicios Especiales")
        print("6. Cerrar sesion")
        
        opcion = input("Ingrese una opcion: ")
        
        if opcion == "1":
            login_cliente.ver_saldo()
        elif opcion == "2":
            login_cliente.ver_transacciones()
        elif opcion == "3":
            login_cliente.hacer_deposito()
        elif opcion == "4":
            login_cliente.hacer_transferencia()
        elif opcion == "5":
            login_cliente.acceder_servicios_especiales()
        elif opcion == "6":
            login_cliente.cerrar_sesion()
            break
        else:
            print("Opcion invalida. Intente nuevamente.")