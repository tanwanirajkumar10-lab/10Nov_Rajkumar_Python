import requests
from django.shortcuts import render

def country_info_view(request):
    search_name = request.GET.get('name')
    country_data = None
    error = None

    if search_name:
        # Full text search for higher accuracy
        url = f"https://restcountries.com/v3.1/name/{search_name}?fullText=true"
        try:
            response = requests.get(url)
            
            # If full text fails, try partial search
            if response.status_code != 200:
                url = f"https://restcountries.com/v3.1/name/{search_name}"
                response = requests.get(url)

            if response.status_code == 200:
                data = response.json()[0]
                
                # Extract and format data
                languages = ", ".join(data.get('languages', {}).values())
                
                currency_list = []
                for curr in data.get('currencies', {}).values():
                    currency_list.append(f"{curr.get('name')} ({curr.get('symbol')})")
                currencies = ", ".join(currency_list)

                country_data = {
                    'name': data.get('name', {}).get('common'),
                    'official_name': data.get('name', {}).get('official'),
                    'flag': data.get('flags', {}).get('png'),
                    'emoji': data.get('flag'),
                    'region': data.get('region'),
                    'subregion': data.get('subregion'),
                    'population': f"{data.get('population', 0):,}",
                    'capital': ", ".join(data.get('capital', [])),
                    'languages': languages or "N/A",
                    'currency': currencies or "N/A"
                }
            else:
                error = f"Country '{search_name}' not found. Please check the spelling."
        except Exception:
            error = "Unable to connect to the country service. Please try again later."

    return render(request, 'Question_18/country.html', {
        'search_name': search_name,
        'country': country_data,
        'error': error
    })
