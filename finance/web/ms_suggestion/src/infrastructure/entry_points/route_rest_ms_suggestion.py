from flask import Flask, request
from finance.web.utilities.services.validation_service import validate_inputs
from finance.web.ms_info.src.domain.usecases.bancol_info import InfoBancol

app = Flask(__name__)

@app.route('/ms_suggestion')
def saludo():
    nombre = request.args.get('nombre', 'Visitante')
    edad = request.args.get('edad', 'desconocida')
    cuidad = request.args.get('cuidad', 'Medellin')
    validation_result = validate_inputs(nombre, edad)
    if isinstance(validation_result, list):
        return f'Datos invalidos'
    ##Caso de uso
    return f'Hola, {nombre}. Tienes {edad} años. Estas en {cuidad}'

def init_app_suggestion():
    app.run(host='0.0.0.0', port=5001,debug=True)
    
    