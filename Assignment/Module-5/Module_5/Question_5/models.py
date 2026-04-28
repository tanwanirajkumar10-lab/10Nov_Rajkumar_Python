from django.db import models

# Create your models here.
class DoctorProfile(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    experience = models.IntegerField()  # years of experience
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name
