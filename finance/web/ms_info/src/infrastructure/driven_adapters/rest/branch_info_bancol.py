import requests
import logging
from finance.web.ms_info.src.domain.model.gateway.branch_gateway import BranchGateway

# Logger definido a nivel de módulo
logger = logging.getLogger(__name__)

class Branches(BranchGateway):

    def extract_branch_info(self, data):
        """
        Extrae información de las sucursales del dato proporcionado.

        Args:
            data (dict): Los datos de entrada que contienen información de las sucursales.

        Returns:
            str: Una cadena con la información de las sucursales y sus horarios si se encuentran,
                de lo contrario, una cadena indicando que no se encontraron sucursales.
        """
        if 'data' in data and 'channels' in data['data']:
            branches = data['data']['channels']
            return branches
        else:
            return 'Oficina no encontrada cerca.'

    def get_bancolombia_branches(self, latitude, longitude):
        try:
            # Realizar la solicitud a la API
            response = self._make_request(latitude, longitude)
            
            # Analizar la respuesta JSON
            data = response.json()
            
            return self.extract_branch_info(data)
        
        except requests.RequestException as e:
            logger.error("Request failed: %s", e)
            return 'Error en la solicitud de sucursales.'

    def _make_request(self, latitude, longitude):
        url = "https://clientes-ext.apps.bancolombia.com/portal-contenidos/physical-point/getBranches"
        headers = self._build_headers()
        payload = self._build_payload(latitude, longitude)
        return requests.post(url, headers=headers, json=payload)

    def _build_headers(self):
        return {
            "Accept": "application/vnd.bancolombia.v3+json",
            "Content-Type": "application/vnd.bancolombia.v3+json",
            "Ip": "Anonimo",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36",
            "Origin": "https://www.bancolombia.com",
            "Referer": "https://www.bancolombia.com/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "es-ES,es;q=0.9"
        }

    def _build_payload(self, latitude, longitude):
        return {
            "meta": {
                "channel": "Portal",
                "typeDocumentCode": "NA",
                "idSession": "2639160355",
                "idTransaction": "26391603552025",
                "initialYearTransaction": 2025,
                "initialMonthTransaction": 1,
                "initialDayTransaction": 19,
                "initialHourTransaction": "12:10:09 PM",
                "ipAddress": "190.250.248.227",
                "latitude": latitude,
                "longitude": longitude,
                "device": "desktop",
                "brand": "NA",
                "model": "NA",
                "os": "Windows",
                "browser": "Chrome",
                "versionOs": "10.0",
                "versionApplication": "1.1.0"
            },
            "data": {
                "latitude": latitude,
                "longitude": longitude,
                "searchRadius": 2
            }
        }