import os

class UXManager:
    @staticmethod
    def limpiar_pantalla():
        """Limpia la consola según el sistema operativo."""
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def mostrar_encabezado(titulo: str):
        """Muestra un encabezado decorado y centrado."""
        UXManager.limpiar_pantalla()
        ancho = 60
        print("=" * ancho)
        print(f"{titulo.center(ancho)}")
        print("=" * ancho)
        print("\n")

    @staticmethod
    def mostrar_menu(opciones: list):
        """Muestra una lista de opciones numeradas."""
        for i, opcion in enumerate(opciones, 1):
            print(f"[{i}] {opcion}")
        print("-" * 60)

    @staticmethod
    def input_estilizado(mensaje: str = "Seleccione una opción"):
        """Wrapper para input con estilo consistente."""
        return input(f"\n>> {mensaje}: ")
