from flask import Flask, request

app = Flask(__name__)

@app.route('/ms_info')
def saludo():
    nombre = request.args.get('nombre', 'Visitante')
    edad = request.args.get('edad', 'desconocida')
    ##Caso de uso
    
    return f'Hola, {nombre}. Tienes {edad} años.'

def init_app():
    return app