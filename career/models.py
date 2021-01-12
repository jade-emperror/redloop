from django.db import models

# Create your models here.
class jobs(models.Model):
    jobid=models.CharField(max_length=5)
    role= models.CharField(max_length=60)
    noofposition = models.IntegerField()
    skill= models.CharField(max_length=70)
    duration= models.TextField(max_length=17)