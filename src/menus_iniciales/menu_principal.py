from services.servicio_clientes import ServicioClientes

def menu_principal():
    servicio = ServicioClientes()
    
    while True:
        print("\n--- GESTOR INTELIGENTE DE CLIENTES (GIC) ---")
        print("1. Iniciar Sesión")
        print("2. Registrarse")
        print("3. Ver todos los clientes (Solo Admin)")
        print("4. Eliminar Cliente (Solo Admin)")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            try:
                cliente = servicio.iniciar_sesion()
                if cliente:
                    # Aquí iría el menú del cliente logueado
                    print(f"Sesión iniciada. Saldo actual: ${cliente.saldo}")
            except Exception as e:
                print(f"Error al iniciar sesión: {e}")

        elif opcion == "2":
            try:
                servicio.agregar_cliente()
            except Exception as e:
                print(f"Error al registrar: {e}")

        elif opcion == "3":
            try:
                servicio.ver_todos_los_clientes()
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "4":
            try:
                servicio.eliminar_cliente_admin()
            except Exception as e:
                print(f"Error al eliminar: {e}")

        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")
