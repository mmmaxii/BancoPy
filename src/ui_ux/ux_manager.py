import os
import random

class UXManager:
    # Variables de clase para el Easter Egg
    contador = 0
    meta_easter_egg = random.randint(10, 15)
    
    ARTE_ASCII = [
        """
          $$$$$$
        $$      $$
       $$   $$   $$   (¡Saco de Dinero!)
       $$   $$   $$
        $$      $$
          $$$$$$
        """,


        """
                     ._     __,
                      |\,../'\
                    ,'. .     `.
                   .--         '`.
                  ( `' ,          ;
                  ,`--' _,       ,'\
                 ,`.____            `.
                /              `,    |
                   '                \,   '                  (Cerdito de la suerte)
               |                /   /`,
               `,  .           ,` ./  |
               ' `.  ,'        |;,'   ,@
         ______|     |      _________,_____jv______
                `.   `.   ,'
                 ,'_,','_,
                 `'   `'
        
        """,


        """
           /\\
          /  \\
         /    \\    (¡Diamante VIP!)
        /______\\
        \\      /
         \\    /
          \\  /
           \\/
        """,
        """
         ______
        /______\\
        |  __  |   (¡Tu Banco de Confianza!)
        | |  | |
        |_|__|_|
        """
    ]

    @staticmethod
    def limpiar_pantalla():
        """Limpia la consola según el sistema operativo."""
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def _verificar_easter_egg():
        """Verifica si es momento de mostrar una sorpresa."""
        UXManager.contador += 1
        if UXManager.contador >= UXManager.meta_easter_egg:
            UXManager.limpiar_pantalla()
            arte = random.choice(UXManager.ARTE_ASCII)
            print("\n" * 2)
            print(arte.center(60))
            print("\n" + "¡HAS ENCONTRADO UN EASTER EGG!".center(60))
            input("\n" + "Presiona ENTER para reclamar tu suerte...".center(60))
            # Resetear
            UXManager.contador = 0
            UXManager.meta_easter_egg = random.randint(10, 15)

    @staticmethod
    def mostrar_encabezado(titulo: str, subtitulo: str = None):
        """Muestra un encabezado decorado y centrado."""
        # Verificar sorpresa antes de limpiar para el nuevo menú
        UXManager._verificar_easter_egg()
        
        UXManager.limpiar_pantalla()
        ancho = 60
        print("=" * ancho)
        print(f"{titulo.center(ancho)}")
        if subtitulo:
            print(f"{subtitulo.center(ancho)}")
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
