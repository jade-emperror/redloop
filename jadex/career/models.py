from django.db import models

# Create your models here.
class jobs(models.Model):
    role= models.TextField()
    noofposition = models.IntegerField()
    skill= models.TextField()
    duration= models.TextField()