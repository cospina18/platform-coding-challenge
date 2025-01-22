import logging
from finance.web.ms_info.src.infrastructure.entry_points.route_rest import init_app
from finance.web.ms_info.src.infrastructure.driven_adapters.rest.branch_info_bancol import Branches
from finance.web.ms_info.src.infrastructure.driven_adapters.rest.localization_geocode import CityCoordinates
from finance.web.ms_info.src.infrastructure.driven_adapters.rest.suggestion_ms import Investment
from finance.web.utilities.services.fluentd_logs import configure_logging


# Inicializa la configuración de logging
configure_logging()

def runner_ms_info():
     logging.getLogger(__name__)
     branch = Branches()
     city = CityCoordinates()
     investment = Investment()
     return init_app(branch, city, investment)


if __name__ == "__main__":
     runner_ms_info()
     #init_app_suggestion()

