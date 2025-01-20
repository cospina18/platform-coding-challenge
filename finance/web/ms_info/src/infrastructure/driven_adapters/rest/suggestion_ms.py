import requests
from finance.web.ms_info.src.domain.model.gateway.investment_gateway import InvestmentGateway

class Investment(InvestmentGateway):

    def get_investment_suggestion(self, name, city, age):
        # Definir la URL
        url = "http://ms-suggestion-app-service.web-app.svc.cluster.local:81/ms_suggestion"
        params = {
            'nombre': name,
            'edad': age,
            'ciudad': city
        }

        # Hacer la solicitud GET
        response = requests.get(url, params=params)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            # Imprimir la respuesta en formato JSON
            return response.json()
        else:
            return f"Error: {response.status_code}"