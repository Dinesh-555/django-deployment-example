from django.db import models

class Users(models.Model):
    objects = None
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=240,unique=True)
# Create your models here.
