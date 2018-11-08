from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuario(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
class Email(models.Model):
    email=models.CharField(max_length=20)
