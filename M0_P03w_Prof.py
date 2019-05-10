# Modulo 0 -  Programa 3 con while de Ramón Maldonado

notas = (2, 4, 6, 8)

# Definición de funciones
def contenido(lista, indice):
    try:
        resultado = lista[indice]
    except:
        resultado = None

    return resultado 

# Contar items, sumar notas y calcular media
num = 0
suma = 0

while contenido(notas, num) != None:
    suma = suma + contenido(notas, num)
    num = num + 1

media = suma / num

print("Número de items: ", num)
print("Nota total.....: ", suma)
print("Nota media.....: ", media)
