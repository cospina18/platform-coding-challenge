from flask import Flask, request
from finance.web.utilities.services.validation_service import validate_inputs
from finance.web.ms_info.src.domain.usecases.bancol_info import InfoBancol

app = Flask(__name__)

@app.route('/ms_info')
def saludo():
    nombre = request.args.get('nombre', 'Visitante')
    edad = request.args.get('edad', 'desconocida')
    cuidad = request.args.get('cuidad', 'Medellin')
    validation_result = validate_inputs(nombre, edad)
    local = usecase.local(cuidad)
    if isinstance(validation_result, list):
        return f'Datos invalidos'
    ##Caso de uso
    return f'Hola, {nombre}. Tienes {edad} años{local}'

def init_app(branch, city):
    global usecase
    usecase= InfoBancol(branch,city)
    app.run(host='0.0.0.0', port=5000,debug=True)
    
    