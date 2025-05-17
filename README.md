# 1. Sitúate en la carpeta del proyecto
cd C:/Users/Rafael/Downloads/restaurante_final

# 2. Crea y activa el entorno virtual
python -m venv .venv
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Linux/macOS:
# source .venv/bin/activate

# 3. Inicializa la base de datos
python -c "from db import init_db; init_db()"

# 4. Crea el usuario administrador
python -c "from auth import crear_usuario; crear_usuario('admin','admin123') and print('Usuario creado')"

# 5. Ejecuta las pruebas automatizadas
python tests\test_app.py

# 6. Arranca la aplicación de escritorio
python main.py

## Credenciales por defecto

- **Usuario:** `admin`  
- **Contraseña:** `admin123`  

## Funcionalidades

### Gestión de Clientes
- Alta, edición y baja de clientes.  
- Campos: **nombre**, **email** (único), **teléfono**.  
- Historial de reservas por cliente.

### Gestión de Mesas
- Tabla **mesas** con `id_mesa`, `capacidad` y `estado` (disponible/ocupada).

### Reservas
- Crear reservas seleccionando **cliente**, **mesa**, **fecha**, **hora** y **número de personas**.  
- Modificar o cancelar reservas liberando la mesa.  
- Envío automático de correo de confirmación al cliente con los detalles.

### Disponibilidad de Mesas
- Consulta en tiempo real de mesas libres para la **fecha** y **hora** específicas.  


