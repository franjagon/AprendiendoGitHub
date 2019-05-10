# Modulo 0 - Programa 1
#
#    Instrucciones
#        - pedir 2 números
#        - dividirlos entre 10
#        - devolver: suma, resta, multiplicación y división
#
#    Restricciones
#        - separar claramente: entrada, transformación y salida
#
#    Especificaciones
#        - formatear salidas a dos decimales
#        - gestionar errores si no se introducen números enteros

divisor = 10

'''Entramos en un bucle del que sólo saldremos cuando el segundo valor introducido sea válido y hayamos presentado los resultados del programa.'''
valid2 = False
while valid2 == False:
    '''Para forzar la entrada de un valor válido del segundo número lo intentaremos cargar en un tipo int.
       Si no se puede excepcionamos el error y repetiremos el bucle completo pidiendo de nuevo el primer número también.'''
    try:
        '''Entramos en un bucle del que sólo saldremos cuando el primer valor introducido sea válido.'''
        valid1 = False
        while valid1 == False:
            '''Para forzar la entrada de un valor válido del primer número lo intentaremos cargar en un tipo int.
               Si no se puede excepcionamos el error y repetiremos el bucle.'''
            try:
                num1 = int(input("Escribe el primer número: "))
                valid1 = True
            except:
                print("El primer número debe ser un entero")
                print("")
    
        num2 = int(input("Escribe el segundo número: "))
        valid2 = True
        
        '''Una vez tenemos dos valores válidos, realizamos los cálculos redondeados a dos decimales y presentamos los resultados.'''
        num1div = num1 / divisor
        num2div = num2 / divisor

        suma = round(num1div + num2div, 2)
        resta = round(num1div - num2div, 2)
        producto = round(num1div * num2div, 2)
        division = round(num1div / num2div, 2)

        print("")
        print("La suma:", num1div, "+", num2div, "da como resultado:", suma)
        print("La resta:", num1div, "-", num2div, "da como resultado:", resta)
        print("El producto:", num1div, "·", num2div, "da como resultado:", producto)
        print("La división:", num1div, "/", num2div, "da como resultado:", division)
    except:
        print("El segundo número debe ser un entero")
        print("")
