import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'module_4.settings')
django.setup()

from Question_20.models import DoctorLocation

def populate():
    doctors = [
        {
            "name": "Dr. Rajesh Varma",
            "specialization": "Cardiologist",
            "latitude": 22.2988,
            "longitude": 70.7963
        },
        {
            "name": "Dr. Anita Desai",
            "specialization": "Pediatrician",
            "latitude": 22.3055,
            "longitude": 70.8212
        },
        {
            "name": "Dr. Sameer Khan",
            "specialization": "Neurologist",
            "latitude": 22.2783,
            "longitude": 70.7905
        },
        {
            "name": "Dr. Priya Sharma",
            "specialization": "Dermatologist",
            "latitude": 22.3120,
            "longitude": 70.8010
        }
    ]

    for doc in doctors:
        DoctorLocation.objects.get_or_create(
            name=doc["name"],
            specialization=doc["specialization"],
            latitude=doc["latitude"],
            longitude=doc["longitude"]
        )
        print(f"Added/Updated: {doc['name']}")

if __name__ == "__main__":
    populate()
