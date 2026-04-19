from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    availability = models.CharField(max_length=200)
    experience_years = models.PositiveIntegerField(default=0)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"Dr. {self.name} - {self.specialty}"
