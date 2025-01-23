import pytest
import requests
from unittest.mock import patch, Mock
from finance.web.ms_info.src.infrastructure.driven_adapters.rest.suggestion_ms import Investment

@pytest.fixture
def investment():
    return Investment()

def test_get_investment_suggestion_success(mocker, investment):
    # Configurar el mock para una respuesta exitosa
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'suggestion': 'buy'}
    mocker.patch('finance.web.ms_info.src.infrastructure.driven_adapters.rest.suggestion_ms.requests.get', return_value=mock_response)

    result = investment.get_investment_suggestion('John Doe', 'Medellín', 30)

    assert result == {'suggestion': 'buy'}
    requests.get.assert_called_once_with(
        "http://ms-suggestion-app-service.web-app.svc.cluster.local:81/ms_suggestion",
        params={'nombre': 'John Doe', 'edad': 30, 'ciudad': 'Medellín'}
    )

def test_get_investment_suggestion_failure(mocker, investment):
    # Configurar el mock para una respuesta fallida
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError
    mocker.patch('finance.web.ms_info.src.infrastructure.driven_adapters.rest.suggestion_ms.requests.get', return_value=mock_response)

    result = investment.get_investment_suggestion('John Doe', 'Medellín', 30)

    assert result == "Error: suggestion unavailable"
    requests.get.assert_called_once_with(
        "http://ms-suggestion-app-service.web-app.svc.cluster.local:81/ms_suggestion",
        params={'nombre': 'John Doe', 'edad': 30, 'ciudad': 'Medellín'}
    )

def test_build_url(investment):
    url = investment._build_url()
    assert url == "http://ms-suggestion-app-service.web-app.svc.cluster.local:81/ms_suggestion"

def test_build_params(investment):
    params = investment._build_params('John Doe', 'Medellín', 30)
    assert params == {'nombre': 'John Doe', 'edad': 30, 'ciudad': 'Medellín'}

def test_make_request_success(mocker, investment):
    # Configurar el mock para una respuesta exitosa
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'suggestion': 'buy'}
    mocker.patch('finance.web.ms_info.src.infrastructure.driven_adapters.rest.suggestion_ms.requests.get', return_value=mock_response)

    url = investment._build_url()
    params = investment._build_params('John Doe', 'Medellín', 30)
    result = investment._make_request(url, params)

    assert result == {'suggestion': 'buy'}
    requests.get.assert_called_once_with(url, params=params)

def test_make_request_failure(mocker, investment):
    # Configurar el mock para una respuesta fallida
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError
    mocker.patch('finance.web.ms_info.src.infrastructure.driven_adapters.rest.suggestion_ms.requests.get', return_value=mock_response)

    url = investment._build_url()
    params = investment._build_params('John Doe', 'Medellín', 30)
    result = investment._make_request(url, params)

    assert result == "Error: suggestion unavailable"
    requests.get.assert_called_once_with(url, params=params)