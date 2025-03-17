@echo off

REM Crear un entorno virtual
python -m venv venv

REM Activar el entorno virtual
call venv\Scripts\activate.bat

REM Instalar las dependencias
pip install -r requirements.txt

REM Levantar el servidor
python manage.py runserver
