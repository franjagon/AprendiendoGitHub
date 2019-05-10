def normal(x):
    return x

def cuadrado(x):
    return x**2

def sumaTodos(limite, func):
    resultado = 0
    for i in range(0, limite + 1):
        resultado += func(i)
    return resultado

'''Las funciones se pueden utilizar como parametros de entrada de otras funciones.'''

print("La suma de los 100 primeros números es: {}".format(sumaTodos(100, normal)))
print("La suma de los cuadrados de los 4 primeros números es: {}".format(sumaTodos(4, cuadrado)))
