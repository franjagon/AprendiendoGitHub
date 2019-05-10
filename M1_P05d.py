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

'''Esta función se utilizará para convertir una palabra en un diccionario con el conteo de sus letras.'''
def convertirDic(palabra):
    diccio = {}
    for letra in palabra:
        if letra in diccio:
            diccio[letra] += 1
        else:
            diccio[letra] = 1
            
    return diccio

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

# Declaración de constantes
    
# Entrada y validación de Datos
print("Voy a pedirte dos palabras y después te diré sin son anagramas\n")

palabra1 = pedirPalabra("Introduce la primera palabra: ")
palabra2 = pedirPalabra("Introduce la segunda palabra: ")

# Procesamiento de datos
'''Convertimos las palabras en diccionarios que contendrán sus letras contabilizadas. Después comparamos ambos diccionarios (con sus items
   ordenados). Si son iguales concluiremos que las palabras introducidas son anagramas.'''
diccio1 = convertirDic(palabra1)
diccio2 = convertirDic(palabra2)

sn = "no"
if sorted(diccio1.items()) == sorted(diccio2.items()):
    sn = "sí"
         
# Presentación de resultados
print("\nLas palabras {} y {}, {} son anagramas".format(palabra1, palabra2, sn))


