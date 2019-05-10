# Modulo 1 - Programa 2
#
#    Instrucciones
#        - desglosar y calcular el total de una factura
#        - se pedirá por consola que se introduzcan el precio unitario y las unidades de cada fila de la factura
#        - si se introduce un cero, bien como precio unitario, bien como cantidad, la fila se descartará y acabará el proceso de entrada de datos
#        - calcular totales y presentar factura
#
#    Restricciones
#        - se admiten entradas de números decimales para el precio unitario, pero las cantidades deberán ser números enteros
#        - gestionar errores si no se introducen valores numéricos positivos (o cero para terminar el proceso de entrada de datos)
#        - formatear los precios unitarios y el total a dos decimales
#        - limitar el desglose a diez filas
#
#    Especificaciones
#        - crear cuantas funciones convenga
#        - distinguir unidad/unidades segun la cantidad introducida

# Definición de funciones
'''Esta función validará que la cantidad recibida (como una cadena) pueda cargarse en un tipo float.
   Se la podrá invocar también para validar enteros (tipo int).
   Además del tipo elegido, se validará que sea un número positivo.
   Si la validación es correcta, devolverá la cantidad como un numero (float o int), en caso contrario devolverá None.'''
def valNumNoNeg(strNumero, como = "F"):
    if como == "F":
        try:
            numero = float(strNumero)            
            if numero < 0:
                numero = None          
        except:
            numero = None            
    elif como == "I":
        try:
            numero = int(strNumero)            
            if numero < 0:
                numero = None         
        except:
            numero = None

    return(numero)

# Declaración de constantes
_LIMITE = 10
_PRECIO = 0
_CANTIDAD = 1
    
# Entrada y validación de Datos
'''Generamos dos listas. La primera se utilizará para ir agrupando las parejas Precio/Unidades.
   En la segunda se irán cargando esas parejas como elementos.'''
parejaFila = []
listaFilas = []

'''Para ir solicitando las parejas Precio/Unidades entramos en un bucle del que sólo podremos salir de dos formas, o bien porque hayamos llegado
   a introducir el límite de parejas (que establecimos en 10), o bien porque el usuario teclee un cero (siempre y cuando haya introducido al
   menos una pareja.
   Se ejecutará el mismo bucle para pedir el precio de la pareja (que validaremos como float) y las unidades (que validaremos como int).'''
PoC = "P"
filas = 0
salir = False
while not salir and filas < _LIMITE:
    '''Entramos en un segundo bucle solicitando precio/unidades, contamos las parejas introducidas para tener en cuenta si ya se ha introducido
       alguna pareja válida (y daremos la posibilidad de salir con un cero) o no. De este bucle saldremos si se introduce una cantidad válida.'''
    datOk = False
    while not datOk:
        if filas == 0:
            if PoC == "P":
                numero = valNumNoNeg(input("Introduce el precio unitario (en €) del producto de la fila " + str(filas + 1) + " de la factura: "))
            else:
                numero = valNumNoNeg(input("  Introduce la cantidad del producto de la fila " + str(filas + 1) + " de la factura: "), como = "I")
        else:
            if PoC == "P":
                numero = valNumNoNeg(input("Introduce el precio unitario (en €) del producto de la fila " + str(filas + 1) + " de la factura (pulsa 0 para salir): "))
            else:
                numero = valNumNoNeg(input("  Introduce la cantidad del producto de la fila " + str(filas + 1) + " de la factura (pulsa 0 para salir): "), como = "I")
        
        if numero == None:
            if PoC == "P":
                print("El valor introducido no es válido. El precio unitario debe ser numérico positivo.")
            else:
                print("  El valor introducido no es válido. La cantidad debe ser numérica entera.")
                
            print("")
        else:
            datOk = True
    
    '''Si la cantidad introducida no es cero la cargamos en la lista para agruparla con su pareja.
       Si la cantidad introducida es cero y ya tenemos alguna fila válida, entonces salimos del bucle.
       Si la cantidad introducida es cero y no tenemos ninguna fila válida, lo reseñamos y volvemos al inicio del bucle.'''
    if numero > 0:
        parejaFila.append(numero)
    elif filas > 0:
        salir = True
    else:
        print("La factura está vacía - Hay que introducir al menos una fila completa")
        print("")

    '''Si no salimos del bucle por un cero (con el que estemos conformes), tendremos dos opciones:
       - Si acabamos de pedir un precio, cambiaremos el indicador para pedir en la siguiente iteración sus unidades (cantidad).
       - Si acabamos de pedir unidades, incrementamos el número de filas en uno, cargamos la pareja en la lista de parejas,
         inicializamos la lista de parejas y cambiamos el indicador para pedir en la siguiente iteración el precio de una nueva fila.'''
    if not salir and numero != 0:
        if PoC == "P":
            PoC = "C"
        else:
            PoC = "P"
            filas += 1            
            listaFilas.append(parejaFila)
            parejaFila = []
            
            print("")

# Procesamiento y cálculo
'''Inicializamos los acumuladores para el total en euros de la factura, el total de unidades y el contador de filas de detalle.'''
Total = 0
Unidades = 0
Linea = 0

print("")

'''Iteramos la lista de parejas y para cada una de ellas:
   - Calculamos su importe, el cual acumulamos al total.
   - Acumulamos sus unidades al total de unidades.
   - incrementamos en uno el contador de filas de detalle.'''
for par in listaFilas:
    importe = par[_PRECIO] * par[_CANTIDAD]
    Total += importe
    Unidades += par[_CANTIDAD]
    Linea += 1

# Presentación de resultados
    '''Si las unidades de la fila son más de una ponemos la coleta -es- al literal -unidad- y presentamos la fila de detalle.'''
    coleta = ""
    if par[_CANTIDAD] > 1:
        coleta = "es"
        
    print(" ({})\t{} €  \tx    {} unidad{}  \t= {}€".format(Linea, round(par[_PRECIO], 2), par[_CANTIDAD], coleta, round(importe, 2)))

'''Tras las filas de detalle presentamos los totales.'''    
print("-----------------------------------------------")
print(" Total:\t\t", round(Total, 2), "€")
print(" Unidades:\t\t", Unidades)