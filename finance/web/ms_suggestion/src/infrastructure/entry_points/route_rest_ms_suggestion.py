from flask import Flask, jsonify, request
from finance.web.utilities.services.validation_service import validate_field, validate_and_extract

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

def init_app_suggestion():
    app.run(host='0.0.0.0', port=5001,debug=True)
    
    