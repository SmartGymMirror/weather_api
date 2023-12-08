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

    try:
        response=requests.get(weather_api_url)
        response.raise_for_status()# Si hay un error en la petición, se lanza una excepción
        weather_data = {
            'humedad': response.json()['main']['humidity'],
            'temperatura': response.json()['main']['temp'],
            'descripcion': response.json()['weather'][0]['description'],
            'icono': response.json()['weather'][0]['icon'],

        }
        return JsonResponse(weather_data, status=200)
    except requests.exceptions.HTTPError as errh:
        return JsonResponse({'error': f'Error HTTP: {errh}'}) 
    except requests.exceptions.RequestException as err:
        return JsonResponse({'error': f'Error de solicitud: {err}'}, status=500)

