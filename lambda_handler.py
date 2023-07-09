import os
import sys

# Add your Django project directory to the sys.path
sys.path.append("/var/task")

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kreimben_com.settings")

# Import and configure the Django application
import django
from django.core.handlers.wsgi import WSGIHandler

django.setup()
application = WSGIHandler()
