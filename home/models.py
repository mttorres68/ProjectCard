from django.db import models

# Create your models here.

class Disciplina(models.Model):
  name = models.CharField(max_length=40)
  description = models.CharField(max_length=100) 