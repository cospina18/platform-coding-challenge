import requests
import logging
from finance.web.ms_info.src.domain.model.gateway.investment_gateway import InvestmentGateway
# Logger definido a nivel de módulo
logger = logging.getLogger(__name__)

class Investment(InvestmentGateway):

    def get_investment_suggestion(self, name, city, age):
        url = self._build_url()
        params = self._build_params(name, city, age)
        return self._make_request(url, params)

    def _build_url(self):
        return "http://ms-suggestion-app-service.web-app.svc.cluster.local:81/ms_suggestion"

    def _build_params(self, name, city, age):
        return {
            'nombre': name,
            'edad': age,
            'ciudad': city
        }

    def _make_request(self, url, params):
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            logger.info("request ms-suggestion-app-service.web-app.svc.cluster.local ok")
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error en la solicitud: {e}")
            return f"Error: suggestion unavailable"