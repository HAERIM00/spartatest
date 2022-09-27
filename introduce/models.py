#user/models.py
from django.db import models

class AcceessLog(models.Model):
    class Meta:
        db_table = "my_user"

    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=64)