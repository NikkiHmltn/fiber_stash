from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Fiber(models.Model):
    types = models.CharField(max_length=100)
    micron = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    texture = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
    return self.types