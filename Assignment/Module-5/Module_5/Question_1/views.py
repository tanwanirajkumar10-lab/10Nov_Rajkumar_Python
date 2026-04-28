from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def home(request):
    return render(request, 'q1_home.html')

class JokeView(APIView):
    def get(self, request):
        try:
            url = "https://official-joke-api.appspot.com/random_joke"
            response = requests.get(url)
            
            if response.status_code == 200:
                joke_data = response.json()
                
                # Displaying joke on the console
                print("\n" + "="*50)
                print("RANDOM JOKE FETCHED:")
                print(f"Setup: {joke_data.get('setup')}")
                print(f"Punchline: {joke_data.get('punchline')}")
                print("="*50 + "\n")
                
                return Response(joke_data, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Failed to fetch joke"}, status=response.status_code)
                
        except Exception as e:
            print(f"Error fetching joke: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)