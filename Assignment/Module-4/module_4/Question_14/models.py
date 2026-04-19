from django.db import models

# Create your models here.
class doctor_profile(models.Model):
    name=models.CharField(max_length=40)
    specialization=models.CharField(max_length=100, default='')
    phone=models.BigIntegerField()