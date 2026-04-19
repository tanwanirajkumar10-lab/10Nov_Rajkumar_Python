from django.db import models

# Create your models here.
class userSignup(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.BigIntegerField()
    password=models.CharField(max_length=12)