bultos_cabidos = 0
carga_actual = 0

capacidad_maxima = float(input())
cantidad_bultos = int(input())
pesos_bultos = []

for i in range(cantidad_bultos):
    peso = float(input())
    pesos_bultos.append(peso)

for peso in pesos_bultos:
        if carga_actual + peso <= capacidad_maxima:
            bultos_cabidos += 1
            carga_actual += peso



print("Caben", bultos_cabidos, "bultos de papa")