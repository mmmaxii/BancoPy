# Arquitectura del Banco: ServicioClientes

En este proyecto, la funcionalidad solicitada para la clase **"Banco"** se implementa a través de la clase **`ServicioClientes`** y su interacción con los repositorios.

Hemos decidido no crear una clase "Banco" monolítica para seguir los principios **SOLID** y la arquitectura en capas, pero la equivalencia es directa:

| Requisito de la Tarea | Implementación en BancoPy | Descripción |
| :--- | :--- | :--- |
| **Clase Banco** | `src/services/servicio_clientes.py` | Clase `ServicioClientes`. Actúa como controlador principal. |
| **Agregar Clientes** | `ServicioClientes.agregar_cliente()` | Solicita datos, instancia el objeto `Cliente` correcto (Regular, Premium, etc.) y delega el guardado. |
| **Gestionar Múltiples Clientes** | `RepositorioClientes` | `ServicioClientes` utiliza `RepositorioClientes` para manejar la colección persistente en base de datos. |
| **Consultar Información** | `ServicioClientes.ver_todos_los_clientes()` | Recupera y muestra la lista completa de clientes. |
| **Realizar Transferencias** | `LoginCliente.hacer_transferencia()` | Una vez que un cliente "entra" al banco (`iniciar_sesion`), la clase `LoginCliente` gestiona sus operaciones financieras, validando saldos y buscando al destinatario a través de los repositorios. |

## ¿Por qué esta arquitectura?

Separar la lógica en **Servicios** (Lógica de Negocio) y **Repositorios** (Acceso a Datos) es una práctica profesional que permite:
1.  **Escalabilidad**: Podemos cambiar la base de datos (de SQLite a PostgreSQL) sin tocar la lógica del banco.
2.  **Mantenimiento**: Si falla el registro, revisamos `ServicioClientes`. Si falla el guardado, revisamos `RepositorioClientes`.
3.  **Seguridad**: Las operaciones sensibles como transferencias están encapsuladas en la sesión del usuario (`LoginCliente`) en lugar de estar expuestas globalmente en el Banco.
