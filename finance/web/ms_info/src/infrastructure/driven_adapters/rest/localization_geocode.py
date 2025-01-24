import requests
import logging
from finance.web.ms_info.src.domain.model.gateway.city_gateway import CityGateway
# Logger definido a nivel de módulo

# Logger definido a nivel de módulo
logger = logging.getLogger(__name__)

class CityCoordinates(CityGateway):

    def __init__(self, api_url="https://geocode.xyz"):
        self.api_url = api_url

    def get_city_coordinates(self, city_name, country_code):
        try:
            # Parámetros para la solicitud de la API
            params = self._build_params(city_name, country_code)
            
            # Realizar la solicitud a la API
            response = self._make_request(params)
            
            # Analizar la respuesta JSON
            data = response.json()
            
            # Extraer latitud y longitud
            latitude, longitude = self._extract_coordinates(data)
            
            logger.info("Request successful: %s", self.api_url)
            return latitude, longitude
        
        except requests.RequestException as e:
            logger.error("Request failed: %s", e)
            return None, None

    def _build_params(self, city_name, country_code):
        return {
            'locate': f'{city_name},{country_code}',
            'json': 1
        }

    def _make_request(self, params):
        return requests.get(self.api_url, params=params)

    def _extract_coordinates(self, data):
        latitude = data.get('latt')
        longitude = data.get('longt')
        return latitude, longitude


