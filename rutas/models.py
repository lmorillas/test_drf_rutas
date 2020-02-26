from django.db import models
import uuid

# Create your models here.

class Archivo(models.Model):
    rutaid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    ruta = models.CharField(max_length=512)

