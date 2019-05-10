# Modulo 0 -  Programa 2 con while
#
#    Instrucciones
#        - sumar los 100 primeros números con bucle while

'''Generamos en vacío el acumulador de la suma, e inicializado a cero el índice.'''
suma = 0
indice = 0

'''Entramos en un bucle del que sólo saldremos cuando hayamos llegado al 100.
   Iteramos del 1 al 100 y vamos acumulando la suma.'''
salte = False
while not salte:
    indice = indice + 1
    suma = suma + indice
    
    if indice > 99:
        salte = True
    
print("La suma de los 100 primeros numeros es:", suma)
