from flask import Flask, jsonify, request
from finance.web.utilities.services.validation_service import validate_field
from finance.web.ms_info.src.domain.usecases.bancol_info import InfoBancol

app = Flask(__name__)

@app.route('/ms_info')
def ms_info():
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
        
        ##Caso de uso
        investment, branch = usecase.local(name, age, city)
        response = {
            'name': name,
            'age': age,
            'city': city,
            'location': branch,
            'message_suggestion' : investment 
        }

        return jsonify(response)
    except Exception as e:
        return jsonify({"error": "Se presentó un error", "detalle": str(e)}), 400
     

def init_app(branch, city, investment):
    global usecase
    usecase= InfoBancol(branch,city, investment)
    app.run(host='0.0.0.0', port=5000,debug=True)
    
    