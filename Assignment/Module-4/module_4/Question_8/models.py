from django.db import models

class Doctor(models.Model):
    SPECIALIZATION_CHOICES = [
        ('Cardiology', 'Cardiology'),
        ('Neurology', 'Neurology'),
        ('Orthopedics', 'Orthopedics'),
        ('Dermatology', 'Dermatology'),
        ('Pediatrics', 'Pediatrics'),
        ('Oncology', 'Oncology'),
        ('Gynecology', 'Gynecology'),
        ('General Medicine', 'General Medicine'),
        ('Ophthalmology', 'Ophthalmology'),
        ('ENT', 'ENT'),
        ('Psychiatry', 'Psychiatry'),
        ('Other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('available', 'Available'),
        ('busy', 'Busy'),
        ('on_leave', 'On Leave'),
    ]

    name             = models.CharField(max_length=200)
    specialization   = models.CharField(max_length=100, choices=SPECIALIZATION_CHOICES, default='General Medicine')
    qualification    = models.CharField(max_length=200, help_text='e.g. MBBS, MD (Cardiology)')
    phone            = models.CharField(max_length=15)
    email            = models.EmailField(unique=True)
    hospital         = models.CharField(max_length=200)
    experience       = models.PositiveIntegerField(help_text='Years of experience')
    consultation_fee = models.DecimalField(max_digits=8, decimal_places=2, default=500.00)
    timing           = models.CharField(max_length=100, default='9 AM - 5 PM')
    status           = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    bio              = models.TextField(blank=True, null=True)
    created_at       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"

    class Meta:
        ordering = ['name']
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'
