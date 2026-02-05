import re
from utils.config import DOMINIOS_PERMITIDOS

class ValidadorFormato:
    """
    Clase encargada de validar el formato estricto de los datos.
    No verifica si el datos es real (ej. si el email existe), solo si cumple el formato visual.
    """

    @staticmethod
    def validar_email(email: str) -> bool:
        """
        Verifica que el email tenga formato correcto: usuario@dominio.com
        Ejemplo válido: juan.perez@gmail.com
        Ejemplo inválido: juan.perez@gmail
        """
        # Expresión regular estándar para emails
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(patron, email):
            raise ValueError(f"'{email}' no es un email válido.")
        
        # Validación de dominios permitidos
        dominio = email.split('@')[1]
        
        if dominio not in DOMINIOS_PERMITIDOS:
            raise ValueError(f"El dominio '{dominio}' no está permitido. Dominios válidos: {', '.join(DOMINIOS_PERMITIDOS)}")
        
        return True

    @staticmethod
    def validar_telefono(telefono: str) -> bool:
        """
        Verifica que el teléfono contenga solo números y tenga un largo razonable.
        Acepta formato internacional con + (ej: +56912345678) o local (912345678).
        """
        # Permite opcionalmente un '+' al inicio, seguido de 8 a 15 dígitos.
        patron = r'^\+?[0-9]{8,15}$'
        if not re.match(patron, telefono):
            raise ValueError(f"'{telefono}' no es un número de teléfono válido (debe tener entre 8 y 15 dígitos).")
        return True

    @staticmethod
    def validar_nombre(nombre: str) -> bool:
        """
        Verifica que el nombre contenga solo letras y espacios (no números ni símbolos raros).
        """
        if not nombre or len(nombre.strip()) == 0:
            raise ValueError("El nombre no puede estar vacío.")
        
        # Solo letras (a-z), espacios y tildes/ñ
        patron = r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$'
        if not re.match(patron, nombre):
            raise ValueError(f"'{nombre}' contiene caracteres inválidos (solo se permiten letras).")
        return True

    @staticmethod
    def validar_rut(rut: str) -> bool:
        """
        Valida formato básico de RUT Chileno (ej: 12345678-9 o 12.345.678-9).
        """
        rut = rut.replace(".", "").replace("-", "") # Limpiamos puntos y guión
        
        # Debe tener al menos 2 caracteres (número + dv)
        if len(rut) < 2:
             raise ValueError("El RUT es demasiado corto.")
        
        cuerpo = rut[:-1]
        dv = rut[-1].upper()

        if not cuerpo.isdigit():
             raise ValueError("El cuerpo del RUT debe ser numérico.")
        
        # Algoritmo de validación del DV (Módulo 11)
        suma = 0
        multiplo = 2
        for c in reversed(cuerpo):
            suma += int(c) * multiplo
            multiplo += 1
            if multiplo == 8:
                multiplo = 2
        
        esperado = 11 - (suma % 11)
        if esperado == 11:
            dv_esperado = "0"
        elif esperado == 10:
            dv_esperado = "K"
        else:
            dv_esperado = str(esperado)
        
        if dv != dv_esperado:
            raise ValueError(f"El RUT {rut} no es válido (Dígito Verificador incorrecto).")
        
        return True