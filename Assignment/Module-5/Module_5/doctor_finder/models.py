from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    years_of_experience = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"Dr. {self.name} ({self.specialty})"
