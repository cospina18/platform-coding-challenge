import requests
from finance.web.ms_info.src.domain.model.gateway.branch_gateway import BranchGateway

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
            branch_info = []

            for branch in branches:
                schedules = branch.get('schedules', [])
                formatted_schedules = "\n".join([f"{schedule['day']}: {schedule['schedules']}" for schedule in schedules])
                info = f"Oficina: {branch.get('channelName')}\nHorarios:\n{formatted_schedules}"
                branch_info.append(info)

            return "\n\n" + "\n\n".join(branch_info) + "\n\n"
        else:
            return 'Oficina no encontrada cerca.'

    def get_bancolombia_branches(self, latitude, longitude):
        # API endpoint
        url = "https://clientes-ext.apps.bancolombia.com/portal-contenidos/physical-point/getBranches"
        
        # Encabezados para la solicitud de la API
        headers = {
            "Accept": "application/vnd.bancolombia.v3+json",
            "Content-Type": "application/vnd.bancolombia.v3+json",
            "Ip": "Anonimo",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36",
            "Origin": "https://www.bancolombia.com",
            "Referer": "https://www.bancolombia.com/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "es-ES,es;q=0.9"
        }
        
        # Carga útil para la solicitud de la API
        payload = {
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
        
        # Realizar la solicitud a la API
        response = requests.post(url, headers=headers, json=payload)
        
        # Analizar la respuesta JSON
        data = response.json()
        
        return self.extract_branch_info(data)

