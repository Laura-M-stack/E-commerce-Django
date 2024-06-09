from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Categoría(models.Model):
    name = models.CharField(max_length=250)

class Meta:
    ordering = ("name", )

def __str__(self):
    return self.name

class Item(models.Model):
    categoría = models.ForeignKey(Categoría, related_name ="items", on_delete = models.CASCADE)
    name = models.CharField(max_length=250)
    descripción = models.TextField(blank=True, null=True)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to = "item_images", blank = True, null = True)
    vendido = models.BooleanField(default=False)
    fecha_de_creación = models.DateTimeField(auto_now_add = True)
    creado_por = models.ForeignKey(User, related_name="items", on_delete = models.CASCADE)