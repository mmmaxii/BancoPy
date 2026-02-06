from services.servicio_clientes import ServicioClientes
from utils.ux_manager import UXManager

def menu_principal():
    servicio = ServicioClientes()
    
    while True:
        UXManager.mostrar_encabezado("GESTOR INTELIGENTE DE CLIENTES (GIC)")
        
        opciones = [
            "Iniciar Sesión",
            "Registrarse",
            "Ver todos los clientes (Solo Admin)",
            "Eliminar Cliente (Solo Admin)",
            "Salir"
        ]
        UXManager.mostrar_menu(opciones)
        
        opcion = UXManager.input_estilizado("Seleccione una opción")
        
        if opcion == "1":
            try:
                cliente = servicio.iniciar_sesion()
                if cliente:
                    # Redirigir al menú del cliente
                    from menus_iniciales.menu_cliente import mostrar_menu_cliente
                    mostrar_menu_cliente(cliente)
                    
            except Exception as e:
                print(f"Error al iniciar sesión: {e}")
                input("Presione ENTER para continuar...")

        elif opcion == "2":
            try:
                servicio.agregar_cliente()
                input("\nPresione ENTER para continuar...")
            except Exception as e:
                print(f"Error al registrar: {e}")
                input("Presione ENTER para continuar...")

        elif opcion == "3":
            try:
                servicio.ver_todos_los_clientes()
                input("\nPresione ENTER para continuar...")
            except Exception as e:
                print(f"Error: {e}")
                input("Presione ENTER para continuar...")

        elif opcion == "4":
            try:
                servicio.eliminar_cliente_admin()
                input("\nPresione ENTER para continuar...")
            except Exception as e:
                print(f"Error al eliminar: {e}")
                input("Presione ENTER para continuar...")

        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")
            input("Presione ENTER para continuar...")
