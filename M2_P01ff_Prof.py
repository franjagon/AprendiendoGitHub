def normal(x):
    return x

def cuadrado(x):
    return x ** 2

def cubo(x):
    return x ** 3

'''Esta función realizará la suma de Todos los resultados de la iteración de la funcion que invoquemos'''
def sumaTodos(limite, func):
    resultado = 0
    for i in range(0, limite + 1):
        resultado += func(i)
    return resultado

'''Las funciones se pueden utilizar como parametros de entrada/salida de otras funciones.'''

if __name__ == "__main__":
    print("La suma de los 100 primeros números es: {}".format(sumaTodos(100, normal)))
    print("La suma de los cuadrados de los 4 primeros números es: {}".format(sumaTodos(4, cuadrado)))
    print("La suma de los cubos de los 3 primeros números es: {}".format(sumaTodos(3, cubo)))
