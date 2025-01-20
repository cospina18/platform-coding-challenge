from flask import Flask, jsonify, request
from finance.web.utilities.services.validation_service import validate_field

app = Flask(__name__)

@app.route('/ms_suggestion')
def suggestion():
    try:
        name = validate_field(request.args.get('nombre', 'Visitante'))
        age = validate_field(request.args.get('edad', 'desconocida'))
        city = validate_field(request.args.get('ciuidad', 'Medellin'))
        data = {
            'mensaje': f'Hola, {name}. Tienes {age} años y puedes aprovechar para invertir en {city}.'
        }
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": "Se presentó un error", "detalle": str(e)}), 400

def init_app_suggestion():
    app.run(host='0.0.0.0', port=5001,debug=True)
    
    