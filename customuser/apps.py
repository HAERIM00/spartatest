from symbol import import_from


import django
django.setup()
from customuser.models import CustomModel


class CustomuserConfig(CustomModel):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customuser'
