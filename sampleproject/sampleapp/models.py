from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pictures')
    description=models.TextField()
class team(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pictures' )