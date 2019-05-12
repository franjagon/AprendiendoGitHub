def sumatorio(n):
    if n > 0:
        return n + sumatorio(n - 1)
    elif n < 0:
        return n + sumatorio(n + 1)
    else:
        return 0

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
