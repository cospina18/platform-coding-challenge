import logging
from flask import Flask, jsonify, request
from finance.web.utilities.services.validation_service import validate_field , validate_and_extract
from finance.web.ms_info.src.domain.usecases.bancol_info import InfoBancol

logger = logging.getLogger(__name__)
app = Flask(__name__)

@app.route('/ms_info')
def ms_info():
    try:
        name = validate_and_extract(request.args, 'nombre', 'Visitante', 'str')
        age = validate_and_extract(request.args, 'edad', '18', 'int')
        city = validate_and_extract(request.args, 'cuidad', 'Medellin', 'str')
        ##Caso de uso
        investment, branch = usecase.local(name, age, city)
        response = {
            'name': name,
            'age': age,
            'city': city,
            'location': branch,
            'message_suggestion' : investment 
        }
        logger.info("Respuesta exitosa 200ok")
        return jsonify(response)
    except ValueError as e:
        return {"message": str(e)}, 400
    except Exception as e:
        logger.info("Se presento un error")
        return jsonify({"error": "Se presentó un error", "detalle": str(e)}), 400
     

def init_app(branch, city, investment):
    global usecase
    usecase= InfoBancol(branch,city, investment)
    app.run(host='0.0.0.0', port=5000,debug=True)
    
    