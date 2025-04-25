Proyecto Django - Formulario Web

Este es un proyecto básico hecho con Django que permite al usuario completar un formulario con su nombre y apellido. Es ideal como introducción al desarrollo de aplicaciones web con Django.

Características

- Formulario funcional que recoge datos del usuario.
- Plantilla HTML para una interfaz sencilla.
- Estructura clara para escalar el proyecto con más campos y validaciones.

Requisitos

- Python 3.10 o superior
- pip
- Git (para clonar el repositorio)
- Django (instalable vía pip)
- (Opcional) Entorno virtual

Instalación y ejecución

1. Clona este repositorio:

git clone https://github.com/tu-usuario/mi_proyecto_django.git

cd mi_proyecto_django

2. Crea un entorno virtual y actívalo:

python -m venv env

- En windows:
  env\Scripts\activate
  
- En Mac/Linux:
  source env/bin/activate
  
3. Instala Django:

pip install Django

4. Ejecuta el servidor de desarrollo:

python manage.py runserver

5. Abre tu navegador y visita:

http://127.0.0.1:8000/

Ahí podrás ver y probar el formulario, se rellena y en el botón de generar PDF, te abre el archivo PDF con el texto escrito.
