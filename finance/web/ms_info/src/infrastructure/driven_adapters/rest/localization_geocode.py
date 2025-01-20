import requests
from finance.web.ms_info.src.domain.model.gateway.city_gateway import CityGateway

class CityCoordinates(CityGateway):


    def get_city_coordinates(self, city_name, country_code):
        # API endpoint
        url = "https://geocode.xyz"
        
        # Parámetros para la solicitud de la API
        params = {
            'locate': f'{city_name},{country_code}',
            'json': 1
        }
        
        # Realizar la solicitud a la API
        response = requests.get(url, params=params)
        
        # Analizar la respuesta JSON
        data = response.json()
        
        # Extraer latitud y longitud
        latitude = data.get('latt')
        longitude = data.get('longt')
        
        return latitude, longitude


