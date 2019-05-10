# Modulo 1 - Programa 7
#
#    Instrucciones
#        - hacer un programa que muestre el ticket con los precios de las entradas al Zoo de un grupo de personas.
#        - los precios por edades son los siguientes:
#          * menores de 2 años --> gratis
#          * hasta 12 años --> 14 €
#          * mayores de 65 años --> 18 €
#          * resto --> 23 €
#        - el programa pedirá, una a una, las edades de las personas del grupo y cuando se introduzca un cero se dará por cerrado el grupo.
#
#    Restricciones
#        - el grupo ha de tener al menos una persona.
#        - gestionar errores si no se introducen edades válidas (numeros enteros positivos).
#
#    Especificaciones
#        - crear cuantas funciones convenga

# Definición de funciones
'''Esta función validará que la cantidad recibida (como una cadena) pueda cargarse en un tipo int. No valdrán números negativos.
   Si la validación es correcta, devolverá la cantidad como un número, en caso contrario devolverá None.'''
def valEdad(strAge):
    try:
        age = int(strAge)
        if age < 0:
            age = None
    except:
        age = None

    return(age)

def pideEdad(mensaje):    
    solAge = None
    while solAge == None:
        solAge = valEdad(input(mensaje))
        if solAge == None:
            print("\tEse dato no puede ser la edad de una persona.")
            print("")
    
    return solAge
    
# Declaración de constantes
_BEBE = 'b'
_MENOR = 'm'
_NORMAL = 'n'
_JUBILADO = 'j'
    
# Entrada y validación de Datos
'''Generamos en vacío una variable para contar las personas del grupo y dos diccionarios, uno con los precios por edades de las entradas y
   otro para ir acumulando a las personas del grupo por edades.'''
pG = 0
precios = {"b": 0, "m": 14, "n": 23, "j": 18}
gente = {"b": 0, "m": 0, "n": 0, "j": 0}

'''Para ir solicitando las edades de las personas del grupo entramos en un bucle del que sólo podremos salir cuando el usuario teclee un cero
   (siempre y cuando haya introducido como mínimo la edad de una persona).'''
salir = False
while not salir:
    if pG == 0:
        edad = pideEdad("Dime la edad de la primera persona del grupo: ")
    else:
        edad = pideEdad("Dime la edad de la siguiente persona del grupo (si no hay más gente, pulsa 0): ")
    
    '''Dependiendo de la edad recibida acumulamos una unidad en la clave adecuada del diccionario de personas por edades.'''
    if edad == 0:
        if pG != 0:
            salir = True
    else:
        pG += 1 
        if edad <= 2:
            gente[_BEBE] += 1
        elif edad <= 12:
            gente[_MENOR] += 1
        elif edad <= 65:
            gente[_NORMAL] += 1
        else:
            gente[_JUBILADO] += 1
    
# Procesamiento de Datos
print("")

total = 0

'''Iteramos el dicionario de personas por edades.
   Para cada clave-valor elegimos los prefijos y sufijos gramaticales correctos para escribir el singular y el plural de forma adecuada y
   tabular perfectamente alineado el tícket, elegimos el texto adecuado para cada línea de detalle y, accediendo al diccionario de precios
   por edades, calculamos el precio unitario de cada línea del tícket (que acumulamos en el total). Una vez hecho esto imprimimos la línea.'''
for k, v in gente.items():
    a1, a2 = "", ""
    d1, d2, d3 = " ", "  ", " "
    if v > 1:
        a1, a2 = "s", "es"
        d1, d2 = "", ""
        if v > 9:
            d3 = ""            
        
    if k == _BEBE:
        t = " de bebé (0€):      " + d3
    elif k == _MENOR:
        t = " de menor" + a2 + " (14€):  " + d2 + d3
    elif k == _NORMAL:
        t = " normal" + a2 + " (23€):    " + d2 + d3
    elif k == _JUBILADO:
        t = " de jubilado (18€): " + d3
        
    pU = v * precios[k]
    total += pU
    
# Presentación de Datos
    if v != 0:
        print(" {} entrada{}{}{}{:6.2f}€".format(v, a1, t, d1, pU))       

'''Por último imprimimos el final del ticket con el total calculado.'''
print("\t\t\t     ----------\n\t\t\t{:13.2f}€".format(total))
        
   
    
    