from flask import Flask, jsonify, request
from finance.web.utilities.services.validation_service import validate_field
from finance.web.ms_info.src.domain.usecases.bancol_info import InfoBancol

app = Flask(__name__)

@app.route('/ms_info')
def ms_info():
    try:
        name = validate_field(request.args.get('nombre', 'Visitante'))
        age = validate_field(request.args.get('edad', 'desconocida'))
        city = validate_field(request.args.get('cuidad', 'Medellin'))
        ##Caso de uso
        local = usecase.local(name, age, city)
        response = {
            'name': name,
            'age': age,
            'city': city,
            'message': local 
        }

        return jsonify(response)
    except Exception as e:
        return jsonify({"error": "Se presentó un error", "detalle": str(e)}), 400
     

def init_app(branch, city, investment):
    global usecase
    usecase= InfoBancol(branch,city, investment)
    app.run(host='0.0.0.0', port=5000,debug=True)
    
    