from django_jinja.builtins import DEFAULT_EXTENSIONS

from coffin import COFFIN_EXTENSIONS

SECRET_KEY = 'We have no secrets.'

INSTALLED_APPS = (
    'django_jinja',
    'coffin',
)

ROOT_URLCONF = 'tests.urls'

TEMPLATES = [
    {
        "NAME": "jinja2",
        "BACKEND": "django_jinja.backend.Jinja2",
        "APP_DIRS": True,
        "OPTIONS": {
            "match_extension": ".jinja",
            "extensions": DEFAULT_EXTENSIONS + COFFIN_EXTENSIONS,
        },
    },
]