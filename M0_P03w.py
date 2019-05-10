# Modulo 0 -  Programa 3
#
#    Instrucciones
#        - De una lista numérica obtener el número de items, su suma y su media aritmética
#
#    Especificaciones
#        - formatear salidas a dos decimales

# Definición de funciones
'''Esta función pide un número mediante un mensaje que recibe y valida que sea un entero positivo.
   En función de si el segundo parámetro que recibe es menor que 3 permite introducir -N o n- para dejar de introducir numeros o no.'''
def pideNum(mensaje, cuantos):
    strNumero = input(mensaje)

    datOK = False
    while not datOK:
        if strNumero.isdigit():
            datOK = True
        elif strNumero == 'N' or strNumero == 'n':
            if cuantos < 3:
                print("La lista tiene elementos insuficientes")
                strNumero = input(mensaje)
            else:
                datOK = True
        elif cuantos < 3:
            print(strNumero, "debe ser un entero positivo")
            strNumero = input(mensaje)
        else:
            print(strNumero, "debe ser un entero positivo; si no deseas introducir más números, pulsa N o n")
            strNumero = input(mensaje)

    return(strNumero)

# Entrada de datos
'''Generamos vacía una lista que contendrá los números que se introduzcan y un contador inicializado a uno (porque pediremos el primer
   número fuera del bucle).'''
listaItems = []
solItem = 1

strItem = pideNum("Introduce el primer número de la lista: ", solItem)

'''Tras pedir el primer número, entramos en un bucle del que sólo saldremos si nos dicen que no desean introducir más numeros -N o n-,
   pero al menos se habrán de introducir los dos primeros números para la lista.'''
while strItem != 'N' and strItem != 'n':
    '''Cuando tenemos un número válido lo cargamos en la lista e incrementamos el contador.
       Si no tenemos aun dos numeros, pediremos de nuevo. si ya tenemos al menos dos números daremos la posibilidad de no introducir más.'''
    listaItems.append(int(strItem))
    solItem = solItem + 1
    if solItem < 3:
        strItem = pideNum("Introduce un segundo número para la lista: ", solItem)
    else:
        strItem = pideNum("Introduce otro número para la lista (pulsa N o n, si no deseas introducir más): ", solItem)

# Procesamiento de datos
'''Valiéndonos de los métodos de las lista obtenemos cuantos elementos tiene y su suma. Con estos valores calculamos la media aritmética.'''
numItems = len(listaItems)
suma = sum(listaItems)
media = round(suma/numItems, 2)

# Salida de datos
print("")
print("La lista tiene:", numItems, "elementos", listaItems)
print("Su suma es:", suma)
print("Su media aritmética es:", media)
