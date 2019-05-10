# Modulo 1 - Programa 6
#
#    Instrucciones
#        - escribir un módulo importable que devuelva el área de un triángulo
#        - el modulo podrá trabajar como programa principal y ser ejecutado recibiendo como parámetros la base y la altura del área a calcular
#
#    Restricciones
#        - gestionar como actuar si no se introducen valores válidos
#        - gestionar como actuar si no se introducen valores suficientes o si alguno/todos no sirve/n. 
#
#    Especificaciones
#        - crear cuantas funciones convenga

'''Importamos el módulo sys para poder utilizar su función -argv- que nos permitirá reconocer los parámetros que podremos (o no) pasar al programa
   si lo ejecutamos como programa principal.'''
from sys import argv

# Definición de funciones
'''Esta función se utilizará para validar los dos parámetros que recibirá la función que calculará el área del triángulo. Sólo se permitirán
   valores numéricos positivos. Si el parámetro que llega para ser analizado no es válido pediremos que se introduzca uno correcto.'''
def validarParam(nombre, strP):
    strN = strP
    datOk = False
    while not datOk:
        try:
            n = float(strN)
            
            if n > 0:
                datOk = True
            else:
               strN = input("No tengo un valor váliddo para la " + nombre + ". Introduce una cantidad que sirva: ") 
        except:
            strN = input("No tengo un valor váliddo para la " + nombre + ". Introduce una cantidad que sirva: ")
        return n
    
'''Esta función calcula y devuelve el área del triángulo. Recibe dos valores para la base y la altura y los manda validar antes de calcular.'''
def areaT(b, h):
    base = validarParam("base", b)
    high = validarParam("altura", h)
    
    return base * high / 2

'''Si el programa se ejecuta como principal nos dice su nombre y despues evalua cuantos parámetros ha recibido en su invocación.
   - Si ha recibido 2 o más: toma los dos primeros en ese orden y los asume como base y altura; con ellos llama a la función del cálculo del área.
   - Si ha recibido 1: lo toma como base y llama a la función del cálculo del área que cuando valide nos pedirá (como mínimo) la altura.
   - Si no recibe parámetros: llama a la función del cálculo del área que cuando valide nos los pedirá.'''
if __name__ == "__main__":
    print("Soy", argv[0], "actuando como programa principal")
    
    if len(argv) > 2:
        print("Superficie: {}".format(areaT(argv[1], argv[2])))
    elif len(argv) > 1:
        print("Superficie: {}".format(areaT(argv[1], None)))
    else:
        print("Superficie: {}".format(areaT(None, None)))