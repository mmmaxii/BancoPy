import random
from itertools import cycle

def generar_rut() -> str:
    """Genera un RUT chileno válido aleatorio."""
    # Rango de RUTs realistas (1.000.000 a 25.000.000)
    numero = random.randint(1000000, 25000000)
    
    # Algoritmo Módulo 11 para calcular dígito verificador
    cadena_numero = str(numero)[::-1]
    suma = 0
    multiplicador = cycle([2, 3, 4, 5, 6, 7])
    
    for digito, serie in zip(cadena_numero, multiplicador):
        suma += int(digito) * serie
        
    resto = suma % 11
    dv_calculado = 11 - resto
    
    if dv_calculado == 11:
        dv = '0'
    elif dv_calculado == 10:
        dv = 'K'
    else:
        dv = str(dv_calculado)
        
    # Formatear el RUT
    rut_sin_formato = f"{numero}-{dv}"
    

    # Formato X.XXX.XXX-Y
    numero_formateado = "{:,}".format(numero).replace(",", ".")
    rut_formateado = f"{numero_formateado}-{dv}"
    
    return rut_formateado
