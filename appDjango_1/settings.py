"""
Configuración de Django para el proyecto AppDjango_1.

Generado por 'Django-Admin StartProject' usando Django 5.0.2.

Para obtener más información sobre este archivo, consulte
#LINK -  https://docs.djangoproject.com/en/5.0/topics/settings/

Para obtener la lista completa de configuraciones y sus valores, ver
#LINK -  https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See #LINK -  https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-$c84@4ru^bv%rkcgg7h7vrm8i96p53f6vdtcu##$by)!#*6^(n"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

"""
:apps - Aplicaciones instaladas / Application definition

Son las aplicaciones instaladas que se 
estarán usando para el proyecto

:admin - Control de administración
:auth - Autenticación de usuarios
:contenttypes - Diferentes tipos de contenidos
:session - Controlar las sesiones
:messages - Controlar los mensajes
:staticfiles - Controlar la carga de archivos estáticos
:django_seed - Semillas y fabricas - #LINK - https://pypi.org/project/django-seed/

:applicationTwo - Sub aplicacion no 2
:pots - Sub aplicacion no 3
"""

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_seed",
    "applicationTwo",
    "posts",
    "school",
]

"""
:middleware - Utilidades de middleware

Los middlewares en Django son una capa de código que se ejecuta tanto 
antes como después de que una vista procese una solicitud. Estos middlewares 
pueden realizar diversas tareas, como autenticación, seguridad, manipulación de
solicitudes y respuestas, entre otras.

:securityMiddleware - Middleware de seguridad

El middleware de seguridad (SecurityMiddleware) es responsable de aplicar varias 
configuraciones de seguridad a la aplicación. Algunas de las funciones importantes 

incluyen:

- Forzar el uso de conexiones HTTPS en todas las vistas.
- Prevenir ciertos tipos de ataques, como el clickjacking, mediante el encabezado X-Frame-Options.
- Habilitar la protección contra ataques de script entre sitios (XSS).
- Configurar encabezados HTTP adicionales para mejorar la seguridad.

:sessionMiddleware - Middleware de sesiones

El middleware de sesiones (SessionMiddleware) gestiona el mantenimiento del estado de 
la sesión para cada usuario. Utiliza cookies para almacenar un identificador de sesión 
único en el navegador del cliente y almacena los datos de sesión en la base de datos o 
en la caché, según la configuración.

:commonMiddleware - Middleware común

El middleware común (CommonMiddleware) proporciona varias características comunes para 
todas las vistas, como la manipulación de encabezados HTTP, la redirección de URLs sin 
la barra final y el manejo de URL canónicas.

:csrfViewMiddleware - Middleware de protección contra CSRF

El middleware de protección contra CSRF (CsrfViewMiddleware) protege contra ataques de 
falsificación de solicitudes entre sitios (CSRF). Inserta un token CSRF único en cada
formulario enviado desde una plantilla. Cuando se procesa la solicitud, este middleware 
verifica que el token coincida con el almacenado en la sesión del usuario, 
evitando así ataques CSRF.

:authenticationMiddleware - Middleware de autenticación

El middleware de autenticación (AuthenticationMiddleware) añade el objeto de usuario 
autenticado a cada solicitud. Esto permite a las vistas acceder fácilmente al usuario 
autenticado actualmente.

:messageMiddleware - Middleware de mensajes

El middleware de mensajes (MessageMiddleware) proporciona una interfaz para 
almacenar mensajes de un solo uso, como mensajes de éxito, advertencia o error,
que pueden ser mostrados al usuario en la siguiente página solicitada.

:clickjackingMiddleware - Middleware de protección contra clickjacking

El middleware de protección contra clickjacking (XFrameOptionsMiddleware) previene 
ataques de clickjacking especificando si una página puede mostrarse dentro de un 
marco (iframe). Configura el encabezado X-Frame-Options para indicar a los 
navegadores cómo manejar el contenido embebido.

Nota: El orden de los middlewares en la lista MIDDLEWARE es importante, ya que cada 
middleware se ejecuta en secuencia, de arriba hacia abajo, en cada solicitud.
"""

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "appDjango_1.urls"


"""
:templates: application

Agregar o modificar la configuración de las plantillas (`TEMPLATES`) en `settings.py` 
de la siguiente manera:

"""

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            "templates"
        ],  # Rutas a directorios donde se buscan plantillas (opcional)
        "APP_DIRS": True,  # Habilita la búsqueda de plantillas dentro de las aplicaciones instaladas
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],  # Lista de procesadores de contexto (opcional)
        },
    },
]

WSGI_APPLICATION = "appDjango_1.wsgi.application"

"""
:database - Configuración de la base de datos 

#LINK -  https://docs.djangoproject.com/en/5.0/ref/settings/#databases

"""

DATABASES = {
    # NOTE - SQLITE . LOCAL
    # "default": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": BASE_DIR / "db.sqlite3",
    # }
    # NOTE - MYSQL
    # LINK - https://www.oracle.com/news/connect/build-web-applications-python-django.html
    # LINK - Installation - https://pypi.org/project/mysqlclient
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "django_bd_1",
        "USER": "root",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "3307",
    }
    # NOTE - ORACLE
    # LINK - https://www.oracle.com/news/connect/build-web-applications-python-django.html
    #     'default': {
    #     'ENGINE': 'django.db.backends.oracle',
    #     'NAME': 'xe',
    #     'USER': 'system',
    #     'PASSWORD': 'oracle',
    #     'HOST':'127.0.0.1',
    #     'PORT':'1521'
    # }
}


# Password validation
# #LINK -  https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# #LINK -  https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Archivos estáticos (CSS, JavaScript, Images)
# #LINK -  https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Ruta de los archivos estáticos (CSS, JavaScript, Images, etc)
STATICFILES_DIRS = [BASE_DIR / "static", "var/www/static"]

# Default primary key field type
# #LINK -  https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
