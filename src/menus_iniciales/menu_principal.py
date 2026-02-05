from services.servicio_clientes import ServicioClientes

def menu_principal():
    servicio = ServicioClientes()
    
    while True:
        print("\n--- GESTOR INTELIGENTE DE CLIENTES (GIC) ---")
        print("1. Crear nuevo cliente")
        print("2. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            try:
                servicio.agregar_cliente()
            except Exception as e:
                print(f"Error: {e}")
        elif opcion == "2":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")
