# REGISTRO_TRABAJO_DJANGO

Este proyecto es una aplicación web para el registro de trabajo utilizando Django. Permite a los usuarios crear y gestionar registros de trabajo, incluyendo detalles como descripción, horas trabajadas, fecha y monto de pago. También incluye funcionalidades de manejo de usuarios, generación de reportes y gráficos.

## Características

- **Registro de Trabajo**: Crear, editar y eliminar registros de trabajo.
- **Manejo de Usuarios**: Registro y autenticación de usuarios.
- **Reportes**: Visualización de registros en una lista.
- **Interfaz de Usuario**: Formularios para entrada de datos y visualización de registros.

## Requisitos

- Python 3.x
- Django 3.x o superior

## Instalación

1. **Clona el Repositorio**:

   ```bash
   git clone https://github.com/tu_usuario/registro_trabajo.git

2. **Crea un Entorno Virtual**:
    ```bash
    python -m venv venv
    
3. **Activa el Entorno Virtual**:

   - **En Windows**:
    ```bash
    venv\Scripts\activate

  - **En macOS/Linux**:
    ```bash
    source venv/bin/activate
    
4. **Instala las Dependencias**:
   ```bash
   pip install -r requirements.txt
   
5. **Aplica las Migraciones**:
   ```bash
   python manage.py migrate
   
6. **Crea un Superusuario (para acceder al panel de administración)**:
   ```bash
   python manage.py createsuperuser
   
7. **Inicia el Servidor**:
   ```bash
   python manage.py runserver
   
8. **Accede a la Aplicación**:

Abre tu navegador y ve a http://127.0.0.1:8000/ para ver la aplicación en funcionamiento.

## Uso

Inicio de Sesión: Accede a la aplicación mediante el inicio de sesión en /accounts/login/.
Crear Registro: Ve a /registros/crear/ para crear un nuevo registro de trabajo.
Lista de Registros: Visualiza los registros en /registros/.


## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
