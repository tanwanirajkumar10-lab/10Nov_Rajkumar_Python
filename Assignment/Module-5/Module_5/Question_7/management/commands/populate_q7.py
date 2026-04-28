from django.core.management.base import BaseCommand
from Question_7.models import Doctor

class Command(BaseCommand):
    help = 'Populates Question_7 Doctor model with sample data'

    def handle(self, *args, **options):
        doctors = [
            ("Dr. Alice Smith", "Cardiology"),
            ("Dr. Bob Johnson", "Neurology"),
            ("Dr. Charlie Brown", "Pediatrics"),
            ("Dr. Diana Prince", "Dermatology"),
            ("Dr. Edward Norton", "General Surgery"),
            ("Dr. Fiona Apple", "Oncology"),
            ("Dr. George Miller", "Radiology"),
            ("Dr. Hannah Abbott", "Orthopedics"),
            ("Dr. Ian McKellen", "Psychiatry"),
            ("Dr. Julie Andrews", "Obstetrics"),
            ("Dr. Kevin Hart", "Dermatology"),
            ("Dr. Lily Evans", "Pediatrics"),
            ("Dr. Matt Damon", "Cardiology"),
            ("Dr. Natalie Portman", "Neurology"),
            ("Dr. Oscar Isaac", "Orthopedics"),
        ]

        for name, specialty in doctors:
            Doctor.objects.get_or_create(name=name, specialty=specialty)
            self.stdout.write(self.style.SUCCESS(f'Successfully added {name}'))
