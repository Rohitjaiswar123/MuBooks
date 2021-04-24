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
class CompsSEBooks(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    link = models.URLField(max_length=200)
    img = models.ImageField(upload_to='pics')
class EXTCSEBooks(models.Model):
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
class CompsTEBooks(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    link = models.URLField(max_length=200)
    img = models.ImageField(upload_to='pics')
class EXTCTEBooks(models.Model):
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
class CompsFEBooks(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    link = models.URLField(max_length=200)
    img = models.ImageField(upload_to='pics')
class EXTCFEBooks(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    link = models.URLField(max_length=200)
    img = models.ImageField(upload_to='pics')