import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coffee_tea_shop.settings')
application = get_wsgi_application()
