

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&3-yj5u)v^2g$*edql&94g_08%y$6nx9ln8(%a_+oy$2g_y0h^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition
AUTH_USER_MODEL = 'accounts.Account'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'posts',
    'django_cleanup.apps.CleanupConfig',
    'ckeditor',
    'ckeditor_uploader',
]


CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'removeButtons': 'Iframe', 
        'extraPlugins':','.join([
            'html5video','youtube',
        ]),
        'width': 'auto',
        'removePlugins':'exportpdf',
        'uploadUrl': '/ckeditor/upload/', 
        'filebrowserUploadUrl': '/ckeditor/upload/',
        'filebrowserImageUploadUrl': '/ckeditor/upload/?type=images',
    },
   #for USER Form
    'minimal': {
        'toolbar': [
            {'name': 'tools', 'items': ['Maximize']},
            {'name': 'insert', 'items': ['Image','Youtube']},
            {'name': 'basicstyles', 'items': ['Bold', 'Italic',]},
            {'name': 'tools', 'items': ['Save']},
            
        ],
        'extraPlugins':','.join([
            'html5video','youtube',
        ]),
         'width':'auto',
         'resize_enabled': True, 
        'removePlugins':'exportpdf',
        'uploadUrl': '/ckeditor/upload/', 
        'filebrowserUploadUrl': '/ckeditor/upload/',
        'filebrowserImageUploadUrl': '/ckeditor/upload/?type=images',
        'image2_alignClasses': ['image-align-left', 'image-align-center', 'image-align-right'],
        'image2_disableResizer': False,
       'contentsCss': ['/static/posts/css/ckeditor.css'],

    },
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'publicblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'posts.context_processors.language_category_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'publicblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
        {
        'NAME': 'accounts.validator.CustomPasswordValidator',  #custom account password validator
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles_build','static')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Optional settings for session and CSRF security
# Uncomment and configure as needed for production
# SESSION_COOKIE_AGE = 60
# SESSION_COOKIE_DOMAIN = None
# SESSION_COOKIE_SECURE = True
# SESSION_COOKIE_HTTPONLY = True

# CSRF_COOKIE_SECURE = False
# CSRF_COOKIE_HTTPONLY = True
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# X_FRAME_OPTIONS = 'DENY'

# LOGIN_URL = '/accounts/login/'
# LOGIN_REDIRECT_URL = '/home/'


EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'  
EMAIL_HOST_USER='98ashokr@gmail.com'
FROM_EMAIL= EMAIL_HOST_USER
EMAIL_HOST_PASSWORD='kewb xizb izxs ajrx'  
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False
PASSWORD_RESET_TIMEOUT=11100



