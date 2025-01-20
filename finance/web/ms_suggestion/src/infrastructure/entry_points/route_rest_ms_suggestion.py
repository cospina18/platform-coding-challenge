from flask import Flask, jsonify, request
from finance.web.utilities.services.validation_service import validate_field

app = Flask(__name__)

@app.route('/ms_suggestion')
def suggestion():
    try:
        input = request.args.get('nombre', 'Visitante')
        validation_result = validate_field(input)
        if validation_result["valid"]:
            name = validation_result["value"]
        else:
            return {"message": "input invalid"}
        input = request.args.get('edad', '18')
        validation_result = validate_field(input)
        if validation_result["valid"]:
            age = validation_result["value"]
        else:
            return {"message": "input invalid"}
        input = request.args.get('cuidad', 'Medellin')
        validation_result = validate_field(input)
        if validation_result["valid"]:
            city = validation_result["value"]
        else:
            return {"message": "input invalid"}
        data = {
            'mensaje': f'Hola, {name}. Tienes {age} años y puedes aprovechar para invertir en {city}.'
        }
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": "Se presentó un error", "detalle": str(e)}), 400

def init_app_suggestion():
    app.run(host='0.0.0.0', port=5001,debug=True)
    
    