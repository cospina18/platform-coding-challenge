import logging
import sys
from datetime import datetime, timezone

def configure_logging():
    """Configura el logger principal para toda la aplicación."""
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Handler para salida estándar (stdout)
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    
    # Crear un formateador personalizado para usar el formato de hora en UTC
    formatter = CustomFormatter(
        '{"time": "%(asctime)s", "level": "%(levelname)s", "logger": "%(name)s", "message": "%(message)s"}'
    )
    
    # Configurar el formateador al handler
    stdout_handler.setFormatter(formatter)
    logger.addHandler(stdout_handler)

    # Redirigir stdout y stderr a logging
    sys.stdout = StreamToLogger(logger, logging.INFO)
    sys.stderr = StreamToLogger(logger, logging.ERROR)


class CustomFormatter(logging.Formatter):
    """Formateador personalizado para incluir el timestamp en formato UTC"""
    def formatTime(self, record, datefmt=None):
        # Obtener la hora actual en UTC y formatear como "%Y-%m-%dT%H:%M:%S"
        timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S')
        # Añadir 'Z' para indicar UTC
        return f"{timestamp}Z"

    def format(self, record):
        # Usar el formato personalizado de hora para el resto del mensaje
        record.asctime = self.formatTime(record)
        return super().format(record)

class StreamToLogger:
    """Redirige stdout y stderr al sistema de logging."""
    def __init__(self, logger, level):
        self.logger = logger
        self.level = level

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            self.logger.log(self.level, line)

    def flush(self):
        pass
