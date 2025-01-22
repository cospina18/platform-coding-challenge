import logging
import sys

def configure_logging():
    """Configura el logger principal para toda la aplicación."""
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Handler para salida estándar (stdout)
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_format = logging.Formatter(
        '{"time": "%(asctime)s", "level": "%(levelname)s", "logger": "%(name)s", "message": "%(message)s"}'
    )  # JSON para facilitar el parsing en Fluentd
    stdout_handler.setFormatter(stdout_format)
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
