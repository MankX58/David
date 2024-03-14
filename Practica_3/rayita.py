numero1 = float(input(""))
numero2 = float(input(""))
numero3 = float(input(""))

ganador = sorted([numero1, numero2, numero3])[1]

if ganador == numero1:
    jugadora = "Andrea"
elif ganador == numero2:
    jugadora = "Sandra"
else:
    jugadora = "Milena"

print("Gana", jugadora)

