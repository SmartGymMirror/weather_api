from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import requests

def get_weather(request):
    localizacion = request.GET.get('localizacion')

    if not localizacion:
        return JsonResponse({'error': 'Debes especificar una localización'}, status=400)
    
    api_key ='' # Aquí va tu API KEY de OpenWeatherMap
    weather_api_url = f'https://api.openweathermap.org/data/2.5/weather?q={localizacion}&appid={api_key}&units=metric'
