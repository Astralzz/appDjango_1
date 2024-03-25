![alt](https://imgs.search.brave.com/xvZ9nwehnreok6qEqfTgluOLSgx52JxVedoqGUsq1mc/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9jZG4u/ZnJlZWJpZXN1cHBs/eS5jb20vbG9nb3Mv/bGFyZ2UvMngvZGph/bmdvLWNvbW11bml0/eS1sb2dvLXBuZy10/cmFuc3BhcmVudC5w/bmc)

# CURSO DE DJANGO

> Por Astral (Edain JCC)

## Tutorial

---

## Comandos para el proyecto

### Crear nueva app o proyecto

    django-admin startproject name_application

## Comando de proyecto (Manage)

- Los comandos se ejecutan a nivel de manage.py
- **_python manage.py_** es la contante y se usa en todos los comandos

### Migrar los datos a la BD

    python manage.py migrate

## Actualizar los modelos del proyecto

    python manage.py makemigrations

## Crear un super usuario

    python manage.py createsuperuser

### Ejecutar el servidor de Django

    python manage.py runserver

### Verificar problemas en nuestro proyecto

    python manage.py check

### Crear nueva sub aplicacion

    python manage.py startapp name_sub_application

### Verificar si una sub aplicacion correctamente creada

    python manage.py check applicationTwo

### Agregar n datos aleatorios

- necesita librería [django_seed](https://pypi.org/project/django-seed/)

        pip install django-seed

- necesita librería [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)

        pip install psycopg2-binary

Comando:

    python manage.py seed name_app --number=n

---
