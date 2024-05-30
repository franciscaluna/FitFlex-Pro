from flask import Flask, jsonify, request

app = Flask(__name__)


ejercicios = [
    {'Nombre': 'Brazos', 'repeticiones': 10, 'series': 4},
    {'Nombre': 'Espalda', 'repeticiones': 15, 'series': 3},
    {'Nombre': 'Piernas', 'repeticiones': 8, 'series': 5},
    {'Nombre': 'Gluteos', 'repeticiones': 20, 'series': 2},
]

# D.32: [GET] Nuestra primera API
@app.route('/saludo')
def saludo():
    return jsonify({'message': 'Bienvendio a FitFlex-Pro!'})

@app.route('/ejercicios', methods=['GET'])
def ejerciciosGet():
    return jsonify({'ejercicios':ejercicios, 'status':'ok' })

#
# D.37: [GET] Consultando información de un único producto
#
@app.route('/ejercicios/<ejercicio>', methods=['GET'])
def ejercicioGet(ejercicio):
    for indice, p in enumerate(ejercicios):
        if p['Nombre'] == ejercicio:
            return jsonify({'ejercicio':ejercicios[indice], 'busqueda':ejercicio, 'status':'ok'})
    return jsonify({'ejercicios':ejercicios, 'status':'nof found' })


#
# D.39: [POST] Dando de alta un nuevo producto
#
@app.route('/ejercicios', methods=['POST'])
def ejercicioPost():
    body = request.json
    nombre = body['Nombre']
    repeticiones = body['repeticiones']
    series = body['series']
    ejercicioAlta = {'Nombre': nombre, 'repeticiones': repeticiones, 'series': series}
    ejercicios.append(ejercicioAlta)
    return jsonify({'ejercicios':ejercicios, 'status':'ok' })

#
# D.42: [PUT] Actualiza un Producto
#             - busca por el nombre
#             - y actualiza el stock
#
@app.route('/ejercicios', methods=['PUT'])
def ejercicioPut():
    body = request.json
    nombre = body['Nombre']
    repeticiones = body['repeticiones']
    series = body['series']
    for indice, p in enumerate(ejercicios):
        if p['Nombre'] == nombre:
           p['repeticiones'] = repeticiones
           p['series'] = series
           return jsonify({'ejercicio': p,
                           'busqueda': nombre,
                           'status': 'ok'})

    return jsonify({'busqueda':ejercicios,
                    'status':'not found' })



#
# D.37: [DELETE] Consultando información de un único producto
#
@app.route('/ejercicios/<ejercicio>', methods=['DELETE'])
def ejercicioDelete(ejercicio):
    for indice, p in enumerate(ejercicios):
        if p['Nombre'] == ejercicio:
            ejercicios[indice:indice+1] = []
            return jsonify({'ejercicio':p, 'busqueda':ejercicio, 'status':'ok'})
    return jsonify({'ejercicios':ejercicios, 'status':'nof found' })




if __name__ == '__main__':
    app.run(debug=True, port=5000)