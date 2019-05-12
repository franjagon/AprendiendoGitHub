from M2_P01ff_Prof import sumaTodos

doble = lambda x : x * 2

print(sumaTodos(3, doble))
print(sumaTodos(3, lambda x : x ** 3))

x = 3
y = 2

print("{} x {} = {}".format(x, y, lambda x, y : x * y))