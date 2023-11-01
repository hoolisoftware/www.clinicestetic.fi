from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-kj1(f!m#qm(=zila(!6$&i$%8q!ysz(gw6-p-iyw#h=^+*9xkc' # noqa ignore

DEBUG = True

ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS = True
CSRF_TRUSTED_ORIGINS = [
    'https://preview.hoolisoftware.xyz'
]
# CORS_ALLOWED_ORIGINS = [
#     'http://localhost:5173',
# ]

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'drf_recaptcha',
    'corsheaders',
    'rest_framework',
    'django_filters',

    'apps.clinic',
    'apps.blog',
    'apps.services',
    'apps.booking',
    'apps.faq'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', # noqa ignore
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', # noqa ignore
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', # noqa ignore
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', # noqa ignore
    },
]

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static/'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'], # noqa
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
    ]
}

gettext = lambda s: s # noqa ignore
LANGUAGES = (
    ('en', gettext('English')),
    ('ru', gettext('Русский')),
    ('fin', gettext('Finn')),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'

# 6LdgzN4oAAAAAAh76VbpoYQpeve2Z93N4M-bExz2
DRF_RECAPTCHA_SECRET_KEY = "6LfTJN8oAAAAAH9mtVuNoWjUqPK7SuAX7iRcpieo"
# 6LfTJN8oAAAAAIuxGZP71utUOLHBoYspKyiiygnD
# 6LfTJN8oAAAAAH9mtVuNoWjUqPK7SuAX7iRcpieo
