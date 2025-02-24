"""
Settings are loaded from environment variables, and can be overridden. The
environment variables will be loaded with the following order priority (from
highest to lowest):
- The os environment variables
- The environment ``.env.{mode}`` specific mode file
- The environment ``.env`` common file
- The default environment files provided in the constructor
- The default environment variables provided in the constructor
"""

from plateforme import Environment

# Load environment variables
env = Environment()

# Environment
DEBUG = env.as_bool('DEBUG', default=False)
SECRET_KEY = env('SECRET_KEY')

# Information
TITLE = 'Plateforme demo application'
DESCRIPTION = 'A simple demo application for the Plateforme framework.'
VERSION = '0.1.0'

# Internationalization
LANGUAGE = env('LANGUAGE', 'en-US')
TIMEZONE = env('TIMEZONE', 'UTC')

# Application
AUTO_IMPORT_DEPENDENCIES = True
AUTO_IMPORT_NAMESPACES = True

NAMESPACES = [
    ('social', {'alias': ''}),
]

PACKAGES = [
    'packages.social',
    'packages.users',
]

DATABASE_ENGINES = {
    'default': env('DATABASE', default='plateforme.db'),
}

LOGGING = {
    'level': 'DEBUG' if DEBUG else 'INFO',
    'handlers': {
        'out': {
            'type': 'file',
            'formatter': 'json',
        },
        'err': {
            'type': 'file',
            'level': 'ERROR',
            'formatter': 'default',
        },
    },
}

# Add more configuration here as needed...
