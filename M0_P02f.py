# Modulo 0 -  Programa 2 con for-in-range
#
#    Instrucciones
#        - sumar los 100 primeros números con bucle for

'''Generamos vacío el acumulador de la suma.'''
suma = 0

'''Iteramos del 1 al 101 (porque el último valor del -range- no se itera) y vamos acumulando cada valor.'''
for n in range(1, 101):
    suma = suma + n
    
print("La suma de los 100 primeros numeros es:", suma)
