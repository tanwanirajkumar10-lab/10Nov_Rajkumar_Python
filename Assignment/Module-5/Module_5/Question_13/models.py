from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)
    contact_email = models.EmailField()

    def __str__(self):
        return f"{self.name} - Available: {self.is_available}"
