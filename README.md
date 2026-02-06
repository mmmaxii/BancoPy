# Gestor Inteligente de Clientes (GIC)

> [!WARNING]
> **PROYECTO EN DESARROLLO (WIP)**
> Este proyecto se encuentra actualmente en construcción. Muchas funcionalidades están incompletas o sujetas a cambios.

## Descripción
Sistema de gestión bancaria desarrollado en Python diseñado para administrar clientes y sus cuentas. El proyecto implementa una arquitectura en capas para separar la lógica de negocio, el acceso a datos y la interfaz de usuario.

Actualmente permite el registro de nuevos clientes, inicio de sesión seguro y gestión administrativa básica.

## Tecnologías Utilizadas
- **Lenguaje**: Python
- **Base de Datos**: SQLite (Gestión de persistencia local)
- **APIs**: SendGrid (Notificaciones por correo electrónico)
- **Librerías**: `sqlite3`, `re`, `sendgrid`

## Estructura del Proyecto

El código fuente se encuentra en el directorio `src/` y está organizado de la siguiente manera:

### `src/models/`
Contiene las clases que representan las entidades del dominio.
- `cliente.py`: Clase base `Cliente`.
- `cliente_regular.py`, `cliente_premium.py`, `cliente_vip.py`, `cliente_corporativo.py`:  Subclases que heredan de `Cliente` con atributos específicos.

### `src/repositorios/`
Capa de acceso a datos (DAO).
- `repositorio_clientes.py`: Gestiona la persistencia de clientes en SQLite (CRUD: Crear, Leer, Buscar, Eliminar).
- `repositorio_transacciones.py`: Gestiona el historial de transacciones (Depósitos, Retiros, Transferencias) vinculado a cada cliente.

### `src/services/`
Capa de lógica de negocio.
- `servicio_clientes.py`: Coordina las operaciones principales (Login, Registro, Eliminación). Implementa la lógica para reconstruir objetos desde la base de datos.
- `servicio_login_cliente.py`: Maneja la sesión del usuario activo, permitiendo consultar saldo, ver historial, depositar y transferir fondos.
- `servicio_notificaciones.py`: Integra la API de SendGrid para enviar correos de bienvenida y despedida.
- `servicio_validacion.py`: Validaciones de negocio adicionales.

### `src/utils/`
Utilidades y helpers.
- `validadores_de_formato.py`: Clase `ValidadorFormato` con métodos estáticos para validar RUT (módulo 11), email (RegEx), teléfonos, etc.
- `inputs_usuario.py`: Maneja la interacción con el usuario en consola, solicitando y limpiando los datos de entrada.
- `config.py`: Variables de configuración global (rutas de BD, etc).

### `src/menus_iniciales/`
- `menu_principal.py`: Interfaz de línea de comandos (CLI) principal que orquesta el flujo de la aplicación.
- `menu_cliente.py`: Menú específico para usuarios logueados.

## Funcionalidades Actuales
- **Gestión de Clientes**: Crear y buscar clientes.
- **Autenticación**: Inicio de sesión mediante **RUT** o **Email** y contraseña.
- **Sistema de Transacciones**:
    - **Depósitos**: Abonar dinero a la propia cuenta.
    - **Transferencias**: Enviar dinero a otros clientes del banco (validando fondos y destinatario).
    - **Historial**: Registro detallado de movimientos (tipo, monto, fecha, destinatario).
- **Validaciones**: Verificación robusta de RUT chileno y formatos de datos.
- **Notificaciones**: Envío de correos automáticos al registrarse, eliminarse o realizar transferencias (requiere API Key).
- **Límites de Saldo (Polimorfismo)**: Restricciones de saldo máximo implementadas en cada subclase mediante sobreescritura de propiedades (setters):
    - **Regular**: Máx $2M
    - **Premium**: Máx $10M
    - **VIP**: Máx $50M
    - **Corporativo**: Máx $100M
- **Modo Admin**: Funcionalidad para eliminar clientes protegida por contraseña maestra (`admin1234`).

## Limitaciones Conocidas (To-Do)
- ❌ **Interfaz Gráfica**: La interacción es 100% por consola (Terminal).
- ❌ **Dashboard**: No existen gráficos ni reportes visuales avanzados.

## Instalación y Ejecución

1. Clonar el repositorio.
2. Crear un entorno virtual e instalar dependencias:
   ```bash
   pip install sendgrid python-dotenv
   ```
3. Configurar variables de entorno en un archivo `.env` en la raíz:
   ```env
   SENDGRID_API_KEY=tu_api_key
   FROM_EMAIL=tu_email_verificado
   ```
4. Ejecutar el sistema desde la raíz del proyecto:
   ```bash
   python src/main.py
   ```
