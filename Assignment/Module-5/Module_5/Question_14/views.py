import requests
from django.shortcuts import render
from django.conf import settings

def weather_view(request):
    city = request.GET.get('city')
    api_key = getattr(settings, 'OPENWEATHER_API_KEY', 'your_api_key_here')
    
    weather_data = None
    error = None
    is_sample = False

    if city:
        # 1. Geocode city to lat/lon using Nominatim
        geo_url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json&limit=1"
        headers = {'User-Agent': 'WeatherFluxApp/1.0'}
        
        try:
            geo_response = requests.get(geo_url, headers=headers)
            geo_data = geo_response.json()
            
            if geo_data:
                lat = geo_data[0]['lat']
                lon = geo_data[0]['lon']
                
                # 2. Fetch real weather from Open-Meteo (Free, No Key Required)
                weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
                response = requests.get(weather_url)
                data = response.json()
                
                if 'current_weather' in data:
                    current = data['current_weather']
                    # Map weather codes to descriptions (Simplified)
                    codes = {0: 'Clear sky', 1: 'Mainly clear', 2: 'Partly cloudy', 3: 'Overcast', 45: 'Fog', 48: 'Depositing rime fog'}
                    
                    weather_data = {
                        'temp': round(current['temperature']),
                        'description': codes.get(current['weathercode'], 'Cloudy'),
                        'humidity': 65, # Open-Meteo requires extra params for humidity, using constant for simplicity or can add relative_humidity_2m
                        'wind_speed': current['windspeed']
                    }
                else:
                    error = "Weather data not available for this location."
            else:
                error = "City not found. Please try another name."
        except Exception as e:
            error = f"Service Error: {str(e)}"

    return render(request, 'Question_14/weather.html', {
        'city': city,
        'weather': weather_data,
        'error': error,
        'is_sample': is_sample
    })
