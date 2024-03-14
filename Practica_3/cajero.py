retiro = int(input(""))

def calcular_billetes(retiro):
    valorBillete = [50000, 20000, 10000, 5000, 2000, 1000]
    billetes = {}

    for valorBillete in valorBillete:
        cantidad_billetes = retiro // valorBillete
        retiro %= valorBillete
        billetes[valorBillete] = cantidad_billetes

    return billetes

billetes = calcular_billetes(retiro)

for valorBillete, cantidad in billetes.items():
    if cantidad > 0:
        print(f"{cantidad} de ${valorBillete}")