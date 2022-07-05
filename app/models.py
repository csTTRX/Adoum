from unicodedata import name
from django.db import models

# Create your models here.

class Formations(models.Model):
    name = models.CharField(max_length=72)
    description = models.TextField()
    start_at = models.DateField()
    end_at = models.DateField(blank=True)

class Experiences(models.Model):
    type = models.CharField(max_length=42)
    post = models.CharField(max_length=72)
    etablisment_name = models.CharField(max_length=72)
    description = models.TextField()
    start_at = models.DateField()
    end_at = models.DateField(blank=True)

class Contact(models.Model):
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()