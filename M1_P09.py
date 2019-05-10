# Modulo 1 - Programa 9
#
#    Instrucciones
#        - hacer un programa que nos pida un año y que llame a un función que devuelva si es bisiesto o no.
#        - un año es bisisesto si es múltiplo de 4, excepto los que son multiplos 100 y no lo son de 400.
#
#    Restricciones
#        - gestionar errores si no se introducen años válidos (numeros enteros positivos).
#
#    Especificaciones
#        - crear cuantas funciones convenga

from datetime import *

# Definición de funciones
'''Esta función validará que la cantidad recibida (como una cadena) pueda cargarse en un tipo int. Sólo valdrán números positivos.
   Si la validación es correcta, devolverá la cantidad como un número, en caso contrario devolverá None.'''
def valAño(strAño):
    try:
        año = int(strAño)
        if año <= 0:
            año = None
    except:
        año = None

    return año

def solAño(mensaje):    
    año = None
    while año == None:
        año = valAño(input(mensaje))
        if año == None:
            print("\tEse valor no puede ser un año.")
            print("")
    
    return año

def esBisiesto(año):
    if año % 400 == 0:
        return True
    elif año % 100 == 0:
        return False
    elif año % 4 == 0:
        return True
    else:
        return False
    
def main():
    hoy = datetime.today().year
    año = solAño("Introduce un año y te diré si fue, es o será bisiesto: ")
    
    nexo = "es"
    sn = "no"
    
    if año < hoy:
        nexo = "fue"
    elif año > hoy:
        nexo = "será"
    
    if esBisiesto(año):
        sn = "sí"
    
    print("\nEl año {} {} {} bisiesto.".format(año, sn, nexo))

main()