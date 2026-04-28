import requests
from django.shortcuts import render
from django.conf import settings

def geocode_view(request):
    address = request.GET.get('address')
    api_key = getattr(settings, 'GOOGLE_MAP_API_KEY', 'your_google_maps_key_here')
    
    result = None
    error = None
    is_sample = False

    if address:
        # Nominatim API Mode (OpenStreetMap)
        # Note: Nominatim requires a User-Agent header
        url = f"https://nominatim.openstreetmap.org/search?q={address}&format=json&limit=1"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data and len(data) > 0:
                    result = {
                        'formatted_address': data[0]['display_name'],
                        'lat': data[0]['lat'],
                        'lng': data[0]['lon']
                    }
                else:
                    error = "No results found. Please verify the address."
            elif response.status_code == 403:
                error = "Access Denied by Nominatim (OSM). This usually happens due to missing User-Agent or throttling."
            else:
                error = f"Geocoding service returned status code {response.status_code}."
        except Exception as e:
            error = f"Unable to connect to Geocoding service: {str(e)}"

    return render(request, 'Question_15/geocoder.html', {
        'address': address,
        'result': result,
        'error': error,
        'is_sample': is_sample
    })
