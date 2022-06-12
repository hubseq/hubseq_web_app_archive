from django.db import models

# Create your models here.
class DataFile(models.Model):
    name = models.CharField(max_length=30)
    datafile = models.FileField(upload_to='media/')
