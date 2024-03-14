a = int(input(""))
b = int(input(""))
c = int(input(""))

ecuacion = b**2 - 4*a*c

if ecuacion > 0:
    x1 = (-b + ecuacion**0.5) / (2*a)
    x2 = (-b - ecuacion**0.5) / (2*a)
    print(f"La ecuación tiene dos soluciones reales, ellas son X1 = {round(x1, 1)} y X2 = {round(x2, 1)}")
elif ecuacion == 0:
    x = -b / (2*a)
    print(f"La ecuación tiene una solución real, ella es X = {round(x, 1)}")
else:
    print("La ecuación no tiene solución en los reales")