from django.shortcuts import render

# Create your views here.
def q2_home(request):
    packages = [
        {"name": "Django", "description": "Core web framework"},
        {"name": "Django REST Framework", "description": "For building APIs"},
        {"name": "Requests", "description": "For making external API calls"}
    ]
    return render(request, 'q2_setup.html', {'packages': packages})
