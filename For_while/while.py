import math

n = int(input("Ingrese un número: "))

while n < 0:
    print(math.sqrt(n))

print("La raiz cuadrada de", n, "es", math.sqrt(n))


