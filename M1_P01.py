# Modulo 1 - Programa 1
#
#    Instrucciones
#        - pedir base y altura
#        - calcular y devolver el área de un triángulo
#
#    Restricciones
#        - se admiten entradas de números decimales
#        - gestionar errores si no se introducen valores numéricos
#        - formatear salida a dos decimales
#
#    Especificaciones
#        - crear una función para validar decimales

# Definición de funciones
'''Esta función validará que el número que recibe (como una cadena de caracteres) pueda cargarse sobre un float y que sea una cantidad mayor
   que cero. Al terminar devolverá el número en tipo float (si cumple la validación) o None (si no la cumple).'''
def valNumPos(strNumero):
    try:
        numero = float(strNumero)
        
        if numero <= 0:
            numero = None
    except:
        numero = None

    return(numero)

'''Esta función solicitará un número positivo mayor que cero (mediante un mensaje que recibe) lo mandará validar como un float y mientras no sea
   válido, lo solicitará de nuevo. Al terminar devolverá el número en tipo float.'''
def SolicNumPos(mensaje):
    datOK = False

    while not datOK:
        numSol = valNumPos(input(mensaje))
        
        if numSol == None:
            print("El valor introducido no es válido. Es necesario un valor numérico positivo mayor que cero.")
            print("")
        else:
            datOK = True

    return(numSol)
    
# Entrada y validación de Datos
'''Utilizamos la misma función para pedir la base y la altura del triángulo.'''
b = SolicNumPos("Introduce la medida de la base del triángulo: ")
h = SolicNumPos("Introduce la medida de la altura del triángulo: ")

# Procesamiento y cálculo
'''Calculamos el área del triángulo con los datos recibidos.'''
area = round((b * h) / 2, 2)

# Presentación de resultados
print("")
print("El área de un triangulo con base =", b, "y altura =", h, "es:", area)
