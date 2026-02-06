from services.servicio_login_cliente import LoginCliente
from models.cliente import Cliente
from utils.ux_manager import UXManager

def mostrar_menu_cliente(cliente: Cliente):
    login_cliente = LoginCliente(cliente)
    while True:
        # Recuperar saldo actualizado
        saldo_formateado = f"${cliente.saldo:,.0f}".replace(",", ".")
        tipo_cliente = cliente.__class__.__name__.replace("Cliente", "")
        subtitulo = f"Saldo: {saldo_formateado} | Plan: {tipo_cliente}"

        UXManager.mostrar_encabezado(f"BIENVENIDO {cliente.nombre.upper()} {cliente.apellido.upper()}", subtitulo)
        
        opciones = [
            "Ver transacciones",
            "Hacer deposito",
            "Hacer transferencia",
            "Servicios Especiales",
            "Cerrar sesion"
        ]
        UXManager.mostrar_menu(opciones)
        
        opcion = UXManager.input_estilizado("Seleccione una opción")
        
        if opcion == "1":
            login_cliente.ver_transacciones()
            input("\nPresione ENTER para continuar...")
        elif opcion == "2":
            login_cliente.hacer_deposito()
            input("\nPresione ENTER para continuar...")
        elif opcion == "3":
            login_cliente.hacer_transferencia()
            input("\nPresione ENTER para continuar...")
        elif opcion == "4":
            login_cliente.acceder_servicios_especiales()
            input("\nPresione ENTER para continuar...")
        elif opcion == "5":
            login_cliente.cerrar_sesion()
            break
        else:
            print("Opción inválida. Intente nuevamente.")
            input("Presione ENTER para continuar...")