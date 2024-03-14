N = int(input())
L = float(input())

area = L ** 2

for i in range(N - 1):
    variacion = float(input())
    L += variacion
    area += L ** 2

print("Ramon, el area total de la estructura basica del universo es de", round(area, 2), "centimetros cuadrados")