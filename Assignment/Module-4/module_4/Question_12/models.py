from django.db import models

# Create your models here.
class doctorprofile(models.Model):
    name=models.CharField(max_length=20)
    specialization=models.CharField(max_length=20)
    qualification=models.CharField(max_length=40)
    experience=models.CharField(max_length=20)
    hospital=models.CharField(max_length=40)
    phone=models.BigIntegerField()
    email=models.EmailField()
    bio=models.TextField()