# Comparación: Programación Estructurada vs. Orientada a Objetos (POO)

## 1. Diferencias Fundamentales

| Característica | Programación Estructurada | Programación Orientada a Objetos (POO) |
| :--- | :--- | :--- |
| **Enfoque** | Se centra en **funciones** (acciones) que operan sobre datos. | Se centra en **objetos** que contienen tanto datos (atributos) como acciones (métodos). |
| **Organización** | El código se divide en funciones secuenciales o bloques lógicos. | El código se organiza en **clases** que modelan entidades del mundo real. |
| **Datos** | Los datos suelen ser globales o pasarse libremente entre funciones (menos control). | Los datos están **encapsulados** dentro de los objetos y protegidos del exterior. |
| **Reutilización** | Reutilización mediante funciones. Más difícil en sistemas grandes. | Alta reutilización mediante **herencia** y **polimorfismo**. |
| **Mantenimiento** | Puede volverse "código espagueti" si crece mucho. | Más fácil de mantener y escalar gracias a la modularidad. |

---

## 2. Ejemplo Práctico en Python

Imaginemos un sistema simple para gestionar una cuenta bancaria.

### A. Versión Estructurada
Aquí usamos diccionarios y funciones separadas. Los datos y la lógica están desconectados.

```python
# Datos (Diccionario)
cliente = {
    "nombre": "Juan",
    "saldo": 1000
}

# Funciones que operan sobre esos datos
def depositar(cuenta, monto):
    cuenta["saldo"] += monto
    print(f"Nuevo saldo: {cuenta['saldo']}")

def retirar(cuenta, monto):
    if monto <= cuenta["saldo"]:
        cuenta["saldo"] -= monto
        print(f"Retiraste: {monto}")
    else:
        print("Fondos insuficientes")

# Ejecución
depositar(cliente, 500)  # Saldo: 1500
retirar(cliente, 200)    # Saldo: 1300
```

### B. Versión Orientada a Objetos (POO)
Aquí unimos datos y comportamientos en una **Clase**. Usamos `__init__` para inicializar y `self` para referirnos al propio objeto.

```python
class CuentaBancaria:
    def __init__(self, nombre, saldo_inicial):
        self.nombre = nombre
        self.__saldo = saldo_inicial  # Encapsulamiento (privado)

    def depositar(self, monto):
        self.__saldo += monto
        print(f"Nuevo saldo de {self.nombre}: {self.__saldo}")

    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Retiraste: {monto}")
        else:
            print("Fondos insuficientes")

    def consultar_saldo(self):
        return self.__saldo

# Creación de Objeto (Instanciación)
mi_cuenta = CuentaBancaria("Juan", 1000)

# Interacción a través de métodos
mi_cuenta.depositar(500)  # Saldo 1500
mi_cuenta.retirar(200)    # Saldo 1300
# print(mi_cuenta.__saldo) # Error! No se puede acceder directamente (Protegido)
```

## Conclusión
La **POO** ofrece una estructura más robusta y segura, ideal para sistemas complejos como un Banco, donde es vital proteger datos sensibles como el saldo y definir reglas claras de negocio.
