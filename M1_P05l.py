# Modulo 1 - Programa 5
#
#    Instrucciones
#        - se pedirá por consola que se introduzcan dos palabras y se devolverá si son o no anagramas
#
#    Restricciones
#        - gestionar errores si no se introducen palabras válidas
#
#    Especificaciones
#        - crear cuantas funciones convenga

# Definición de funciones

'''Esta función se utilizará para validar la entrada de las palabras. Permitiremos únicamente cadenas que contengan caracteres alfabéticos,
sin números ni símbolos.'''
def pedirPalabra(mensaje):
    salir = False
    
    while not salir:
        palabra = input(mensaje)
        
        if len(palabra) != 0:
            if palabra.isalpha() and palabra.isalnum():
                salir = True
            else:
                print("Sólo sirven palabras con caracteres alfabéticos")
            
    return palabra

'''Esta función la llamaremos para convertir las palabras en listas de letras. Las listas tienen métodos que las cadenas no.'''
def montarLista(pal):
    listaPal = []
    for letra in pal:
        listaPal.append(letra)

    return listaPal

'''Esta función es la que analiza si las dos palabras recibidas son o no anagramas. Devolverá un valor booleano según su análisis.'''
def analizarAnagramas(pal1, pal2):
    son = False
    
    '''Lo primero que hace, si las longitudes de las palabras coinciden, es pedir la conversión de las palabras en listas de letras.'''
    if len(pal1) == len(pal2):
        lista1 = montarLista(pal1)
        lista2 = montarLista(pal2)

        '''Entramos en un primer bucle en el que vamos sacando una a una las letras de la lista1 (palabra1).'''
        salir = False
        while not salir:
            letra1 = lista1.pop()
            
            '''Con cada letra de lista1 entramos en un segundo bucle en el que, iteramos por índice la lista2, buscando su coincidencia.'''                        
            i = 0
            salir2 = False
            while i < len(lista2) and not salir2:
                
                '''Si encontramos la letra de la lista1 en lista2, salimos del segundo bucle pero quitando antes la letra de la lista2.
                   La quitamos, igual que quitamos la letra de lista1, para que no caigamos en el error de coincidir letras repetidas.
                   Si no encontramos coincidencia antes de que el índice llegue al final de lista2, saldremos del bucle sabiendo ya que
                   no son anagramas.'''
                if letra1 == lista2[i]:
                    del lista2[i]
                    salir2 = True
                i += 1
            
            '''Al salir del segundo bucle, preguntamos si hemos salido por que el índice ha recorrido toda la lista2 sin encontrar la
               coincidencia o si, por el contrario, hemos encontrado coincidencia de letras.
               En el primer caso salimos del primer bucle sin cambiar el valor por defecto del retorno (False).
               En el segundo caso preguntamos si no quedan letras para analizar en lista1, en tal caso concluiremos que son anagramas.
               Si quedan mas letras en lista1 iteraremos de nuevo el primer bucle con una nueva letra.'''                    
            if salir2 == False:
                salir = True
            elif len(lista1) == 0:
                salir = True
                son = True
                
    return son
  

# Declaración de constantes
    
# Entrada y validación de Datos
print("Voy a pedirte dos palabras y después te diré sin son anagramas\n")

palabra1 = pedirPalabra("Introduce la primera palabra: ")
palabra2 = pedirPalabra("Introduce la segunda palabra: ")

# Procesamiento de datos
sn = "no"
if analizarAnagramas(palabra1, palabra2):
    sn = "sí"
         
# Presentación de resultados
print("\nLas palabras {} y {}, {} son anagramas".format(palabra1, palabra2, sn))

