# Modulo 1 - Programa 3 de Ramón Maldonado

# Definición de funciones
def FtoC(g):
    return round((g - 32) * 5 / 9, 2)

def CtoF(g):
    return round(32 + (g * 9 / 5), 2)

def centigrados(ini, fin):
    for grados in range(ini, fin + 10, 10):
        print("{}ºF  -->  {}ºC".format(grados, FtoC(grados)))

def fahrenheit(ini, fin):
    for grados in range(ini, fin + 10, 10):
        print("{}ºC  -->  {}ºF".format(grados, CtoF(grados)))
  
# Entrada y validación de Datos
tipo = input("Salida (F/C): ")

if tipo == "C":
    centigrados(0, 230)
elif tipo == "F":
    fahrenheit(0, 100)
else:
    print("Tipo incorrecto")
