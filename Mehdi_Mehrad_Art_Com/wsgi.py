"""
WSGI config for Mehdi_Mehrad_Art_Com project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mehdi_Mehrad_Art_Com.settings')

application = get_wsgi_application()
