from datetime import datetime
from django.db import models

# Create your models here.
class Site(models.Model):
    nome_card = models.CharField(max_length=200)
    description =  models.TextField()
    path = models.ImageField()
    date_create = models.DateTimeField(default=datetime.now, blank =True)