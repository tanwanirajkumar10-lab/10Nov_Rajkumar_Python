import json
from django.shortcuts import render
from django.conf import settings

def doctor_map_view(request):
    """
    Renders an OpenStreetMap showing doctors in a specific city
    using Leaflet.js and the Overpass API.
    """
    search_city = request.GET.get('city', '').strip()
    
    context = {
        'search_city': search_city,
    }
    
    return render(request, 'Question_22/map.html', context)
