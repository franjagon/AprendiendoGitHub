'''Esta función calcula el sumatorio de todos los números desde un número inicial hasta cero.
   Si iniciamos en positivo va restando y si iniciamos en negativo va sumando'''
def sumatorio(n):
    if n > 0:
        return n + sumatorio(n - 1)
    elif n < 0:
        return n + sumatorio(n + 1)
    else:
        return 0

'''Esta función calcula el factorial de un numero entero positivo.
   Si introducimos cero, su factorial es uno.
   Si introducimos un número negativo devuelve cero'''
def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    elif n == 1 or n == 0:
        return 1
    else:
        return 0

print(sumatorio(100))
print(sumatorio(-100))

print(factorial(4))
print(factorial(0))
print(factorial(-2))
