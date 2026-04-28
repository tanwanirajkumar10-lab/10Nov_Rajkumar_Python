from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    experience = models.PositiveIntegerField(help_text="Experience in years")
    contact_number = models.CharField(max_length=15)
    about = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
