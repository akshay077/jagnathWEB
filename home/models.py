from django.db import models
from django.urls import reverse_lazy

# Create your models here.
class Service(models.Model):
    title       = models.CharField(max_length=120)
    serviceImg  = models.ImageField(upload_to='service_pics')
    description = models.TextField()
class Team(models.Model):
    Name       = models.CharField(max_length=120)
    Post       = models.CharField(max_length=120)
    description = models.ImageField(upload_to='service_pics')