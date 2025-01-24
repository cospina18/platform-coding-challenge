import logging
from finance.web.ms_suggestion.src.infrastructure.entry_points.route_rest_ms_suggestion import init_app_suggestion
from finance.web.utilities.services.fluentd_logs import configure_logging

# Inicializa la configuración de logging
configure_logging()

def runner_ms_suggestion():
     logger = logging.getLogger(__name__)
     logger.info("ms_suggestion start")
     return init_app_suggestion( )


if __name__ == "__main__":
     runner_ms_suggestion()

