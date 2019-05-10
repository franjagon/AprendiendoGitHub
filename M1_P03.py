# Modulo 1 - Programa 3
#
#    Instrucciones
#        - se pedirá por consola que se introduzca una C o una F
#        - si se introduce C, presentar por pantalla una tabla desde 0 a 230 grados fahrenheit (de diez en diez) con sus equivalencias en grados centigrados
#                 ºC = (ºF - 32) * (5/9)
#        - si se introduce F, presentar por pantalla una tabla desde 0 a 1000 grados centigrados (de cien en cien) con sus equivalencias en grados fahrenheit
#                 ºF = (ºC * (9/5)) + 32
#
#    Restricciones
#        - gestionar errores si no se introduce un valor válido
#
#    Especificaciones
#        - crear cuantas funciones convenga

# Definición de funciones
'''No declaramos funciones'''

# Declaración de constantes
_C = "C"
_F = "F"
    
# Entrada y validación de Datos
'''Solicitamos la entrada de una C o de una F. Nos será indiferente que se introduzca la letra mayúscula o minúscula.
   Mientras no se teclee una letra correcta el programa sigue preguntando.
   Con la opción elegida fijamos el final del tramo de iteración.'''
salir = False
while not salir:
    CoF = input("Introduce una C o una F: ").upper()
    
    if CoF != _C and CoF != _F:
        print(CoF, "no sirve, debe ser una C o una F")
    else:
        print("")
        
        salir = True
        
        if CoF == _C:
            fin = 240
        else:
            fin = 110    

# Procesamiento de datos
'''Iteramos el tramo hasta el fin correspondiente a la opción elegida y para cada valor del índice escribimos una línea con el cálculo.'''
for i in range(0, fin, 10):
    if CoF == _C:
        FoC = _F
        equiv = round((i - 32) * 5 / 9, 2)
    else:
        FoC = _C
        equiv = round(32 + (i * 9 / 5), 2)
         
# Presentación de resultados
    print("{}º{}  -->  {}º{}".format(i, FoC, equiv, CoF))
