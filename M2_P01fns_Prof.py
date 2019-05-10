def maximo(*lista):
    if len(lista) == 0:
        return 0
    
    m = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > m:
            m = lista[i]
    return m

def minimo(*lista):
    if len(lista) == 0:
        return 0
    
    m = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < m:
            m = lista[i]
    return m

def media(*lista):
    if len(lista) == 0:
        return 0
    
    suma = 0
    for i in lista:
        suma += i
    
    return suma / len(lista)

'''Las funciones pueden devolver funciones que pueden subinvocarse desde la llamada original.'''

diccioFuncs = {'maximo': maximo, 'minimo': minimo, 'media': media}

def devuelveFunc(nombre):
    nombre = nombre.lower()
    if nombre in diccioFuncs.keys():
        return diccioFuncs[nombre]
    
    return None

lista = [1, 3, -1, 15, 9]

print("El elemento máximo de la lista {} es:  {}".format(lista, devuelveFunc("maximo")(1, 3, -1, 15, 9)))
print("El elemento mínimo de la lista {} es:  {}".format(lista, devuelveFunc("minimo")(1, 3, -1, 15, 9)))
print("La media aritmética de la lista {} es: {}".format(lista, devuelveFunc("media")(1, 3, -1, 15, 9)))


        