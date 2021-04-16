from django.db import models




# Create your models here.
class Sem1(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    link = models.URLField(max_length=200)
    img = models.ImageField(upload_to='pics')
class Sem2(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    link = models.URLField(max_length=200)
    img = models.ImageField(upload_to='pics')
class ITSEBooks(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    link = models.URLField(max_length=200)
    img = models.ImageField(upload_to='pics')
class MecSEBooks(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    link = models.URLField(max_length=200)
    img = models.ImageField(upload_to='pics')
class CivilSEBooks(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    link = models.URLField(max_length=200)
    img = models.ImageField(upload_to='pics')
class ElectricalSEBooks(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    link = models.URLField(max_length=200)
    img = models.ImageField(upload_to='pics')
class ITTEBooks(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    link = models.URLField(max_length=200)
    img = models.ImageField(upload_to='pics')
class MecTEBooks(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    link = models.URLField(max_length=200)
    img = models.ImageField(upload_to='pics')
class CivilTEBooks(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    link = models.URLField(max_length=200)
    img = models.ImageField(upload_to='pics')
class ElectricalTEBooks(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    link = models.URLField(max_length=200)
    img = models.ImageField(upload_to='pics')
class ITFEBooks(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    link = models.URLField(max_length=200)
    img = models.ImageField(upload_to='pics')
class MecFEBooks(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    link = models.URLField(max_length=200)
    img = models.ImageField(upload_to='pics')
class CivilFEBooks(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    link = models.URLField(max_length=200)
    img = models.ImageField(upload_to='pics')
class ElectricalFEBooks(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    link = models.URLField(max_length=200)
    img = models.ImageField(upload_to='pics')