Proyecto Django - Gestión de Envíos
Este proyecto está construido con Django y se gestiona a través de un entorno virtual para asegurar la independencia de las dependencias.

Requisitos previos
Python 3.x instalado.
Django instalado (puede ser instalado dentro del entorno virtual).
pip, el gestor de paquetes de Python.
Configuración del Entorno

1. Crear Entorno Virtual
   Para crear un entorno virtual llamado myenv, ejecuta el siguiente comando:
   python3 -m venv env
2. Activar el Entorno Virtual
   En Windows, activa el entorno virtual con:
   .\env\Scripts\Activate
3. Desactivar el Entorno Virtual
   Para desactivar el entorno virtual, simplemente ejecuta:
   deactivate
4. Descargar las dependencias
   pip install requirements.txt

Instalación del Proyecto Django

5. Crear el Proyecto Django
   Con el entorno virtual activado, puedes crear el proyecto utilizando el siguiente comando (dentro del directorio de tu proyecto):
   django-admin startproject envios .
   El punto (.) al final del comando asegura que los archivos del proyecto Django se creen en el directorio actual.

6. Crear una Aplicación en Django
   Una vez que el proyecto está configurado, puedes crear una aplicación llamada envios_app con el siguiente comando:
   django-admin startapp envios_app
7. Configuración del Proyecto
   Agrega la nueva app a la configuración de tu proyecto en settings.py. Busca la lista INSTALLED_APPS y añade tu aplicación de la siguiente manera:
   INSTALLED_APPS = [
   ...
   'envios_app',
   ]
8. Migraciones: Asegúrate de aplicar las migraciones iniciales para configurar la base de datos:
   python manage.py migrate

9. Ejecutar el Servidor de Desarrollo
   Para iniciar el servidor de desarrollo, utiliza el siguiente comando:
   python manage.py runserver
   El servidor estará disponible en http://127.0.0.1:8000/.

10. Crear Migraciones
    Si realizas cambios en los modelos, crea migraciones para aplicarlos en la base de datos:
    python3 manage.py makemigrations
11. Aplicar Migraciones
    Después de crear migraciones, aplícalas con:
    python manage.py migrate
12. Crear un Superusuario
    Para acceder al panel de administración de Django, necesitas crear un superusuario:
    python manage.py createsuperuser
