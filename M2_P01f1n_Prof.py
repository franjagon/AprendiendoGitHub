def sumaTodos(limite):
    resultado = 0
    for i in range(0, limite + 1):
        resultado += i
    return resultado

def sumaCuadrados(limite):
    resultado = 0
    for i in range(0, limite + 1):
        resultado += i**2
    return resultado

'''Las funciones se pueden clonar en variables.'''

addAll = sumaTodos
addSquares = sumaCuadrados

print("La suma de los 100 primeros números es: {}".format(addAll(100)))
print("La suma de los cuadrados de los 4 primeros números es: {}".format(addSquares(4)))
