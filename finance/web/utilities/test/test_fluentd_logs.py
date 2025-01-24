import pytest
import logging
import sys
from io import StringIO
from unittest import mock

# Importar la función y la clase que queremos probar
from finance.web.utilities.services.fluentd_logs import configure_logging, StreamToLogger


@pytest.fixture
def capture_output():
    # Guardar el stdout y stderr originales
    original_stdout = sys.stdout
    original_stderr = sys.stderr

    # Redirigir stdout y stderr a StringIO para capturar las salidas
    captured_stdout = StringIO()
    captured_stderr = StringIO()
    sys.stdout = captured_stdout
    sys.stderr = captured_stderr

    yield captured_stdout, captured_stderr

    # Restaurar stdout y stderr originales
    sys.stdout = original_stdout
    sys.stderr = original_stderr

@mock.patch('logging.StreamHandler')
@mock.patch('logging.getLogger')
def test_configure_logging(mock_get_logger, mock_stream_handler, capture_output):
    # Crear un mock para el logger
    mock_logger = mock.Mock()
    mock_get_logger.return_value = mock_logger

    # Configurar el mock para que tenga una lista de handlers
    mock_logger.handlers = []

    # Crear un mock para el StreamHandler
    mock_handler = mock.Mock()
    mock_stream_handler.return_value = mock_handler

    # Configurar el logging
    configure_logging()

    # Verificar que el nivel del logger esté configurado a DEBUG
    mock_logger.setLevel.assert_called_once_with(logging.DEBUG)

    # Verificar que se haya añadido el handler
    mock_logger.addHandler.assert_called_once_with(mock_handler)

    # Verificar que el formateador esté configurado correctamente
    formatter = mock_handler.setFormatter.call_args[0][0]
    assert formatter._fmt == '{"time": "%(asctime)s", "level": "%(levelname)s", "logger": "%(name)s", "message": "%(message)s"}'
    assert formatter.datefmt == '%Y-%m-%dT%H:%M:%SZ'