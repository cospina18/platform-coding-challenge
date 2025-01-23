import logging
import sys

def configure_logging():
    """Configura el logger principal para toda la aplicación."""
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Handler para salida estándar (stdout)
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    
    # Crear un formateador estándar con datefmt
    formatter = logging.Formatter(
        '{"time": "%(asctime)s", "level": "%(levelname)s", "logger": "%(name)s", "message": "%(message)s"}',
        datefmt='%Y-%m-%dT%H:%M:%SZ'
    )
    
    # Configurar el formateador al handler
    stdout_handler.setFormatter(formatter)
    logger.addHandler(stdout_handler)

    # Redirigir stdout y stderr a logging
    sys.stdout = StreamToLogger(logger, logging.INFO)
    sys.stderr = StreamToLogger(logger, logging.ERROR)

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

# Configurar el logging al inicio de tu aplicación