import pytest
from flask import Flask, request, jsonify
from finance.web.utilities.services.validation_service import validate_field, validate_and_extract

# Define the Flask app and the suggestion route
app = Flask(__name__)

@app.route('/ms_suggestion')
def suggestion():
    try:
        name = validate_and_extract(request.args, 'nombre', 'Visitante', 'str')
        age = validate_and_extract(request.args, 'edad', '18', 'int')
        city = validate_and_extract(request.args, 'cuidad', 'Medellin', 'str')
        data = {
            'mensaje': f'Hola, {name}. puedes aprovechar para invertir!! visitanos en nuestras sedes.'
        }
        return jsonify(data)
    except ValueError as e:
        return {"message": str(e)}, 400
    except Exception as e:
        return jsonify({"error": "Se presentó un error", "detalle": str(e)}), 400

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.mark.parametrize("query_string, expected_status, expected_response", [
    ({'nombre': 'Juan', 'edad': '25', 'cuidad': 'Bogota'}, 200, {'mensaje': 'Hola, Juan. puedes aprovechar para invertir!! visitanos en nuestras sedes.'}),
    ({'nombre': 'Juan', 'edad': 'abc', 'cuidad': 'Bogota'}, 400, {"message": "invalid input"}),
    ({'nombre': 'Juan', 'edad': '25'}, 200, {'mensaje': 'Hola, Juan. puedes aprovechar para invertir!! visitanos en nuestras sedes.'}),
    ({'edad': '25', 'cuidad': 'Bogota'}, 200, {'mensaje': 'Hola, Visitante. puedes aprovechar para invertir!! visitanos en nuestras sedes.'}),
    ({'nombre': 'Juan', 'cuidad': 'Bogota'}, 200, {'mensaje': 'Hola, Juan. puedes aprovechar para invertir!! visitanos en nuestras sedes.'}),
    ({}, 200, {'mensaje': 'Hola, Visitante. puedes aprovechar para invertir!! visitanos en nuestras sedes.'}),
])
def test_suggestion(client, mocker, query_string, expected_status, expected_response):
    mocker.patch('finance.web.utilities.services.validation_service.validate_and_extract', side_effect=validate_and_extract)
    response = client.get('/ms_suggestion', query_string=query_string)
    assert response.status_code == expected_status
    assert response.get_json() == expected_response

@pytest.mark.parametrize("query_string, exception_type, expected_status", [
    ({'nombre': 'Juan', 'edad': 'abc', 'cuidad': 'Bogota'}, ValueError, 400),
     ({'nombre': 'Jua1n', 'edad': 10, 'cuidad': 'Bogota'}, ValueError, 400),
     ({'nombre': 'Jua1n', 'edad': 10, 'cuidad': 'Bogota'}, Exception, 400),
])
def test_suggestion_exceptions(client, mocker, query_string, exception_type, expected_status):
    mocker.patch('finance.web.utilities.services.validation_service.validate_and_extract', side_effect=exception_type("invalid input"))
    response = client.get('/ms_suggestion', query_string=query_string)
    assert response.status_code == expected_status

if __name__ == '__main__':
    pytest.main()