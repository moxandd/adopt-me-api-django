# To use Neon with Django, you have to create a Project on Neon and specify the project connection settings in your settings.py in the same way as for standalone Postgres.

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'Adopt-me-again',
    'USER': 'danya-kazakov-96',
    'PASSWORD': 'zJX3SgVBFK1N',
    'HOST': 'ep-still-band-83637146.eu-central-1.aws.neon.tech',
    'PORT': '5432',
  }
}